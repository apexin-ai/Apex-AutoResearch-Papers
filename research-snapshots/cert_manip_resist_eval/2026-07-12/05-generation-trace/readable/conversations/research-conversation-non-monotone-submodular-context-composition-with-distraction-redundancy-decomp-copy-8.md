# Research conversation: Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition ## Core Problem How can post-retri

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0.jsonl`
- **Structured JSON:** [`40775ee4a36ff4c82268.json`](../../sessions/40/40775ee4a36ff4c82268.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T07:21:41.359Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T07:21:41.359Z",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "content": "# Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition\n\n## Core Problem\n\nHow can post-retrieval context composition for RAG be formalized as a constrained non-monotone submodular optimization problem that provably distinguishes between redundancy (intra-set semantic overlap) and distraction (answer-conditional interference) as separate penalty terms, yielding greedy approximation guarantees even when adding passages can decrease generation quality?\n\n## Broader Motivation\n\nThe problem of \"when does adding more information provably hurt?\" arises across context engineering: in-context learning (where Sub-CP, arXiv:2510.05130, applies submodular optimization to exemplar partitioning), tool-use composition, and multi-document grounding all exhibit non-monotone returns to context size. This work instantiates the question in RAG post-retrieval composition—including both single-hop and multi-hop QA—where it is most acute and empirically measurable, providing the first framework that decomposes the harm into redundancy and distraction with provable optimization guarantees.\n\n## Research Opportunity\n\nThree independently developed building blocks have converged but never been combined: (1) AdaGReS (arXiv Dec 2025) proved ε-approximate submodularity for redundancy-penalized context selection but only handles monotone objectives; (2) The Distracting Effect (ACL 2025) provides a concrete per-passage distraction measure DE_q(p) = 1−P(NO-RESPONSE|q,p) but performs no set-level optimization; (3) the AAMAS 2026 γ-weakly DR-submodular paper provides approximation guarantees Φ_γ for non-monotone objectives but has zero empirical applications to NLP.\n\nThe critical insight: subtracting a modular distraction penalty from AdaGReS's ε-approximately submodular objective makes the combined function non-monotone and non-submodular. The general problem class of maximizing \"approximately submodular minus modular\" functions has been studied theoretically (Qian, arXiv:1910.05492; Buchbinder et al., FOCS 2012 for the exact submodular case), but has never been instantiated in NLP or RAG. This work provides the first such instantiation, deriving the specific γ-weak DR-submodularity parameter for the RAG distraction-redundancy objective and empirically validating the AAMAS double-greedy framework in this domain.\n\n## Why Decompose Redundancy and Distraction?\n\nRedundancy and distraction damage generation quality through fundamentally different causal mechanisms, necessitating independent modeling:\n\n**Redundancy is an opportunity cost.** Repeated information wastes token budget, displacing other useful passages. Its harm is indirect—the model does not get confused by redundant content, but misses out on complementary evidence. Marginal harm diminishes: the n-th duplicate contributes less incremental information loss. This calls for a pairwise similarity penalty with diminishing marginal structure.\n\n**Distraction is an interference cost.** Irrelevant-but-plausible passages actively mislead the LLM's attention and reasoning, producing incorrect answers even when the gold passage is present. Its harm is direct and may compound: multiple distracting passages can reinforce a misleading narrative. This calls for a per-passage penalty tied to answer-conditional interference (DE_q).\n\nBecause these mechanisms have different scaling behavior and different causal pathways, a single penalty term cannot optimally control both. The decomposition into separate β (redundancy) and λ (distraction) hyperparameters allows independent calibration of each failure mode.\n\n## Research Landscape\n\nCurrent SOTA splits into two disjoint camps with a verified gap.\n\n**Camp 1 (formal guarantees, distraction-blind):** AdaGReS achieves ε-approximate submodularity with adaptive β* but only models redundancy, evaluated on 2 benchmarks. CCBQP (arXiv 2604.02554, Apr 2026) provides Frank-Wolfe with O(nd) iterations and landscape analysis via diagonal loading λ≥2, dominating MMR and DPP on the relevance-diversity Pareto frontier (QAMPARI/ASQA), but handles only relevance-diversity with no distraction term. Note that CCBQP's relevance weighting does not substitute for explicit distraction modeling: as shown in The Distracting Effect (ACL 2025), high-DE passages are often topically related to the query (moderate-to-high relevance) but answer-misleading—relevance-based weighting cannot distinguish these from genuinely helpful passages. SMART-RAG (arXiv:2409.13992, Sep 2024) uses DPP to jointly model relevance, diversity, and conflict (inter-passage contradiction), training-free, but \"conflict\" captures contradictory information between passages, not answer-conditional interference from individually misleading content. ScalDPP (arXiv:2604.03240, Apr 2026) scales DPP via P-Adapter with Diverse Margin Loss but remains in the relevance-diversity paradigm and requires training the P-Adapter.\n\n**Camp 2 (distraction-aware, no formal guarantees):** LDAR (ICLR 2026) is a distraction-aware retriever operating at retrieval time across 6 benchmarks but provides no post-retrieval composition or approximation bounds. DynamicRAG (NeurIPS 2025) uses RL with LLM feedback across 7 benchmarks but offers no optimization guarantees. Context-Picker (arXiv Dec 2025) uses two-stage RL for context selection across 5 benchmarks. Vendi-RAG (arXiv:2502.11228, Feb 2025) uses Vendi Score diversity + LLM judge for iterative diversity-quality optimization on multi-hop QA, but provides no formal guarantees and does not explicitly decompose redundancy from distraction. All learned approaches are distribution-dependent with no formal generalization guarantees under domain shift.\n\n**The gap:** No existing method is simultaneously post-retrieval, formally grounded with provable approximation bounds, and distraction-aware.\n\n## Addressing the Trivial Alternative\n\nA natural two-stage pipeline—first filter high-DE passages via threshold, then run AdaGReS's monotone greedy on survivors—appears to achieve both distraction-awareness and formal guarantees without new theory. Joint optimization is necessary because:\n\n**Pre-filtering forfeits optimality guarantees.** Removing passages before optimization shrinks the feasible set in a data-dependent, non-principled way. The resulting solution has no approximation guarantee relative to the optimal subset of the full candidate set. The joint formulation preserves the full candidate set and provides Φ_γ guarantees over it. A passage with high individual DE_q may still be the optimal choice when its relevance contribution outweighs the distraction cost in the joint objective—threshold filtering irrecoverably discards such passages.\n\nAs an empirical hypothesis, we additionally test whether set-level distraction interaction matters: the ablation includes a conditional DE_q(p|S\\{p}) variant to evaluate whether set-conditioned distraction scoring provides benefit beyond modular DE. The two-stage pipeline itself is included as an explicit ablation baseline (Ablation 7).\n\n## Proposed Approach\n\nDefine the set objective:\n\nf(S) = Σ_{p∈S} rel(q,p) − β·Σ_{p,p'∈S} sim(p,p') − λ·Σ_{p∈S} DE_q(p)\n\nwhere rel(q,p) is query-passage relevance (embedding cosine similarity), sim(p,p') is pairwise passage similarity (redundancy), and DE_q(p) is the per-passage Distracting Effect score (ACL 2025) computed via LLM no-response probability.\n\n**Why non-monotone:** The distraction penalty Σ DE_q(p) grows linearly with |S|. Beyond a critical set size, accumulated distraction cost overwhelms relevance gains, making f decrease with added passages. This non-monotonicity invalidates standard monotone greedy guarantees (AdaGReS).\n\n**Computational advantage of modular DE:** Since DE_q(p) depends only on the (q,p) pair, all DE scores can be pre-computed and cached before the greedy optimization begins. The DE computation cost is O(n) LLM calls (one per candidate passage), amortized across the optimization.\n\n**Theoretical contribution:** The relevance − redundancy component inherits AdaGReS's ε-approximate submodularity. Subtracting the modular distraction term yields a non-monotone, non-submodular function in the \"approximately submodular minus modular\" problem class (cf. Qian, arXiv:1910.05492). Our specific contribution is deriving the γ-weak DR-submodularity parameter for this RAG-specific objective under bounded-embedding conditions, enabling the AAMAS 2026 double-greedy framework with Φ_γ > γe^{−γ} approximation guarantee.\n\nThe bounded-embedding conditions require: (a) embedding norms bounded in [c_min, c_max] with c_min > 0; (b) the diminishing-return ratio of the relevance-redundancy component lower-bounded by γ > 0, which depends on the ratio c_min/c_max and the maximum pairwise similarity in the candidate set. When the candidate pool contains near-duplicate passages (sim ≈ 1), γ may degrade; we empirically measure γ on each benchmark and discuss graceful degradation.\n\n**γ as a diagnostic of composition difficulty.** Beyond its role as an algorithm parameter, γ encodes a structural property of the retrieval pool: it characterizes the gap between monotone greedy and non-monotone optimization for a given query's candidate set. When γ ≈ 1 (semantically diverse, low-redundancy pool), monotone greedy suffices and non-monotone optimization offers marginal gains. When γ ≪ 1 (high redundancy, high distraction), non-monotone optimization becomes essential. We empirically validate this by analyzing the correlation between per-query γ values and the accuracy improvement of our method over monotone baselines, establishing γ as a practical diagnostic for when sophisticated context composition is worthwhile.\n\n**Comparison with classical algorithms:** For exact non-monotone submodular functions, Buchbinder et al. (FOCS 2012) provide a 1/2-approximation via randomized double-greedy, tighter than AAMAS's Φ_γ when γ ≈ 1. Our empirically measured γ determines which framework is more appropriate. Both algorithms are included in the experimental comparison.\n\n## Experimental Design\n\n**Benchmarks:** Natural Questions (NQ), ASQA, QAMPARI, HotpotQA.\n\n**Metrics per benchmark:**\n- NQ: Exact Match (EM), token-level F1\n- ASQA: ROUGE-L, Disambig-F1 (D-F1), citation precision/recall (ALCE framework)\n- QAMPARI: Entity-level F1, entity recall\n- HotpotQA: EM, F1, supporting fact precision/recall\n- Cross-benchmark: tokens per query, wall-clock latency per query, redundancy ratio\n\n**Models:** Qwen3-Embedding-8B (retrieval + similarity), Qwen3-8B (DE scoring + secondary generator), Llama-4-Scout (primary generator).\n\n**Baselines (three groups):**\n- Simple heuristic: top-k, MMR\n- Formal optimization: AdaGReS, CCBQP, SMART-RAG\n- Learned: DynamicRAG, LDAR, Context-Picker, Vendi-RAG\n\n**LDAR comparison protocol:** Two settings: (a) Retrieval-controlled—all methods use Qwen3-Embedding-8B top-N candidates, comparing post-retrieval composition only; (b) End-to-end—LDAR uses its own retriever vs. proposed method with Qwen3-Embedding-8B + composition, comparing paradigms.\n\n**Ablation studies:**\n1. Component isolation: (a) f without distraction (= relevance − redundancy), (b) f without redundancy (= relevance − distraction), (c) full f → marginal contribution of each penalty\n2. Hyperparameter sensitivity: β × λ grid (5×5), Pareto surface\n3. Algorithm comparison: AAMAS double-greedy vs. Buchbinder et al. randomized double-greedy vs. standard greedy vs. random\n4. DE scoring model: Qwen3-8B DE vs. Llama-4-Scout self-DE → cross-model transferability\n5. Per-passage DE vs. conditional DE_q(p|S\\{p}): set-conditional scoring benefit vs. cost\n6. Selection set size k: impact on f and downstream accuracy\n7. Joint optimization vs. two-stage pipeline: DE threshold τ ∈ {0.3, 0.5, 0.7} filter → AdaGReS greedy vs. full joint optimization\n8. Cross-generator validation: full comparison on NQ + ASQA with Qwen3-8B as generator, for proposed method + AdaGReS + DynamicRAG\n9. Candidate pool size: top-50 / top-100 / top-200 → sensitivity and DE cost scaling\n\n**Domain-shift evaluation:** Train/tune learned baselines (DynamicRAG, Context-Picker) on one benchmark distribution, evaluate on a different benchmark. Proposed method uses identical hyperparameters across all benchmarks without retuning.\n\n**Compute-normalized comparison:** Decompose costs into three stages: (1) retrieval + embedding (shared); (2) selection/composition (DE pre-computation, optimization algorithm, reranking); (3) generation (variable token count from different selections). Plot accuracy-vs-selection-cost and accuracy-vs-total-cost Pareto curves. Provide concrete wall-clock estimates for DE pre-computation (Qwen3-8B throughput on target hardware).\n\n**Cross-model DE calibration:** On validation subsets, compute DE using both Qwen3-8B and Llama-4-Scout, report Spearman/Pearson correlation.\n\n**γ measurement and analysis:** Compute γ per-query as the minimum diminishing-return ratio over all passage subsets. Report distribution statistics (mean, std, min, percentiles) per benchmark. Analyze correlation between per-query γ and accuracy improvement over monotone baselines. Specifically examine γ behavior in high-redundancy multi-hop scenarios (HotpotQA) vs. single-hop (NQ).\n\n**Bounded-embedding verification:** Report embedding norm distributions and pairwise similarity statistics for Qwen3-Embedding-8B on each benchmark corpus.\n\n**Statistical rigor:** 3-5 independent runs per configuration, mean ± std, paired bootstrap significance tests.\n\n## Key References\n\n- AdaGReS: Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG (arXiv Dec 2025)\n- The Distracting Effect: Understanding Irrelevant Passages in RAG (ACL 2025)\n- Stronger Approximation Guarantees for Non-Monotone γ-Weakly DR-Submodular Maximization (AAMAS 2026)\n- Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming (arXiv 2604.02554, Apr 2026)\n- Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding (ICLR 2026)\n- DynamicRAG: Leveraging Outputs of LLM as Feedback for Dynamic Reranking in RAG (NeurIPS 2025)\n- Context-Picker: Dynamic Context Selection Using Multi-stage Reinforcement Learning (arXiv Dec 2025)\n- AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop RAG (arXiv May 2026)\n- SMART-RAG: Selection using Determinantal Matrices for Augmented Retrieval (arXiv:2409.13992, Sep 2024)\n- ScalDPP: Scaling DPPs for RAG — Density Meets Diversity (arXiv:2604.03240, Apr 2026)\n- Vendi-RAG: Adaptively Trading-Off Diversity and Quality (arXiv:2502.11228, Feb 2025)\n- Sub-CP: Submodular Context Partitioning for In-Context Learning (arXiv:2510.05130, Oct 2025)\n- Qian: Multi-objective Evolutionary Algorithms for Approximately Submodular Minus Modular (arXiv:1910.05492)\n- Buchbinder, Feldman, Naor, Schwartz: A Tight (1/2)-Approximation for Unconstrained Submodular Maximization (FOCS 2012)\n- ALCE: Enabling Large Language Models to Generate Text with Citations (Gao et al., EMNLP 2023)"
}
```

---

### Runtime record

_source line 2 · 2026-05-30T07:21:41.365Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T07:21:41.365Z",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0"
}
```

---

## Round 1

46 recorded events

### User

_source line 3 · 2026-05-30T07:21:41.389Z_

# Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition

## Core Problem

How can post-retrieval context composition for RAG be formalized as a constrained non-monotone submodular optimization problem that provably distinguishes between redundancy (intra-set semantic overlap) and distraction (answer-conditional interference) as separate penalty terms, yielding greedy approximation guarantees even when adding passages can decrease generation quality?

## Broader Motivation

The problem of "when does adding more information provably hurt?" arises across context engineering: in-context learning (where Sub-CP, arXiv:2510.05130, applies submodular optimization to exemplar partitioning), tool-use composition, and multi-document grounding all exhibit non-monotone returns to context size. This work instantiates the question in RAG post-retrieval composition—including both single-hop and multi-hop QA—where it is most acute and empirically measurable, providing the first framework that decomposes the harm into redundancy and distraction with provable optimization guarantees.

## Research Opportunity

Three independently developed building blocks have converged but never been combined: (1) AdaGReS (arXiv Dec 2025) proved ε-approximate submodularity for redundancy-penalized context selection but only handles monotone objectives; (2) The Distracting Effect (ACL 2025) provides a concrete per-passage distraction measure DE_q(p) = 1−P(NO-RESPONSE|q,p) but performs no set-level optimization; (3) the AAMAS 2026 γ-weakly DR-submodular paper provides approximation guarantees Φ_γ for non-monotone objectives but has zero empirical applications to NLP.

The critical insight: subtracting a modular distraction penalty from AdaGReS's ε-approximately submodular objective makes the combined function non-monotone and non-submodular. The general problem class of maximizing "approximately submodular minus modular" functions has been studied theoretically (Qian, arXiv:1910.05492; Buchbinder et al., FOCS 2012 for the exact submodular case), but has never been instantiated in NLP or RAG. This work provides the first such instantiation, deriving the specific γ-weak DR-submodularity parameter for the RAG distraction-redundancy objective and empirically validating the AAMAS double-greedy framework in this domain.

## Why Decompose Redundancy and Distraction?

Redundancy and distraction damage generation quality through fundamentally different causal mechanisms, necessitating independent modeling:

**Redundancy is an opportunity cost.** Repeated information wastes token budget, displacing other useful passages. Its harm is indirect—the model does not get confused by redundant content, but misses out on complementary evidence. Marginal harm diminishes: the n-th duplicate contributes less incremental information loss. This calls for a pairwise similarity penalty with diminishing marginal structure.

**Distraction is an interference cost.** Irrelevant-but-plausible passages actively mislead the LLM's attention and reasoning, producing incorrect answers even when the gold passage is present. Its harm is direct and may compound: multiple distracting passages can reinforce a misleading narrative. This calls for a per-passage penalty tied to answer-conditional interference (DE_q).

Because these mechanisms have different scaling behavior and different causal pathways, a single penalty term cannot optimally control both. The decomposition into separate β (redundancy) and λ (distraction) hyperparameters allows independent calibration of each failure mode.

## Research Landscape

Current SOTA splits into two disjoint camps with a verified gap.

**Camp 1 (formal guarantees, distraction-blind):** AdaGReS achieves ε-approximate submodularity with adaptive β* but only models redundancy, evaluated on 2 benchmarks. CCBQP (arXiv 2604.02554, Apr 2026) provides Frank-Wolfe with O(nd) iterations and landscape analysis via diagonal loading λ≥2, dominating MMR and DPP on the relevance-diversity Pareto frontier (QAMPARI/ASQA), but handles only relevance-diversity with no distraction term. Note that CCBQP's relevance weighting does not substitute for explicit distraction modeling: as shown in The Distracting Effect (ACL 2025), high-DE passages are often topically related to the query (moderate-to-high relevance) but answer-misleading—relevance-based weighting cannot distinguish these from genuinely helpful passages. SMART-RAG (arXiv:2409.13992, Sep 2024) uses DPP to jointly model relevance, diversity, and conflict (inter-passage contradiction), training-free, but "conflict" captures contradictory information between passages, not answer-conditional interference from individually misleading content. ScalDPP (arXiv:2604.03240, Apr 2026) scales DPP via P-Adapter with Diverse Margin Loss but remains in the relevance-diversity paradigm and requires training the P-Adapter.

**Camp 2 (distraction-aware, no formal guarantees):** LDAR (ICLR 2026) is a distraction-aware retriever operating at retrieval time across 6 benchmarks but provides no post-retrieval composition or approximation bounds. DynamicRAG (NeurIPS 2025) uses RL with LLM feedback across 7 benchmarks but offers no optimization guarantees. Context-Picker (arXiv Dec 2025) uses two-stage RL for context selection across 5 benchmarks. Vendi-RAG (arXiv:2502.11228, Feb 2025) uses Vendi Score diversity + LLM judge for iterative diversity-quality optimization on multi-hop QA, but provides no formal guarantees and does not explicitly decompose redundancy from distraction. All learned approaches are distribution-dependent with no formal generalization guarantees under domain shift.

**The gap:** No existing method is simultaneously post-retrieval, formally grounded with provable approximation bounds, and distraction-aware.

## Addressing the Trivial Alternative

A natural two-stage pipeline—first filter high-DE passages via threshold, then run AdaGReS's monotone greedy on survivors—appears to achieve both distraction-awareness and formal guarantees without new theory. Joint optimization is necessary because:

**Pre-filtering forfeits optimality guarantees.** Removing passages before optimization shrinks the feasible set in a data-dependent, non-principled way. The resulting solution has no approximation guarantee relative to the optimal subset of the full candidate set. The joint formulation preserves the full candidate set and provides Φ_γ guarantees over it. A passage with high individual DE_q may still be the optimal choice when its relevance contribution outweighs the distraction cost in the joint objective—threshold filtering irrecoverably discards such passages.

As an empirical hypothesis, we additionally test whether set-level distraction interaction matters: the ablation includes a conditional DE_q(p|S\{p}) variant to evaluate whether set-conditioned distraction scoring provides benefit beyond modular DE. The two-stage pipeline itself is included as an explicit ablation baseline (Ablation 7).

## Proposed Approach

Define the set objective:

f(S) = Σ_{p∈S} rel(q,p) − β·Σ_{p,p'∈S} sim(p,p') − λ·Σ_{p∈S} DE_q(p)

where rel(q,p) is query-passage relevance (embedding cosine similarity), sim(p,p') is pairwise passage similarity (redundancy), and DE_q(p) is the per-passage Distracting Effect score (ACL 2025) computed via LLM no-response probability.

**Why non-monotone:** The distraction penalty Σ DE_q(p) grows linearly with |S|. Beyond a critical set size, accumulated distraction cost overwhelms relevance gains, making f decrease with added passages. This non-monotonicity invalidates standard monotone greedy guarantees (AdaGReS).

**Computational advantage of modular DE:** Since DE_q(p) depends only on the (q,p) pair, all DE scores can be pre-computed and cached before the greedy optimization begins. The DE computation cost is O(n) LLM calls (one per candidate passage), amortized across the optimization.

**Theoretical contribution:** The relevance − redundancy component inherits AdaGReS's ε-approximate submodularity. Subtracting the modular distraction term yields a non-monotone, non-submodular function in the "approximately submodular minus modular" problem class (cf. Qian, arXiv:1910.05492). Our specific contribution is deriving the γ-weak DR-submodularity parameter for this RAG-specific objective under bounded-embedding conditions, enabling the AAMAS 2026 double-greedy framework with Φ_γ > γe^{−γ} approximation guarantee.

The bounded-embedding conditions require: (a) embedding norms bounded in [c_min, c_max] with c_min > 0; (b) the diminishing-return ratio of the relevance-redundancy component lower-bounded by γ > 0, which depends on the ratio c_min/c_max and the maximum pairwise similarity in the candidate set. When the candidate pool contains near-duplicate passages (sim ≈ 1), γ may degrade; we empirically measure γ on each benchmark and discuss graceful degradation.

**γ as a diagnostic of composition difficulty.** Beyond its role as an algorithm parameter, γ encodes a structural property of the retrieval pool: it characterizes the gap between monotone greedy and non-monotone optimization for a given query's candidate set. When γ ≈ 1 (semantically diverse, low-redundancy pool), monotone greedy suffices and non-monotone optimization offers marginal gains. When γ ≪ 1 (high redundancy, high distraction), non-monotone optimization becomes essential. We empirically validate this by analyzing the correlation between per-query γ values and the accuracy improvement of our method over monotone baselines, establishing γ as a practical diagnostic for when sophisticated context composition is worthwhile.

**Comparison with classical algorithms:** For exact non-monotone submodular functions, Buchbinder et al. (FOCS 2012) provide a 1/2-approximation via randomized double-greedy, tighter than AAMAS's Φ_γ when γ ≈ 1. Our empirically measured γ determines which framework is more appropriate. Both algorithms are included in the experimental comparison.

## Experimental Design

**Benchmarks:** Natural Questions (NQ), ASQA, QAMPARI, HotpotQA.

**Metrics per benchmark:**
- NQ: Exact Match (EM), token-level F1
- ASQA: ROUGE-L, Disambig-F1 (D-F1), citation precision/recall (ALCE framework)
- QAMPARI: Entity-level F1, entity recall
- HotpotQA: EM, F1, supporting fact precision/recall
- Cross-benchmark: tokens per query, wall-clock latency per query, redundancy ratio

**Models:** Qwen3-Embedding-8B (retrieval + similarity), Qwen3-8B (DE scoring + secondary generator), Llama-4-Scout (primary generator).

**Baselines (three groups):**
- Simple heuristic: top-k, MMR
- Formal optimization: AdaGReS, CCBQP, SMART-RAG
- Learned: DynamicRAG, LDAR, Context-Picker, Vendi-RAG

**LDAR comparison protocol:** Two settings: (a) Retrieval-controlled—all methods use Qwen3-Embedding-8B top-N candidates, comparing post-retrieval composition only; (b) End-to-end—LDAR uses its own retriever vs. proposed method with Qwen3-Embedding-8B + composition, comparing paradigms.

**Ablation studies:**
1. Component isolation: (a) f without distraction (= relevance − redundancy), (b) f without redundancy (= relevance − distraction), (c) full f → marginal contribution of each penalty
2. Hyperparameter sensitivity: β × λ grid (5×5), Pareto surface
3. Algorithm comparison: AAMAS double-greedy vs. Buchbinder et al. randomized double-greedy vs. standard greedy vs. random
4. DE scoring model: Qwen3-8B DE vs. Llama-4-Scout self-DE → cross-model transferability
5. Per-passage DE vs. conditional DE_q(p|S\{p}): set-conditional scoring benefit vs. cost
6. Selection set size k: impact on f and downstream accuracy
7. Joint optimization vs. two-stage pipeline: DE threshold τ ∈ {0.3, 0.5, 0.7} filter → AdaGReS greedy vs. full joint optimization
8. Cross-generator validation: full comparison on NQ + ASQA with Qwen3-8B as generator, for proposed method + AdaGReS + DynamicRAG
9. Candidate pool size: top-50 / top-100 / top-200 → sensitivity and DE cost scaling

**Domain-shift evaluation:** Train/tune learned baselines (DynamicRAG, Context-Picker) on one benchmark distribution, evaluate on a different benchmark. Proposed method uses identical hyperparameters across all benchmarks without retuning.

**Compute-normalized comparison:** Decompose costs into three stages: (1) retrieval + embedding (shared); (2) selection/composition (DE pre-computation, optimization algorithm, reranking); (3) generation (variable token count from different selections). Plot accuracy-vs-selection-cost and accuracy-vs-total-cost Pareto curves. Provide concrete wall-clock estimates for DE pre-computation (Qwen3-8B throughput on target hardware).

**Cross-model DE calibration:** On validation subsets, compute DE using both Qwen3-8B and Llama-4-Scout, report Spearman/Pearson correlation.

**γ measurement and analysis:** Compute γ per-query as the minimum diminishing-return ratio over all passage subsets. Report distribution statistics (mean, std, min, percentiles) per benchmark. Analyze correlation between per-query γ and accuracy improvement over monotone baselines. Specifically examine γ behavior in high-redundancy multi-hop scenarios (HotpotQA) vs. single-hop (NQ).

**Bounded-embedding verification:** Report embedding norm distributions and pairwise similarity statistics for Qwen3-Embedding-8B on each benchmark corpus.

**Statistical rigor:** 3-5 independent runs per configuration, mean ± std, paired bootstrap significance tests.

## Key References

- AdaGReS: Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG (arXiv Dec 2025)
- The Distracting Effect: Understanding Irrelevant Passages in RAG (ACL 2025)
- Stronger Approximation Guarantees for Non-Monotone γ-Weakly DR-Submodular Maximization (AAMAS 2026)
- Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming (arXiv 2604.02554, Apr 2026)
- Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding (ICLR 2026)
- DynamicRAG: Leveraging Outputs of LLM as Feedback for Dynamic Reranking in RAG (NeurIPS 2025)
- Context-Picker: Dynamic Context Selection Using Multi-stage Reinforcement Learning (arXiv Dec 2025)
- AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop RAG (arXiv May 2026)
- SMART-RAG: Selection using Determinantal Matrices for Augmented Retrieval (arXiv:2409.13992, Sep 2024)
- ScalDPP: Scaling DPPs for RAG — Density Meets Diversity (arXiv:2604.03240, Apr 2026)
- Vendi-RAG: Adaptively Trading-Off Diversity and Quality (arXiv:2502.11228, Feb 2025)
- Sub-CP: Submodular Context Partitioning for In-Context Learning (arXiv:2510.05130, Oct 2025)
- Qian: Multi-objective Evolutionary Algorithms for Approximately Submodular Minus Modular (arXiv:1910.05492)
- Buchbinder, Feldman, Naor, Schwartz: A Tight (1/2)-Approximation for Unconstrained Submodular Maximization (FOCS 2012)
- ALCE: Enabling Large Language Models to Generate Text with Citations (Gao et al., EMNLP 2023)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "56213f29-1a0f-4729-bde9-d7c8e301fb24",
  "type": "user",
  "uuid": "2a2578f3-43f5-4b7c-998e-8e540737e330",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T07:21:41.388Z_

```json
{
  "parentUuid": "2a2578f3-43f5-4b7c-998e-8e540737e330",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
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
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
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
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "41afe73c-d18d-4021-826f-9d76b03f5f67",
  "timestamp": "2026-05-30T07:21:41.388Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T07:21:41.388Z_

```json
{
  "parentUuid": "41afe73c-d18d-4021-826f-9d76b03f5f67",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3ac3335c-75d8-4dcb-9fa9-bbf0b13ad478",
  "timestamp": "2026-05-30T07:21:41.388Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition  ## Core Problem  How can post-retrieval context composition for RAG be formalized as a constrained non-monotone…",
  "leafUuid": "3ac3335c-75d8-4dcb-9fa9-bbf0b13ad478",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Non-monotone submodular context composition for RAG",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0"
}
```

---

### Assistant

_source line 8 · 2026-05-30T07:21:51.054Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully read and analyze this proposal before doing any web searches. The proposal is about formalizing post-retrieval context composition for RAG as a constrained non-monotone submodular optimization problem that decomposes penalties into redundancy and distraction terms.

Let me first understand the core contributions:
1. Combining three independently developed building blocks: AdaGReS (submodular redundancy), Distracting Effect (per-passage distraction measure), and AAMAS 2026 γ-weakly DR-submodular guarantees
2. Deriving γ-weak DR-submodularity for the specific RAG objective


3. Validating the double-greedy framework empirically

Now I need to investigate whether the distraction-aware scoring combined with formal optimization guarantees is truly novel, if anyone else has explored this decomposition of redundancy versus distraction, and whether there are recent works that could challenge the novelty claims.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ac3335c-75d8-4dcb-9fa9-bbf0b13ad478",
  "isSidechain": false,
  "requestId": "req_011CbYMG89UGpWtRorNZAD99",
  "type": "assistant",
  "uuid": "98e82775-ff10-474d-b69d-14774189a5e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VJx6uJj76kafUQW74mCDux",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5458,
      "cache_read_input_tokens": 14184,
      "output_tokens": 385,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5458,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 385,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 5458,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5458
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

_source line 9 · 2026-05-30T07:21:51.553Z_

I need to do thorough front-end research before evaluating this proposal. Let me start by searching for the most relevant recent works and checking the novelty claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98e82775-ff10-474d-b69d-14774189a5e0",
  "isSidechain": false,
  "requestId": "req_011CbYMG89UGpWtRorNZAD99",
  "type": "assistant",
  "uuid": "9d6a5cc6-57e5-4fd6-a592-f155c3d2744e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VJx6uJj76kafUQW74mCDux",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5458,
      "cache_read_input_tokens": 14184,
      "output_tokens": 385,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5458,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 385,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 5458,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5458
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

_source line 10 · 2026-05-30T07:21:51.727Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SwuuBsbJxD8L7WMA7Loyij`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d6a5cc6-57e5-4fd6-a592-f155c3d2744e",
  "isSidechain": false,
  "requestId": "req_011CbYMG89UGpWtRorNZAD99",
  "type": "assistant",
  "uuid": "21f0b05d-8432-4d0b-8c14-e7da200c706f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VJx6uJj76kafUQW74mCDux",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5458,
      "cache_read_input_tokens": 14184,
      "output_tokens": 385,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5458,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 385,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 5458,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5458
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

_source line 11 · 2026-05-30T07:21:51.734Z_

<details><summary>↩ Tool result · `toolu_01SwuuBsbJxD8L7WMA7Loyij`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21f0b05d-8432-4d0b-8c14-e7da200c706f",
  "isSidechain": false,
  "promptId": "56213f29-1a0f-4729-bde9-d7c8e301fb24",
  "type": "user",
  "uuid": "4df56b4c-a2c3-493e-8c23-516661ac1dec",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "21f0b05d-8432-4d0b-8c14-e7da200c706f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-30T07:21:54.927Z_

Now let me conduct my front-end research with multiple targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4df56b4c-a2c3-493e-8c23-516661ac1dec",
  "isSidechain": false,
  "requestId": "req_011CbYMGtUEAJRxikwnrZzqx",
  "type": "assistant",
  "uuid": "dee78652-2002-48c4-a949-81e14b47a47a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017QskyVHoNDWMESgPmW8YFx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 913,
      "cache_read_input_tokens": 19642,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 913,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 85,
          "cache_read_input_tokens": 19642,
          "cache_creation_input_tokens": 913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 913
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

_source line 13 · 2026-05-30T07:21:55.197Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TjsxtnhYNMoa4mMFJWoSmN`</summary>

```json
{
  "query": "submodular optimization RAG context selection post-retrieval 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dee78652-2002-48c4-a949-81e14b47a47a",
  "isSidechain": false,
  "requestId": "req_011CbYMGtUEAJRxikwnrZzqx",
  "type": "assistant",
  "uuid": "0a4aaeb6-f8b3-4885-964a-ba843dbaff6a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017QskyVHoNDWMESgPmW8YFx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 913,
      "cache_read_input_tokens": 19642,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 913,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 85,
          "cache_read_input_tokens": 19642,
          "cache_creation_input_tokens": 913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 913
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

_source line 14 · 2026-05-30T07:22:03.596Z_

<details><summary>↩ Tool result · `toolu_01TjsxtnhYNMoa4mMFJWoSmN`</summary>

```text
Web search results for query: "submodular optimization RAG context selection post-retrieval 2025 2026"

Links: [{"title":"AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG","url":"https://arxiv.org/pdf/2512.25052"},{"title":"Submodular Optimization for Text Selection, Passage Reranking & Context Engineering","url":"https://jina.ai/news/submodular-optimization-for-text-selection-passage-reranking-context-engineering/"},{"title":"SMART-RAG: Selection using Determinantal Matrices for Augmented   Retrieval","url":"https://arxiv.org/pdf/2409.13992"},{"title":"From RAG to Context - A 2025 year-end review of RAG | RAGFlow","url":"https://ragflow.io/blog/rag-review-2025-from-rag-to-context"},{"title":"Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating Distractors and Positional Bias","url":"https://arxiv.org/pdf/2512.14313"},{"title":"Cluster-based Adaptive Retrieval: Dynamic Context Selection for RAG Applications","url":"https://arxiv.org/pdf/2511.14769"},{"title":"Rethinking Retrieval-Augmentation as Synthesis: A Query-Aware Context Merging Approach","url":"https://arxiv.org/pdf/2603.20286"}]

I've found several highly relevant research papers and resources on submodular optimization for RAG context selection. Here's what the search reveals:

## Key Recent Research (2025-2026)

**AdaGReS: Adaptive Greedy Context Selection** (December 2025)
The proposed approach provides theoretical analysis showing approximate submodularity under practical embedding similarity conditions, yielding near-optimality guarantees for greedy selection. This addresses redundancy control and context quality in question answering and biomedical corpora.

**SMART-RAG: Selection using Determinantal Matrices** (September 2024)
SMART is an unsupervised, training-free framework that leverages Determinantal Point Processes (DPPs) to simultaneously model relevance, diversity and conflict for context selection in RAG.

**Submodular Optimization in Context Engineering** (July 2025)
The lazy greedy algorithm is used to solve submodular optimization problems, achieving a (1 - 1/e) ≈ 0.632 approximation guarantee for monotone submodular functions. Text selection and passage reranking are integral components of context engineering in knowledge base selection and context compression.

**Dynamic Context Selection** (2025)
Recent work introduces classifiers that predict the optimal number of contexts to retrieve, dynamically adapting context length to specific query requirements in RAG systems.

The research indicates that submodular optimization is now a central technique for addressing redundancy and improving context quality in post-retrieval processing for RAG systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a4aaeb6-f8b3-4885-964a-ba843dbaff6a",
  "isSidechain": false,
  "promptId": "56213f29-1a0f-4729-bde9-d7c8e301fb24",
  "type": "user",
  "uuid": "f1fc0c86-97ff-489d-b2cf-0921b6c46f71",
  "toolUseResult": {
    "query": "submodular optimization RAG context selection post-retrieval 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JBVh5LcYbXzKcN3z4uWtUT",
        "content": [
          {
            "title": "AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG",
            "url": "https://arxiv.org/pdf/2512.25052"
          },
          {
            "title": "Submodular Optimization for Text Selection, Passage Reranking & Context Engineering",
            "url": "https://jina.ai/news/submodular-optimization-for-text-selection-passage-reranking-context-engineering/"
          },
          {
            "title": "SMART-RAG: Selection using Determinantal Matrices for Augmented   Retrieval",
            "url": "https://arxiv.org/pdf/2409.13992"
          },
          {
            "title": "From RAG to Context - A 2025 year-end review of RAG | RAGFlow",
            "url": "https://ragflow.io/blog/rag-review-2025-from-rag-to-context"
          },
          {
            "title": "Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating Distractors and Positional Bias",
            "url": "https://arxiv.org/pdf/2512.14313"
          },
          {
            "title": "Cluster-based Adaptive Retrieval: Dynamic Context Selection for RAG Applications",
            "url": "https://arxiv.org/pdf/2511.14769"
          },
          {
            "title": "Rethinking Retrieval-Augmentation as Synthesis: A Query-Aware Context Merging Approach",
            "url": "https://arxiv.org/pdf/2603.20286"
          }
        ]
      },
      "I've found several highly relevant research papers and resources on submodular optimization for RAG context selection. Here's what the search reveals:\n\n## Key Recent Research (2025-2026)\n\n**AdaGReS: Adaptive Greedy Context Selection** (December 2025)\nThe proposed approach provides theoretical analysis showing approximate submodularity under practical embedding similarity conditions, yielding near-optimality guarantees for greedy selection. This addresses redundancy control and context quality in question answering and biomedical corpora.\n\n**SMART-RAG: Selection using Determinantal Matrices** (September 2024)\nSMART is an unsupervised, training-free framework that leverages Determinantal Point Processes (DPPs) to simultaneously model relevance, diversity and conflict for context selection in RAG.\n\n**Submodular Optimization in Context Engineering** (July 2025)\nThe lazy greedy algorithm is used to solve submodular optimization problems, achieving a (1 - 1/e) ≈ 0.632 approximation guarantee for monotone submodular functions. Text selection and passage reranking are integral components of context engineering in knowledge base selection and context compression.\n\n**Dynamic Context Selection** (2025)\nRecent work introduces classifiers that predict the optimal number of contexts to retrieve, dynamically adapting context length to specific query requirements in RAG systems.\n\nThe research indicates that submodular optimization is now a central technique for addressing redundancy and improving context quality in post-retrieval processing for RAG systems."
    ],
    "durationSeconds": 8.392522058,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0a4aaeb6-f8b3-4885-964a-ba843dbaff6a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-30T07:22:06.997Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DcJXZNW2zni3C8YDizaaGd`</summary>

```json
{
  "query": "distracting effect irrelevant passages RAG distraction-aware retrieval 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1fc0c86-97ff-489d-b2cf-0921b6c46f71",
  "isSidechain": false,
  "requestId": "req_011CbYMHky4FtDZKPygVv3yD",
  "type": "assistant",
  "uuid": "e61e8449-1fe4-4f47-a6c3-9f498c4f9d11",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WU4A3cJQvCYRgVyPJrLTfg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 828,
      "cache_read_input_tokens": 20555,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 828,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 20555,
          "cache_creation_input_tokens": 828,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 828
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

_source line 16 · 2026-05-30T07:22:14.261Z_

<details><summary>↩ Tool result · `toolu_01DcJXZNW2zni3C8YDizaaGd`</summary>

```text
Web search results for query: "distracting effect irrelevant passages RAG distraction-aware retrieval 2025 2026"

Links: [{"title":"The Distracting Effect: Understanding Irrelevant Passages in RAG","url":"https://arxiv.org/pdf/2505.06914"},{"title":"The Distracting Effect: Understanding Irrelevant Passages in RAG - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.892/"},{"title":"[2505.06914] The Distracting Effect: Understanding Irrelevant Passages in RAG","url":"https://arxiv.org/abs/2505.06914"},{"title":"The Distracting Effect: Understanding Irrelevant Passages in RAG","url":"https://arxiv.org/html/2505.06914v1"},{"title":"Paper page - The Distracting Effect: Understanding Irrelevant Passages in RAG","url":"https://huggingface.co/papers/2505.06914"},{"title":"The Distracting Effect: Understanding Irrelevant Passages ...","url":"https://aclanthology.org/2025.acl-long.892.pdf"}]

I've found relevant search results for your query. Here's what the search revealed:

A well-known issue with Retrieval Augmented Generation (RAG) is that retrieved passages that are irrelevant to the query sometimes distract the answer-generating LLM, causing it to provide an incorrect response.

The primary research paper on this topic is titled "The Distracting Effect: Understanding Irrelevant Passages in RAG" by Amiraz, Cuconasu, Filice, and Karnin. It was published in Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) in July 2025, in Vienna, Austria.

Key findings from this research include:

- The researchers move beyond the simple binary classification of irrelevant passages as either completely unrelated vs. distracting, and develop and analyze multiple methods for finding hard distracting passages.

- By fine-tuning LLMs with carefully selected distracting passages, they achieve up to a 7.5% increase in answering accuracy compared to counterparts fine-tuned on conventional RAG datasets.

- They provide a quantifiable measure of the distracting effect of a passage and demonstrate its robustness across LLMs.

The research addresses how to evaluate and mitigate the negative effects of distracting passages in RAG systems, which is an important practical problem for improving LLM performance on knowledge-intensive tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e61e8449-1fe4-4f47-a6c3-9f498c4f9d11",
  "isSidechain": false,
  "promptId": "56213f29-1a0f-4729-bde9-d7c8e301fb24",
  "type": "user",
  "uuid": "5945e91b-d04a-404b-b24c-989533d83b97",
  "toolUseResult": {
    "query": "distracting effect irrelevant passages RAG distraction-aware retrieval 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013JHmSVM71KAu4KtVZ4HXEk",
        "content": [
          {
            "title": "The Distracting Effect: Understanding Irrelevant Passages in RAG",
            "url": "https://arxiv.org/pdf/2505.06914"
          },
          {
            "title": "The Distracting Effect: Understanding Irrelevant Passages in RAG - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.892/"
          },
          {
            "title": "[2505.06914] The Distracting Effect: Understanding Irrelevant Passages in RAG",
            "url": "https://arxiv.org/abs/2505.06914"
          },
          {
            "title": "The Distracting Effect: Understanding Irrelevant Passages in RAG",
            "url": "https://arxiv.org/html/2505.06914v1"
          },
          {
            "title": "Paper page - The Distracting Effect: Understanding Irrelevant Passages in RAG",
            "url": "https://huggingface.co/papers/2505.06914"
          },
          {
            "title": "The Distracting Effect: Understanding Irrelevant Passages ...",
            "url": "https://aclanthology.org/2025.acl-long.892.pdf"
          }
        ]
      },
      "I've found relevant search results for your query. Here's what the search revealed:\n\nA well-known issue with Retrieval Augmented Generation (RAG) is that retrieved passages that are irrelevant to the query sometimes distract the answer-generating LLM, causing it to provide an incorrect response.\n\nThe primary research paper on this topic is titled \"The Distracting Effect: Understanding Irrelevant Passages in RAG\" by Amiraz, Cuconasu, Filice, and Karnin. It was published in Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) in July 2025, in Vienna, Austria.\n\nKey findings from this research include:\n\n- The researchers move beyond the simple binary classification of irrelevant passages as either completely unrelated vs. distracting, and develop and analyze multiple methods for finding hard distracting passages.\n\n- By fine-tuning LLMs with carefully selected distracting passages, they achieve up to a 7.5% increase in answering accuracy compared to counterparts fine-tuned on conventional RAG datasets.\n\n- They provide a quantifiable measure of the distracting effect of a passage and demonstrate its robustness across LLMs.\n\nThe research addresses how to evaluate and mitigate the negative effects of distracting passages in RAG systems, which is an important practical problem for improving LLM performance on knowledge-intensive tasks."
    ],
    "durationSeconds": 7.258348243,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e61e8449-1fe4-4f47-a6c3-9f498c4f9d11",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-30T07:22:18.604Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BuDnjSWwrwncyrn4bNvu8h`</summary>

```json
{
  "query": "non-monotone submodular maximization DR-submodular approximation guarantee 2025 2026 AAMAS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5945e91b-d04a-404b-b24c-989533d83b97",
  "isSidechain": false,
  "requestId": "req_011CbYMJZ118ZLga1bDMhP5N",
  "type": "assistant",
  "uuid": "5c6ffc04-febb-4040-a89f-3e119953be56",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013pr7SeRjtsU6ZaJ4gXjVm5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 719,
      "cache_read_input_tokens": 21383,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 719,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 21383,
          "cache_creation_input_tokens": 719,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 719
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

_source line 18 · 2026-05-30T07:22:25.798Z_

<details><summary>↩ Tool result · `toolu_01BuDnjSWwrwncyrn4bNvu8h`</summary>

```text
Web search results for query: "non-monotone submodular maximization DR-submodular approximation guarantee 2025 2026 AAMAS"

Links: [{"title":"Stronger Approximation Guarantees for Non-Monotone 𝛾-Weakly DR-Submodular Maximization","url":"https://arxiv.org/html/2601.00611"},{"title":"Stronger Approximation Guarantees for Non-Monotone γ-Weakly","url":"https://arxiv.org/pdf/2601.00611"},{"title":"[2601.00611] Stronger Approximation Guarantees for Non-Monotone γ-Weakly DR-Submodular Maximization","url":"https://arxiv.org/abs/2601.00611"},{"title":"Non-monotone DR-submodular Maximization: Approximation and Regret   Guarantees","url":"https://arxiv.org/pdf/1905.09595"},{"title":"Fast approximation algorithm for non-monotone DR-submodular maximization under size constraint | Journal of Combinatorial Optimization | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10878-025-01374-4"},{"title":"Online Non-Monotone DR-Submodular Maximization | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/17186"},{"title":"[1905.09595] Non-monotone DR-submodular Maximization: Approximation and Regret Guarantees","url":"https://arxiv.org/abs/1905.09595"}]

Based on the search results, here's what I found relevant to your query:

## Recent Work on Non-Monotone DR-Submodular Maximization (2025-2026)

A paper titled "Stronger Approximation Guarantees for Non-Monotone γ-Weakly DR-Submodular Maximization" will be presented in part at the International Conference on Autonomous Agents and Multiagent Systems (AAMAS) in May 2026. 

This work studies the maximization of a nonnegative, non-monotone γ-weakly DR-submodular function over a down-closed convex body. The main result is an approximation algorithm whose guarantee depends smoothly on γ; in particular, when γ=1 (the DR-submodular case) the bound recovers the 0.401 approximation factor.

The approach combines a Frank–Wolfe–guided continuous-greedy framework with a γ-aware double-greedy step, yielding a simple yet effective procedure for handling non-monotonicity.

## Related Recent Work (December 2025)

Additionally, a recent study on non-monotone DR-submodular maximization over a ground set subject to a size constraint proposes algorithms named FastDrSub and FastDrSub+, where FastDrSub offers an approximation ratio of 0.044 and FastDrSub+ improves with a ratio of 1/4-ε.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c6ffc04-febb-4040-a89f-3e119953be56",
  "isSidechain": false,
  "promptId": "56213f29-1a0f-4729-bde9-d7c8e301fb24",
  "type": "user",
  "uuid": "df7b400f-1a44-4e07-81b2-a86b55ebe80c",
  "toolUseResult": {
    "query": "non-monotone submodular maximization DR-submodular approximation guarantee 2025 2026 AAMAS",
    "results": [
      {
        "tool_use_id": "srvtoolu_01J7JA8ZAmP9eNMkNgfkrgSp",
        "content": [
          {
            "title": "Stronger Approximation Guarantees for Non-Monotone 𝛾-Weakly DR-Submodular Maximization",
            "url": "https://arxiv.org/html/2601.00611"
          },
          {
            "title": "Stronger Approximation Guarantees for Non-Monotone γ-Weakly",
            "url": "https://arxiv.org/pdf/2601.00611"
          },
          {
            "title": "[2601.00611] Stronger Approximation Guarantees for Non-Monotone γ-Weakly DR-Submodular Maximization",
            "url": "https://arxiv.org/abs/2601.00611"
          },
          {
            "title": "Non-monotone DR-submodular Maximization: Approximation and Regret   Guarantees",
            "url": "https://arxiv.org/pdf/1905.09595"
          },
          {
            "title": "Fast approximation algorithm for non-monotone DR-submodular maximization under size constraint | Journal of Combinatorial Optimization | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10878-025-01374-4"
          },
          {
            "title": "Online Non-Monotone DR-Submodular Maximization | Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/17186"
          },
          {
            "title": "[1905.09595] Non-monotone DR-submodular Maximization: Approximation and Regret Guarantees",
            "url": "https://arxiv.org/abs/1905.09595"
          }
        ]
      },
      "Based on the search results, here's what I found relevant to your query:\n\n## Recent Work on Non-Monotone DR-Submodular Maximization (2025-2026)\n\nA paper titled \"Stronger Approximation Guarantees for Non-Monotone γ-Weakly DR-Submodular Maximization\" will be presented in part at the International Conference on Autonomous Agents and Multiagent Systems (AAMAS) in May 2026. \n\nThis work studies the maximization of a nonnegative, non-monotone γ-weakly DR-submodular function over a down-closed convex body. The main result is an approximation algorithm whose guarantee depends smoothly on γ; in particular, when γ=1 (the DR-submodular case) the bound recovers the 0.401 approximation factor.\n\nThe approach combines a Frank–Wolfe–guided continuous-greedy framework with a γ-aware double-greedy step, yielding a simple yet effective procedure for handling non-monotonicity.\n\n## Related Recent Work (December 2025)\n\nAdditionally, a recent study on non-monotone DR-submodular maximization over a ground set subject to a size constraint proposes algorithms named FastDrSub and FastDrSub+, where FastDrSub offers an approximation ratio of 0.044 and FastDrSub+ improves with a ratio of 1/4-ε."
    ],
    "durationSeconds": 7.1892408459999935,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5c6ffc04-febb-4040-a89f-3e119953be56",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-30T07:22:29.129Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013hb6wKPDEsnEf7g51dcrJW`</summary>

```json
{
  "query": "CCBQP cardinality constrained binary quadratic programming retrieval diversity 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df7b400f-1a44-4e07-81b2-a86b55ebe80c",
  "isSidechain": false,
  "requestId": "req_011CbYMKPt6nEuRBjvoT7vZE",
  "type": "assistant",
  "uuid": "e7320294-1569-4ff9-b0de-e3e0018aadaf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EiZfJay3qGAdPyXrBhmLyQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 858,
      "cache_read_input_tokens": 22102,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 858,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 22102,
          "cache_creation_input_tokens": 858,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 858
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

_source line 20 · 2026-05-30T07:22:35.944Z_

<details><summary>↩ Tool result · `toolu_013hb6wKPDEsnEf7g51dcrJW`</summary>

```text
Web search results for query: "CCBQP cardinality constrained binary quadratic programming retrieval diversity 2026 arXiv"

Links: [{"title":"[2604.02554] Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming","url":"https://arxiv.org/abs/2604.02554"},{"title":"Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming","url":"https://arxiv.org/pdf/2604.02554"},{"title":"Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming","url":"https://arxiv.org/html/2604.02554"},{"title":"An Algorithm to Solve Cardinality Constrained Quadratic ...","url":"https://arxiv.org/pdf/2504.04043"},{"title":"[2504.04043] An Algorithm to Solve Cardinality Constrained Quadratic Optimization Problem with an Application to the Best Subset Selection in Regression","url":"https://arxiv.org/abs/2504.04043"}]

Based on the search results, I found a highly relevant paper matching your query:

**"Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming"** (arXiv:2604.02554)

This paper proposes a principled formulation of diversity retrieval as a cardinality-constrained binary quadratic programming (CCBQP), which explicitly balances relevance and semantic diversity through an interpretable trade-off parameter.

The paper was authored by Qiheng Lu and Nicholas D. Sidiropoulos from the University of Virginia. It was submitted on April 2, 2026.

Key aspects of the work include:

- The paper addresses diversity-aware retrieval which is essential for Retrieval-Augmented Generation (RAG), noting that existing methods lack theoretical guarantees and face scalability issues as the number of retrieved passages increases.

- The authors develop a non-convex tight continuous relaxation and a Frank–Wolfe based algorithm with landscape analysis and convergence guarantees.

- Extensive experiments demonstrate that their method consistently dominates baselines on the relevance-diversity Pareto frontier, while achieving significant speedup.

The paper is available on arXiv at: https://arxiv.org/abs/2604.02554


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7320294-1569-4ff9-b0de-e3e0018aadaf",
  "isSidechain": false,
  "promptId": "56213f29-1a0f-4729-bde9-d7c8e301fb24",
  "type": "user",
  "uuid": "78eb7af0-6e41-400f-8634-d0eeb3d9f06b",
  "toolUseResult": {
    "query": "CCBQP cardinality constrained binary quadratic programming retrieval diversity 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XcTJ4TVQXiSoVmnZ3R4XEu",
        "content": [
          {
            "title": "[2604.02554] Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming",
            "url": "https://arxiv.org/abs/2604.02554"
          },
          {
            "title": "Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming",
            "url": "https://arxiv.org/pdf/2604.02554"
          },
          {
            "title": "Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming",
            "url": "https://arxiv.org/html/2604.02554"
          },
          {
            "title": "An Algorithm to Solve Cardinality Constrained Quadratic ...",
            "url": "https://arxiv.org/pdf/2504.04043"
          },
          {
            "title": "[2504.04043] An Algorithm to Solve Cardinality Constrained Quadratic Optimization Problem with an Application to the Best Subset Selection in Regression",
            "url": "https://arxiv.org/abs/2504.04043"
          }
        ]
      },
      "Based on the search results, I found a highly relevant paper matching your query:\n\n**\"Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming\"** (arXiv:2604.02554)\n\nThis paper proposes a principled formulation of diversity retrieval as a cardinality-constrained binary quadratic programming (CCBQP), which explicitly balances relevance and semantic diversity through an interpretable trade-off parameter.\n\nThe paper was authored by Qiheng Lu and Nicholas D. Sidiropoulos from the University of Virginia. It was submitted on April 2, 2026.\n\nKey aspects of the work include:\n\n- The paper addresses diversity-aware retrieval which is essential for Retrieval-Augmented Generation (RAG), noting that existing methods lack theoretical guarantees and face scalability issues as the number of retrieved passages increases.\n\n- The authors develop a non-convex tight continuous relaxation and a Frank–Wolfe based algorithm with landscape analysis and convergence guarantees.\n\n- Extensive experiments demonstrate that their method consistently dominates baselines on the relevance-diversity Pareto frontier, while achieving significant speedup.\n\nThe paper is available on arXiv at: https://arxiv.org/abs/2604.02554"
    ],
    "durationSeconds": 6.809487857,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e7320294-1569-4ff9-b0de-e3e0018aadaf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
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
  "lastPrompt": "# Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition  ## Core Problem  How can post-retrieval context composition for RAG be formalized as a constrained non-monotone…",
  "leafUuid": "78eb7af0-6e41-400f-8634-d0eeb3d9f06b",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Non-monotone submodular context composition for RAG",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0"
}
```

---

### Tool call

_source line 23 · 2026-05-30T07:22:38.350Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011Vn5TuXnwakRBkAYoEVhyB`</summary>

```json
{
  "query": "\"redundancy\" \"distraction\" decomposition context selection RAG optimization 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78eb7af0-6e41-400f-8634-d0eeb3d9f06b",
  "isSidechain": false,
  "requestId": "req_011CbYML9EZrdziAxcc3XvHL",
  "type": "assistant",
  "uuid": "5c84d684-22f9-4a8c-9da8-792df7cc4caf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012a6svsTonkT4z6TrudRtAy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 691,
      "cache_read_input_tokens": 22960,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 691,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 22960,
          "cache_creation_input_tokens": 691,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 691
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

_source line 24 · 2026-05-30T07:22:45.167Z_

<details><summary>↩ Tool result · `toolu_011Vn5TuXnwakRBkAYoEVhyB`</summary>

```text
Web search results for query: ""redundancy" "distraction" decomposition context selection RAG optimization 2025 2026"

Links: [{"title":"AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG","url":"https://arxiv.org/pdf/2512.25052"},{"title":"Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating Distractors and Positional Bias","url":"https://arxiv.org/pdf/2512.14313"},{"title":"The 2025 Guide to Retrieval-Augmented Generation (RAG)","url":"https://www.edenai.co/post/the-2025-guide-to-retrieval-augmented-generation-rag"},{"title":"Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding","url":"https://arxiv.org/pdf/2509.21865"},{"title":"From RAG to Context - A 2025 year-end review of RAG | RAGFlow","url":"https://ragflow.io/blog/rag-review-2025-from-rag-to-context"},{"title":"RAG is DEAD!. Retrieval-Augmented Generation ruled… | by Reliable Data Engineering | Medium","url":"https://medium.com/@reliabledataengineering/rag-is-dead-and-why-thats-the-best-news-you-ll-hear-all-year-0f3de8c44604"},{"title":"Rethinking Retrieval-Augmentation as Synthesis: A Query-Aware Context Merging Approach","url":"https://arxiv.org/pdf/2603.20286"}]

I found several highly relevant research papers and articles on RAG optimization for 2025-2026. Here's what the search revealed:

## Key Research on RAG Optimization

Recent work on adaptive context selection includes AdaGReS, which provides theoretical analysis of redundancy-aware scoring and demonstrates improvements in redundancy control and context quality on question answering tasks.

Dynamic context selection approaches introduce classifiers that predict the optimal number of contexts to retrieve and dynamically adapt context length to specific query requirements, showing consistent improvements in generation.

## Addressing Distraction in RAG

Research demonstrates that both open and closed-source LLMs can fail to answer questions even when the relevant passage is retrieved, due to interference from distracting passages. When model capacity is limited, supplying full context may introduce distraction and degrade answer quality.

## Decomposition and Context Synthesis

The standard retrieve-then-select paradigm retains only top-k chunks by semantic similarity, but this approach suffers from information loss, fragmented context, and significant semantic redundancy as multiple high-ranking chunks may convey repetitive information.

## Industry Trends for 2025-2026

Newer approaches like CRAG break down retrieved documents into smaller components to focus on key insights while filtering out irrelevant or redundant details.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c84d684-22f9-4a8c-9da8-792df7cc4caf",
  "isSidechain": false,
  "promptId": "56213f29-1a0f-4729-bde9-d7c8e301fb24",
  "type": "user",
  "uuid": "6a5516e4-5a6e-4b35-b5a5-dbed902fac4b",
  "toolUseResult": {
    "query": "\"redundancy\" \"distraction\" decomposition context selection RAG optimization 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Qxn7UqGVHeBoCSuTNq3Pqn",
        "content": [
          {
            "title": "AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG",
            "url": "https://arxiv.org/pdf/2512.25052"
          },
          {
            "title": "Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating Distractors and Positional Bias",
            "url": "https://arxiv.org/pdf/2512.14313"
          },
          {
            "title": "The 2025 Guide to Retrieval-Augmented Generation (RAG)",
            "url": "https://www.edenai.co/post/the-2025-guide-to-retrieval-augmented-generation-rag"
          },
          {
            "title": "Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding",
            "url": "https://arxiv.org/pdf/2509.21865"
          },
          {
            "title": "From RAG to Context - A 2025 year-end review of RAG | RAGFlow",
            "url": "https://ragflow.io/blog/rag-review-2025-from-rag-to-context"
          },
          {
            "title": "RAG is DEAD!. Retrieval-Augmented Generation ruled… | by Reliable Data Engineering | Medium",
            "url": "https://medium.com/@reliabledataengineering/rag-is-dead-and-why-thats-the-best-news-you-ll-hear-all-year-0f3de8c44604"
          },
          {
            "title": "Rethinking Retrieval-Augmentation as Synthesis: A Query-Aware Context Merging Approach",
            "url": "https://arxiv.org/pdf/2603.20286"
          }
        ]
      },
      "I found several highly relevant research papers and articles on RAG optimization for 2025-2026. Here's what the search revealed:\n\n## Key Research on RAG Optimization\n\nRecent work on adaptive context selection includes AdaGReS, which provides theoretical analysis of redundancy-aware scoring and demonstrates improvements in redundancy control and context quality on question answering tasks.\n\nDynamic context selection approaches introduce classifiers that predict the optimal number of contexts to retrieve and dynamically adapt context length to specific query requirements, showing consistent improvements in generation.\n\n## Addressing Distraction in RAG\n\nResearch demonstrates that both open and closed-source LLMs can fail to answer questions even when the relevant passage is retrieved, due to interference from distracting passages. When model capacity is limited, supplying full context may introduce distraction and degrade answer quality.\n\n## Decomposition and Context Synthesis\n\nThe standard retrieve-then-select paradigm retains only top-k chunks by semantic similarity, but this approach suffers from information loss, fragmented context, and significant semantic redundancy as multiple high-ranking chunks may convey repetitive information.\n\n## Industry Trends for 2025-2026\n\nNewer approaches like CRAG break down retrieved documents into smaller components to focus on key insights while filtering out irrelevant or redundant details."
    ],
    "durationSeconds": 6.813142707999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5c84d684-22f9-4a8c-9da8-792df7cc4caf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-30T07:22:50.302Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EgJHVTkKsHMPFmKfc8VUcb`</summary>

```json
{
  "query": "DynamicRAG LDAR Context-Picker distraction-aware learned context selection NeurIPS ICLR 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a5516e4-5a6e-4b35-b5a5-dbed902fac4b",
  "isSidechain": false,
  "requestId": "req_011CbYMLpkrBYSmJixAJTbxS",
  "type": "assistant",
  "uuid": "f4ff74d0-2ab4-4b45-9990-77c2eba5f6bc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rHwfBp9pcGkDHGKEJFbbv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 23651,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 84,
          "cache_read_input_tokens": 23651,
          "cache_creation_input_tokens": 808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 808
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

_source line 26 · 2026-05-30T07:22:58.916Z_

<details><summary>↩ Tool result · `toolu_01EgJHVTkKsHMPFmKfc8VUcb`</summary>

```text
Web search results for query: "DynamicRAG LDAR Context-Picker distraction-aware learned context selection NeurIPS ICLR 2025 2026"

Links: [{"title":"Context-Picker: Dynamic context selection using multi-stage","url":"https://arxiv.org/pdf/2512.14465"},{"title":"Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding","url":"https://arxiv.org/html/2509.21865v2"},{"title":"Context-Picker: Dynamic Context Selection Using Multi-stage Reinforcement Learning","url":"https://arxiv.org/html/2512.14465"},{"title":"Preprint. BEYOND RAG VS. LONG-CONTEXT: LEARNING DISTRACTION-AWARE RETRIEVAL FOR","url":"https://arxiv.org/pdf/2509.21865"},{"title":"Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating Distractors and Positional Bias","url":"https://arxiv.org/html/2512.14313v1"},{"title":"Paper page - Context-Picker: Dynamic context selection using multi-stage reinforcement learning","url":"https://huggingface.co/papers/2512.14465"},{"title":"Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating Distractors and Positional Bias","url":"https://arxiv.org/pdf/2512.14313"},{"title":"[2512.14465] Context-Picker: Dynamic context selection using multi-stage reinforcement learning","url":"https://arxiv.org/abs/2512.14465"}]

Based on the search results, I found information about several related research works on context selection and retrieval-augmented generation:

## LDAR (Learning Distraction-Aware Retrieval)

LDAR (Learning Distraction-Aware Retrieval) is a retriever that learns to select passages to minimize potential interference from distracting passages in accordance with the capacity of the LLM, thereby achieving significantly better performance and lower token usage compared to long-context approaches. The approach demonstrates that retrieving passages in bands (selecting from contiguous ranges along the similarity-ranked list) is critical for learning a distraction-aware retrieval strategy, as the banded retrieval strategy provides a form of abstraction that improves generalization.

## Context-Picker

Context-Picker is a reasoning-aware framework that learns a variable-length evidence set under a token budget, combining an offline evidence mining pipeline that distills greedily minimal sufficient evidence sets via a generator–judge loop with Leave-One-Out (LOO) pruning, and a two-stage reinforcement learning schedule optimized with GRPO, where Stage I emphasizes coverage of reasoning chains and Stage II tightens redundancy penalties to prune distractors.

## DynamicRAG

DynamicRAG adaptively determines both the ranking and the number (k) of retrieved documents for each query, employing a dynamic reranker trained using reinforcement learning, where the quality of LLM-generated responses serves as the reward signal.

These papers represent recent advances in dynamic context selection for RAG systems, all focusing on addressing the challenge of distractors and optimizing context length in retrieval-augmented generation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4ff74d0-2ab4-4b45-9990-77c2eba5f6bc",
  "isSidechain": false,
  "promptId": "56213f29-1a0f-4729-bde9-d7c8e301fb24",
  "type": "user",
  "uuid": "e312d535-94d0-4489-a1dc-080708179fde",
  "toolUseResult": {
    "query": "DynamicRAG LDAR Context-Picker distraction-aware learned context selection NeurIPS ICLR 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GCvT8GasDqs1p6stZSJ6QZ",
        "content": [
          {
            "title": "Context-Picker: Dynamic context selection using multi-stage",
            "url": "https://arxiv.org/pdf/2512.14465"
          },
          {
            "title": "Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding",
            "url": "https://arxiv.org/html/2509.21865v2"
          },
          {
            "title": "Context-Picker: Dynamic Context Selection Using Multi-stage Reinforcement Learning",
            "url": "https://arxiv.org/html/2512.14465"
          },
          {
            "title": "Preprint. BEYOND RAG VS. LONG-CONTEXT: LEARNING DISTRACTION-AWARE RETRIEVAL FOR",
            "url": "https://arxiv.org/pdf/2509.21865"
          },
          {
            "title": "Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating Distractors and Positional Bias",
            "url": "https://arxiv.org/html/2512.14313v1"
          },
          {
            "title": "Paper page - Context-Picker: Dynamic context selection using multi-stage reinforcement learning",
            "url": "https://huggingface.co/papers/2512.14465"
          },
          {
            "title": "Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating Distractors and Positional Bias",
            "url": "https://arxiv.org/pdf/2512.14313"
          },
          {
            "title": "[2512.14465] Context-Picker: Dynamic context selection using multi-stage reinforcement learning",
            "url": "https://arxiv.org/abs/2512.14465"
          }
        ]
      },
      "Based on the search results, I found information about several related research works on context selection and retrieval-augmented generation:\n\n## LDAR (Learning Distraction-Aware Retrieval)\n\nLDAR (Learning Distraction-Aware Retrieval) is a retriever that learns to select passages to minimize potential interference from distracting passages in accordance with the capacity of the LLM, thereby achieving significantly better performance and lower token usage compared to long-context approaches. The approach demonstrates that retrieving passages in bands (selecting from contiguous ranges along the similarity-ranked list) is critical for learning a distraction-aware retrieval strategy, as the banded retrieval strategy provides a form of abstraction that improves generalization.\n\n## Context-Picker\n\nContext-Picker is a reasoning-aware framework that learns a variable-length evidence set under a token budget, combining an offline evidence mining pipeline that distills greedily minimal sufficient evidence sets via a generator–judge loop with Leave-One-Out (LOO) pruning, and a two-stage reinforcement learning schedule optimized with GRPO, where Stage I emphasizes coverage of reasoning chains and Stage II tightens redundancy penalties to prune distractors.\n\n## DynamicRAG\n\nDynamicRAG adaptively determines both the ranking and the number (k) of retrieved documents for each query, employing a dynamic reranker trained using reinforcement learning, where the quality of LLM-generated responses serves as the reward signal.\n\nThese papers represent recent advances in dynamic context selection for RAG systems, all focusing on addressing the challenge of distractors and optimizing context length in retrieval-augmented generation tasks."
    ],
    "durationSeconds": 8.608855263999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f4ff74d0-2ab4-4b45-9990-77c2eba5f6bc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-30T07:23:01.951Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XzFFJdQyZuLhT4esR2mty2`</summary>

```json
{
  "query": "approximately submodular minus modular optimization NLP application instantiation 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e312d535-94d0-4489-a1dc-080708179fde",
  "isSidechain": false,
  "requestId": "req_011CbYMMqTJ2NSxAx9U1CyMb",
  "type": "assistant",
  "uuid": "240cc65d-4539-441f-8df7-1ef5f4a227d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F33fnPurr997oDskViYFK1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 877,
      "cache_read_input_tokens": 24459,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 877,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 24459,
          "cache_creation_input_tokens": 877,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 877
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

_source line 28 · 2026-05-30T07:23:09.257Z_

<details><summary>↩ Tool result · `toolu_01XzFFJdQyZuLhT4esR2mty2`</summary>

```text
Web search results for query: "approximately submodular minus modular optimization NLP application instantiation 2024 2025 2026"

Links: [{"title":"Optimal Approximation for Submodular and Supermodular Optimization with Bounded Curvature | Mathematics of Operations Research","url":"https://pubsonline.informs.org/doi/abs/10.1287/moor.2016.0842"},{"title":"Multiobjective Evolutionary Algorithms Are Still Good: Maximizing Monotone Approximately Submodular Minus Modular Functions | MIT Press Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/9655642"},{"title":"Multi-objective Evolutionary Algorithms are Still Good: Maximizing   Monotone Approximately Submodular Minus Modular Functions","url":"https://arxiv.org/pdf/1910.05492"},{"title":"Adaptive Submodular Policy Optimization","url":"https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_341.pdf"},{"title":"Submodular Minimization in the Context of Modern LP and MILP Methods and Solvers – Optimization Online","url":"https://optimization-online.org/2015/01/4762/"}]

Based on the web search results, I found relevant information about approximately submodular minus modular optimization:

The research studies the problem class of maximizing monotone approximately submodular minus modular functions (i.e., g-c) with a size constraint, where g is a non-negative monotone approximately submodular function.

In this context, f = g - c where g is a non-negative monotone approximately submodular function and c is a non-negative modular function, resulting in the objective function f being non-monotone nonsubmodular.

A simple multiobjective evolutionary algorithm (GSEMO) has been shown to achieve good polynomial-time approximation guarantees for submodular optimization, where the objective function is only required to satisfy certain properties.

Empirical studies on applications of Bayesian experimental design and directed vertex cover demonstrate the effectiveness of this approach.

However, the search results do not contain specific information about NLP (Natural Language Processing) applications or instantiations of this optimization technique in the 2024-2026 timeframe. The results primarily focus on the theoretical framework and algorithmic approaches rather than NLP-specific instantiations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "240cc65d-4539-441f-8df7-1ef5f4a227d6",
  "isSidechain": false,
  "promptId": "56213f29-1a0f-4729-bde9-d7c8e301fb24",
  "type": "user",
  "uuid": "de989194-e6e1-445a-85b2-84db4e474bdf",
  "toolUseResult": {
    "query": "approximately submodular minus modular optimization NLP application instantiation 2024 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UQXEMGUgudKgv67pLuc978",
        "content": [
          {
            "title": "Optimal Approximation for Submodular and Supermodular Optimization with Bounded Curvature | Mathematics of Operations Research",
            "url": "https://pubsonline.informs.org/doi/abs/10.1287/moor.2016.0842"
          },
          {
            "title": "Multiobjective Evolutionary Algorithms Are Still Good: Maximizing Monotone Approximately Submodular Minus Modular Functions | MIT Press Journals & Magazine | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/document/9655642"
          },
          {
            "title": "Multi-objective Evolutionary Algorithms are Still Good: Maximizing   Monotone Approximately Submodular Minus Modular Functions",
            "url": "https://arxiv.org/pdf/1910.05492"
          },
          {
            "title": "Adaptive Submodular Policy Optimization",
            "url": "https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_341.pdf"
          },
          {
            "title": "Submodular Minimization in the Context of Modern LP and MILP Methods and Solvers – Optimization Online",
            "url": "https://optimization-online.org/2015/01/4762/"
          }
        ]
      },
      "Based on the web search results, I found relevant information about approximately submodular minus modular optimization:\n\nThe research studies the problem class of maximizing monotone approximately submodular minus modular functions (i.e., g-c) with a size constraint, where g is a non-negative monotone approximately submodular function.\n\nIn this context, f = g - c where g is a non-negative monotone approximately submodular function and c is a non-negative modular function, resulting in the objective function f being non-monotone nonsubmodular.\n\nA simple multiobjective evolutionary algorithm (GSEMO) has been shown to achieve good polynomial-time approximation guarantees for submodular optimization, where the objective function is only required to satisfy certain properties.\n\nEmpirical studies on applications of Bayesian experimental design and directed vertex cover demonstrate the effectiveness of this approach.\n\nHowever, the search results do not contain specific information about NLP (Natural Language Processing) applications or instantiations of this optimization technique in the 2024-2026 timeframe. The results primarily focus on the theoretical framework and algorithmic approaches rather than NLP-specific instantiations."
    ],
    "durationSeconds": 7.301310771000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "240cc65d-4539-441f-8df7-1ef5f4a227d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-30T07:23:09.263Z_

```json
{
  "parentUuid": "de989194-e6e1-445a-85b2-84db4e474bdf",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "7e2313dd-c7b7-47bd-83e3-ea9da670ec11",
  "timestamp": "2026-05-30T07:23:09.263Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-30T07:23:12.496Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RRKBpSrXTMXJHXQkCJry4B`</summary>

```json
{
  "query": "AdaGATE adaptive gap-aware token-efficient evidence assembly multi-hop RAG 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e2313dd-c7b7-47bd-83e3-ea9da670ec11",
  "isSidechain": false,
  "requestId": "req_011CbYMNbqGuYq8Qg7zFrSVi",
  "type": "assistant",
  "uuid": "0b8a820f-457d-4aca-8cef-f39835854d05",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ARTXCR7yDepxwmQxumftAf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 772,
      "cache_read_input_tokens": 25336,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 772,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 25336,
          "cache_creation_input_tokens": 772,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 772
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

_source line 31 · 2026-05-30T07:23:23.912Z_

<details><summary>↩ Tool result · `toolu_01RRKBpSrXTMXJHXQkCJry4B`</summary>

```text
Web search results for query: "AdaGATE adaptive gap-aware token-efficient evidence assembly multi-hop RAG 2026"

Links: [{"title":"[2605.05245] AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2605.05245"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/new?skip=25&show=2000"},{"title":"AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop Retrieval-Augmented Generation","url":"https://arxiv.org/html/2605.05245"},{"title":"AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for","url":"https://arxiv.org/pdf/2605.05245"},{"title":"ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems | Request PDF","url":"https://www.researchgate.net/publication/382633733_ARES_An_Automated_Evaluation_Framework_for_Retrieval-Augmented_Generation_Systems"},{"title":"FAIR-RAG: Faithful Adaptive Iterative Refinement for Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2510.22344"},{"title":"Replace, Don't Expand: Mitigating Context Dilution in Multi-Hop RAG via Fixed-Budget Evidence Assembly","url":"https://arxiv.org/pdf/2512.10787"},{"title":"[2511.09803] Retrieval as a Decision: Training-Free Adaptive Gating for Efficient RAG","url":"https://arxiv.org/abs/2511.09803"}]

Based on the search results, here's what I found about AdaGATE:

AdaGATE is a training-free evidence controller for multi-hop RAG that frames evidence selection as a token-constrained repair problem. It combines entity centric gap tracking, targeted micro-query generation, and a utility based selection mechanism that balances gap coverage, corroboration, novelty, redundancy, and direct question relevance.

The research evaluated AdaGATE on HotpotQA under clean, redundancy, and noise injected retrieval conditions, achieving the best evidence F1 among compared controllers, reaching 62.3% on clean data and 71.2% under redundancy injection, while using 2.6x fewer input tokens than Adaptive-k. These results suggest that explicit gap-aware repair, combined with token-efficient evidence selection, improves robustness in multi-hop RAG under imperfect retrieval.

The paper was recently published on arXiv (May 2026) with authors including Yilin Guo, and code and evaluation pipeline are available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b8a820f-457d-4aca-8cef-f39835854d05",
  "isSidechain": false,
  "promptId": "56213f29-1a0f-4729-bde9-d7c8e301fb24",
  "type": "user",
  "uuid": "c5a33ce1-7271-47bb-922e-e4229cd01451",
  "toolUseResult": {
    "query": "AdaGATE adaptive gap-aware token-efficient evidence assembly multi-hop RAG 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GL7RN5gFdDoXs5k9Nd7W4E",
        "content": [
          {
            "title": "[2605.05245] AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop Retrieval-Augmented Generation",
            "url": "https://arxiv.org/abs/2605.05245"
          },
          {
            "title": "Computer Science",
            "url": "https://arxiv.org/list/cs/new?skip=25&show=2000"
          },
          {
            "title": "AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2605.05245"
          },
          {
            "title": "AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for",
            "url": "https://arxiv.org/pdf/2605.05245"
          },
          {
            "title": "ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems | Request PDF",
            "url": "https://www.researchgate.net/publication/382633733_ARES_An_Automated_Evaluation_Framework_for_Retrieval-Augmented_Generation_Systems"
          },
          {
            "title": "FAIR-RAG: Faithful Adaptive Iterative Refinement for Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2510.22344"
          },
          {
            "title": "Replace, Don't Expand: Mitigating Context Dilution in Multi-Hop RAG via Fixed-Budget Evidence Assembly",
            "url": "https://arxiv.org/pdf/2512.10787"
          },
          {
            "title": "[2511.09803] Retrieval as a Decision: Training-Free Adaptive Gating for Efficient RAG",
            "url": "https://arxiv.org/abs/2511.09803"
          }
        ]
      },
      "Based on the search results, here's what I found about AdaGATE:\n\nAdaGATE is a training-free evidence controller for multi-hop RAG that frames evidence selection as a token-constrained repair problem. It combines entity centric gap tracking, targeted micro-query generation, and a utility based selection mechanism that balances gap coverage, corroboration, novelty, redundancy, and direct question relevance.\n\nThe research evaluated AdaGATE on HotpotQA under clean, redundancy, and noise injected retrieval conditions, achieving the best evidence F1 among compared controllers, reaching 62.3% on clean data and 71.2% under redundancy injection, while using 2.6x fewer input tokens than Adaptive-k. These results suggest that explicit gap-aware repair, combined with token-efficient evidence selection, improves robustness in multi-hop RAG under imperfect retrieval.\n\nThe paper was recently published on arXiv (May 2026) with authors including Yilin Guo, and code and evaluation pipeline are available on GitHub."
    ],
    "durationSeconds": 11.408189394,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0b8a820f-457d-4aca-8cef-f39835854d05",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-30T07:23:33.799Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VWwrw9JQvw3F6Rj9cXw8XZ`</summary>

```json
{
  "query": "Vendi-RAG vendi score diversity quality retrieval augmented generation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5a33ce1-7271-47bb-922e-e4229cd01451",
  "isSidechain": false,
  "requestId": "req_011CbYMPgLApLkV8eNJT1aBv",
  "type": "assistant",
  "uuid": "364d54ab-794a-42f1-b599-aeccbe2dd94d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJiXTnpxmbEArRsn8PvTF2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 26108,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 781,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 26108,
          "cache_creation_input_tokens": 781,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 781
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

_source line 33 · 2026-05-30T07:23:41.148Z_

<details><summary>↩ Tool result · `toolu_01VWwrw9JQvw3F6Rj9cXw8XZ`</summary>

```text
Web search results for query: "Vendi-RAG vendi score diversity quality retrieval augmented generation 2025"

Links: [{"title":"Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs","url":"https://arxiv.org/html/2502.11228v2"},{"title":"[2502.11228] Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs","url":"https://arxiv.org/abs/2502.11228"},{"title":"(PDF) Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs","url":"https://www.researchgate.net/publication/389090989_Vendi-RAG_Adaptively_Trading-Off_Diversity_And_Quality_Significantly_Improves_Retrieval_Augmented_Generation_With_LLMs"},{"title":"[Literature Review] Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs","url":"https://www.themoonlight.io/en/review/vendi-rag-adaptively-trading-off-diversity-and-quality-significantly-improves-retrieval-augmented-generation-with-llms"},{"title":"Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs | Article Information | J-GLOBAL","url":"https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=202502218784102922"},{"title":"dblp: Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs.","url":"https://dblp.org/rec/journals/corr/abs-2502-11228.html"}]

Based on the search results, here's what I found about Vendi-RAG:

## Overview

Vendi-RAG is a framework based on an iterative process that jointly optimizes retrieval diversity and answer quality. The paper was presented by Mohammad R. Rezaei and Adji Bousso Dieng and focuses on improving the retrieval-augmented generation process in large language models, particularly for multi-hop question-answering tasks.

## Problem It Addresses

Traditional RAG systems primarily focus on relevance-based retrieval and often struggle with redundancy, especially when reasoning requires connecting information from multiple sources.

## Key Innovation: The Vendi Score

Vendi-RAG leverages the Vendi Score, a flexible similarity-based diversity metric, to promote semantic diversity in document retrieval. The process begins with an initial retrieval step, where a diverse set of documents is retrieved using the Vendi Score, ensuring broad semantic coverage.

## How It Works

An LLM judge evaluates candidate answers, generated after a reasoning step, and outputs a score that the retriever uses to balance relevance and diversity among the retrieved documents during each iteration.

## Results

This joint optimization leads to significantly higher accuracy for multi-hop QA tasks.

The paper was published in February 2025 on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "364d54ab-794a-42f1-b599-aeccbe2dd94d",
  "isSidechain": false,
  "promptId": "56213f29-1a0f-4729-bde9-d7c8e301fb24",
  "type": "user",
  "uuid": "9ac07c91-0962-433f-a588-a87ec3bb592d",
  "toolUseResult": {
    "query": "Vendi-RAG vendi score diversity quality retrieval augmented generation 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_017WVaZdDMP2515Vz67iy5y8",
        "content": [
          {
            "title": "Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs",
            "url": "https://arxiv.org/html/2502.11228v2"
          },
          {
            "title": "[2502.11228] Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs",
            "url": "https://arxiv.org/abs/2502.11228"
          },
          {
            "title": "(PDF) Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs",
            "url": "https://www.researchgate.net/publication/389090989_Vendi-RAG_Adaptively_Trading-Off_Diversity_And_Quality_Significantly_Improves_Retrieval_Augmented_Generation_With_LLMs"
          },
          {
            "title": "[Literature Review] Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs",
            "url": "https://www.themoonlight.io/en/review/vendi-rag-adaptively-trading-off-diversity-and-quality-significantly-improves-retrieval-augmented-generation-with-llms"
          },
          {
            "title": "Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs | Article Information | J-GLOBAL",
            "url": "https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=202502218784102922"
          },
          {
            "title": "dblp: Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs.",
            "url": "https://dblp.org/rec/journals/corr/abs-2502-11228.html"
          }
        ]
      },
      "Based on the search results, here's what I found about Vendi-RAG:\n\n## Overview\n\nVendi-RAG is a framework based on an iterative process that jointly optimizes retrieval diversity and answer quality. The paper was presented by Mohammad R. Rezaei and Adji Bousso Dieng and focuses on improving the retrieval-augmented generation process in large language models, particularly for multi-hop question-answering tasks.\n\n## Problem It Addresses\n\nTraditional RAG systems primarily focus on relevance-based retrieval and often struggle with redundancy, especially when reasoning requires connecting information from multiple sources.\n\n## Key Innovation: The Vendi Score\n\nVendi-RAG leverages the Vendi Score, a flexible similarity-based diversity metric, to promote semantic diversity in document retrieval. The process begins with an initial retrieval step, where a diverse set of documents is retrieved using the Vendi Score, ensuring broad semantic coverage.\n\n## How It Works\n\nAn LLM judge evaluates candidate answers, generated after a reasoning step, and outputs a score that the retriever uses to balance relevance and diversity among the retrieved documents during each iteration.\n\n## Results\n\nThis joint optimization leads to significantly higher accuracy for multi-hop QA tasks.\n\nThe paper was published in February 2025 on arXiv."
    ],
    "durationSeconds": 7.34240989499999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "364d54ab-794a-42f1-b599-aeccbe2dd94d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
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
  "lastPrompt": "# Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition  ## Core Problem  How can post-retrieval context composition for RAG be formalized as a constrained non-monotone…",
  "leafUuid": "9ac07c91-0962-433f-a588-a87ec3bb592d",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Non-monotone submodular context composition for RAG",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0"
}
```

---

### Tool call

_source line 36 · 2026-05-30T07:23:44.393Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XkcN6oPtQoZoKc3g93uvig`</summary>

```json
{
  "query": "ScalDPP scaling DPP retrieval augmented generation P-Adapter diverse margin loss 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ac07c91-0962-433f-a588-a87ec3bb592d",
  "isSidechain": false,
  "requestId": "req_011CbYMQx2WtGPDMN2n9KSzi",
  "type": "assistant",
  "uuid": "9888fac5-d78b-4ffa-9ac1-7c6c9759b83b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N1kPQ1GckDgMVvwXnE8MG6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 889,
      "cache_read_input_tokens": 26889,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 889,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 26889,
          "cache_creation_input_tokens": 889,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 889
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

_source line 37 · 2026-05-30T07:23:52.444Z_

<details><summary>↩ Tool result · `toolu_01XkcN6oPtQoZoKc3g93uvig`</summary>

```text
Web search results for query: "ScalDPP scaling DPP retrieval augmented generation P-Adapter diverse margin loss 2026"

Links: [{"title":"Scaling DPPs for RAG: Density Meets Diversity","url":"https://arxiv.org/pdf/2604.03240"},{"title":"Scaling DPPs for RAG: Density Meets Diversity","url":"https://arxiv.org/html/2604.03240"},{"title":"[2604.03240] Scaling DPPs for RAG: Density Meets Diversity","url":"https://arxiv.org/abs/2604.03240"},{"title":"Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming","url":"https://arxiv.org/pdf/2604.02554"},{"title":"Inference Scaling for Bridging Retrieval and Augmented Generation","url":"https://arxiv.org/html/2412.10684v1"},{"title":"(PDF) Inference Scaling for Long-Context Retrieval Augmented Generation","url":"https://www.researchgate.net/publication/384698992_Inference_Scaling_for_Long-Context_Retrieval_Augmented_Generation"}]

Based on the search results, I found relevant information about ScalDPP:

ScalDPP is a diversity-aware retrieval mechanism for RAG that incorporates Determinantal Point Processes (DPPs) through a lightweight P-Adapter, enabling scalable modeling of inter-chunk dependencies and complementary context selection.

The approach develops a novel set-level objective called Diverse Margin Loss (DML), which enforces ground-truth complementary evidence chains to dominate any equally sized redundant alternatives under DPP geometry.

The underlying problem addressed is that standard RAG pipelines ignore interactions among retrieved candidates, leading to redundant contexts that dilute density and fail to surface complementary evidence. ScalDPP argues that effective retrieval should optimize jointly for both density and diversity, ensuring the grounding evidence is dense in information yet diverse in coverage.

The research paper was published as a preprint on April 7, 2026, according to the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9888fac5-d78b-4ffa-9ac1-7c6c9759b83b",
  "isSidechain": false,
  "promptId": "56213f29-1a0f-4729-bde9-d7c8e301fb24",
  "type": "user",
  "uuid": "f263b03d-a2e8-4ce0-8d51-3ff494125ba8",
  "toolUseResult": {
    "query": "ScalDPP scaling DPP retrieval augmented generation P-Adapter diverse margin loss 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TSk1192gu3mvEaQvdWu7kM",
        "content": [
          {
            "title": "Scaling DPPs for RAG: Density Meets Diversity",
            "url": "https://arxiv.org/pdf/2604.03240"
          },
          {
            "title": "Scaling DPPs for RAG: Density Meets Diversity",
            "url": "https://arxiv.org/html/2604.03240"
          },
          {
            "title": "[2604.03240] Scaling DPPs for RAG: Density Meets Diversity",
            "url": "https://arxiv.org/abs/2604.03240"
          },
          {
            "title": "Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming",
            "url": "https://arxiv.org/pdf/2604.02554"
          },
          {
            "title": "Inference Scaling for Bridging Retrieval and Augmented Generation",
            "url": "https://arxiv.org/html/2412.10684v1"
          },
          {
            "title": "(PDF) Inference Scaling for Long-Context Retrieval Augmented Generation",
            "url": "https://www.researchgate.net/publication/384698992_Inference_Scaling_for_Long-Context_Retrieval_Augmented_Generation"
          }
        ]
      },
      "Based on the search results, I found relevant information about ScalDPP:\n\nScalDPP is a diversity-aware retrieval mechanism for RAG that incorporates Determinantal Point Processes (DPPs) through a lightweight P-Adapter, enabling scalable modeling of inter-chunk dependencies and complementary context selection.\n\nThe approach develops a novel set-level objective called Diverse Margin Loss (DML), which enforces ground-truth complementary evidence chains to dominate any equally sized redundant alternatives under DPP geometry.\n\nThe underlying problem addressed is that standard RAG pipelines ignore interactions among retrieved candidates, leading to redundant contexts that dilute density and fail to surface complementary evidence. ScalDPP argues that effective retrieval should optimize jointly for both density and diversity, ensuring the grounding evidence is dense in information yet diverse in coverage.\n\nThe research paper was published as a preprint on April 7, 2026, according to the search results."
    ],
    "durationSeconds": 8.047357686999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9888fac5-d78b-4ffa-9ac1-7c6c9759b83b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-30T07:23:55.886Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me do one more search to check if anyone has recently combined formal optimization guarantees with distraction-awareness in RAG, which is the core novelty claim of this proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f263b03d-a2e8-4ce0-8d51-3ff494125ba8",
  "isSidechain": false,
  "requestId": "req_011CbYMRoXa5saDwrCoLgHvN",
  "type": "assistant",
  "uuid": "5ce861d2-a006-4d78-b995-a43590e57632",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qiBmfsiEAmXA6ru9kZCdr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 621,
      "cache_read_input_tokens": 27778,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 621,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 125,
          "cache_read_input_tokens": 27778,
          "cache_creation_input_tokens": 621,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 621
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

_source line 39 · 2026-05-30T07:23:56.588Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013nji7SbBbRmKybvkYAZLpC`</summary>

```json
{
  "query": "post-retrieval context composition formal optimization guarantees distraction aware RAG 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ce861d2-a006-4d78-b995-a43590e57632",
  "isSidechain": false,
  "requestId": "req_011CbYMRoXa5saDwrCoLgHvN",
  "type": "assistant",
  "uuid": "817b0d98-eae1-4fcb-ad9c-b2816e405f58",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019qiBmfsiEAmXA6ru9kZCdr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 621,
      "cache_read_input_tokens": 27778,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 621,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 125,
          "cache_read_input_tokens": 27778,
          "cache_creation_input_tokens": 621,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 621
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

_source line 40 · 2026-05-30T07:24:03.636Z_

<details><summary>↩ Tool result · `toolu_013nji7SbBbRmKybvkYAZLpC`</summary>

```text
Web search results for query: "post-retrieval context composition formal optimization guarantees distraction aware RAG 2025 2026"

Links: [{"title":"[2509.21865] Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding","url":"https://arxiv.org/abs/2509.21865"},{"title":"Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding","url":"https://arxiv.org/pdf/2509.21865"},{"title":"PrismRAG: Boosting RAG Factuality with Distractor Resilience and Strategized Reasoning","url":"https://arxiv.org/pdf/2507.18857"},{"title":"When RAG Hurts: Diagnosing and Mitigating Attention Distraction in Retrieval-Augmented LVLMs","url":"https://arxiv.org/pdf/2602.00344"},{"title":"(PDF) The Evolution of Retrieval-Augmented Generation (RAG) in AI","url":"https://www.researchgate.net/publication/399423892_The_Evolution_of_Retrieval-Augmented_Generation_RAG_in_AI"},{"title":"From RAG to Context - A 2025 year-end review of RAG | RAGFlow","url":"https://ragflow.io/blog/rag-review-2025-from-rag-to-context"}]

Based on the web search results, here's what I found relevant to your query:

## Key Research Findings

LDAR (Learning Distraction-Aware Retrieval) is an adaptive retriever that learns to retrieve contexts in a way that mitigates interference from distracting passages, thereby achieving significantly higher performance with reduced token usage compared to long-context approaches. Extensive experiments across diverse LLM architectures and six knowledge-intensive benchmarks demonstrate the effectiveness and robustness of this approach.

Research shows that appending large blocks of retrieved content, such as entire web pages or lengthy documents, can overwhelm the model and induce hallucinations. This addresses the broader challenge of distraction in RAG systems.

Another relevant work, PRISMRAG, enhances LLM's capability in generating answers from multiple retrieval results.

## Context Composition Challenges

Mechanically stuffing lengthy text into an LLM's context window is essentially a "brute-force" strategy that inevitably scatters the model's attention, significantly degrading answer quality through the "Lost in the Middle" or "information flooding" effect.

The search results indicate that distraction-aware RAG and post-retrieval context optimization are active research areas in 2025-2026, with focus on balancing information coverage while mitigating interference from irrelevant passages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "817b0d98-eae1-4fcb-ad9c-b2816e405f58",
  "isSidechain": false,
  "promptId": "56213f29-1a0f-4729-bde9-d7c8e301fb24",
  "type": "user",
  "uuid": "9fce0d9c-17df-47e3-8cbb-2c86efbd5d08",
  "toolUseResult": {
    "query": "post-retrieval context composition formal optimization guarantees distraction aware RAG 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CUJ2qAsh87xhE7nuZLaZnP",
        "content": [
          {
            "title": "[2509.21865] Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding",
            "url": "https://arxiv.org/abs/2509.21865"
          },
          {
            "title": "Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding",
            "url": "https://arxiv.org/pdf/2509.21865"
          },
          {
            "title": "PrismRAG: Boosting RAG Factuality with Distractor Resilience and Strategized Reasoning",
            "url": "https://arxiv.org/pdf/2507.18857"
          },
          {
            "title": "When RAG Hurts: Diagnosing and Mitigating Attention Distraction in Retrieval-Augmented LVLMs",
            "url": "https://arxiv.org/pdf/2602.00344"
          },
          {
            "title": "(PDF) The Evolution of Retrieval-Augmented Generation (RAG) in AI",
            "url": "https://www.researchgate.net/publication/399423892_The_Evolution_of_Retrieval-Augmented_Generation_RAG_in_AI"
          },
          {
            "title": "From RAG to Context - A 2025 year-end review of RAG | RAGFlow",
            "url": "https://ragflow.io/blog/rag-review-2025-from-rag-to-context"
          }
        ]
      },
      "Based on the web search results, here's what I found relevant to your query:\n\n## Key Research Findings\n\nLDAR (Learning Distraction-Aware Retrieval) is an adaptive retriever that learns to retrieve contexts in a way that mitigates interference from distracting passages, thereby achieving significantly higher performance with reduced token usage compared to long-context approaches. Extensive experiments across diverse LLM architectures and six knowledge-intensive benchmarks demonstrate the effectiveness and robustness of this approach.\n\nResearch shows that appending large blocks of retrieved content, such as entire web pages or lengthy documents, can overwhelm the model and induce hallucinations. This addresses the broader challenge of distraction in RAG systems.\n\nAnother relevant work, PRISMRAG, enhances LLM's capability in generating answers from multiple retrieval results.\n\n## Context Composition Challenges\n\nMechanically stuffing lengthy text into an LLM's context window is essentially a \"brute-force\" strategy that inevitably scatters the model's attention, significantly degrading answer quality through the \"Lost in the Middle\" or \"information flooding\" effect.\n\nThe search results indicate that distraction-aware RAG and post-retrieval context optimization are active research areas in 2025-2026, with focus on balancing information coverage while mitigating interference from irrelevant passages."
    ],
    "durationSeconds": 7.041249246000021,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "817b0d98-eae1-4fcb-ad9c-b2816e405f58",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-30T07:24:06.661Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RMaMrZGEHyZjDBAyopWeCC`</summary>

```json
{
  "query": "Sub-CP submodular context partitioning in-context learning arXiv 2510.05130"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fce0d9c-17df-47e3-8cbb-2c86efbd5d08",
  "isSidechain": false,
  "requestId": "req_011CbYMScAyJaHWg2bnW38Pg",
  "type": "assistant",
  "uuid": "21f5ca20-09a1-4543-82a8-78c00eadd8e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G5xaAishNyWcRXRbb9XHDt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 807,
      "cache_read_input_tokens": 28399,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 807,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 28399,
          "cache_creation_input_tokens": 807,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 807
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

_source line 42 · 2026-05-30T07:24:13.264Z_

<details><summary>↩ Tool result · `toolu_01RMaMrZGEHyZjDBAyopWeCC`</summary>

```text
Web search results for query: "Sub-CP submodular context partitioning in-context learning arXiv 2510.05130"

Links: [{"title":"[2510.05130] Submodular Context Partitioning and Compression for In-Context Learning","url":"https://arxiv.org/abs/2510.05130"},{"title":"Submodular Context Partitioning for In-Context Learning","url":"https://arxiv.org/html/2510.05130v1"},{"title":"Submodular Context Partitioning for In-Context Learning Shaoyi Zheng1","url":"https://arxiv.org/pdf/2510.05130"},{"title":"Sub-SA: Strengthen In-context Learning via Submodular Selective   Annotation","url":"https://arxiv.org/pdf/2407.05693"},{"title":"[2407.05693] Sub-SA: Strengthen In-context Learning via Submodular Selective Annotation","url":"https://arxiv.org/abs/2407.05693"}]

Based on the search results, here's what I found about the arXiv paper 2510.05130:

## Submodular Context Partitioning for In-Context Learning

Sub-CP is a block-aware context selection framework that leverages submodular objectives to control block diversity. 

**The Problem:**
In-context learning (ICL) enables efficient few-shot learning in large language models (LLMs) without training, but suffers from the quadratic input complexity of transformers, limiting the maximum number of exemplars. While various efficient ICL approaches partition the context into blocks to process (e.g., ensembling, compression, cross-attention), they often ignore the information redundancy or under-representation caused by different partition strategies, leading to suboptimal performance.

**The Solution:**
Sub-CP supports a flexible spectrum of selection strategies, allowing each block to range from globally diverse to locally coherent. This allows fine-grained control over semantic structure while enabling precomputation.

**Results:**
Extensive experiments across diverse tasks on multiple datasets show that Sub-CP consistently improves performance across model scales.

The paper was authored by Shaoyi Zheng and colleagues, with the latest version posted on October 9, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21f5ca20-09a1-4543-82a8-78c00eadd8e2",
  "isSidechain": false,
  "promptId": "56213f29-1a0f-4729-bde9-d7c8e301fb24",
  "type": "user",
  "uuid": "13d63702-c849-4997-8cb5-9e02d600a5e9",
  "toolUseResult": {
    "query": "Sub-CP submodular context partitioning in-context learning arXiv 2510.05130",
    "results": [
      {
        "tool_use_id": "srvtoolu_019trsTcWzczib2jvQv1oMbB",
        "content": [
          {
            "title": "[2510.05130] Submodular Context Partitioning and Compression for In-Context Learning",
            "url": "https://arxiv.org/abs/2510.05130"
          },
          {
            "title": "Submodular Context Partitioning for In-Context Learning",
            "url": "https://arxiv.org/html/2510.05130v1"
          },
          {
            "title": "Submodular Context Partitioning for In-Context Learning Shaoyi Zheng1",
            "url": "https://arxiv.org/pdf/2510.05130"
          },
          {
            "title": "Sub-SA: Strengthen In-context Learning via Submodular Selective   Annotation",
            "url": "https://arxiv.org/pdf/2407.05693"
          },
          {
            "title": "[2407.05693] Sub-SA: Strengthen In-context Learning via Submodular Selective Annotation",
            "url": "https://arxiv.org/abs/2407.05693"
          }
        ]
      },
      "Based on the search results, here's what I found about the arXiv paper 2510.05130:\n\n## Submodular Context Partitioning for In-Context Learning\n\nSub-CP is a block-aware context selection framework that leverages submodular objectives to control block diversity. \n\n**The Problem:**\nIn-context learning (ICL) enables efficient few-shot learning in large language models (LLMs) without training, but suffers from the quadratic input complexity of transformers, limiting the maximum number of exemplars. While various efficient ICL approaches partition the context into blocks to process (e.g., ensembling, compression, cross-attention), they often ignore the information redundancy or under-representation caused by different partition strategies, leading to suboptimal performance.\n\n**The Solution:**\nSub-CP supports a flexible spectrum of selection strategies, allowing each block to range from globally diverse to locally coherent. This allows fine-grained control over semantic structure while enabling precomputation.\n\n**Results:**\nExtensive experiments across diverse tasks on multiple datasets show that Sub-CP consistently improves performance across model scales.\n\nThe paper was authored by Shaoyi Zheng and colleagues, with the latest version posted on October 9, 2025."
    ],
    "durationSeconds": 6.598071626999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "21f5ca20-09a1-4543-82a8-78c00eadd8e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-30T07:25:17.072Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the research landscape. Let me synthesize my findings and evaluate this proposal.

Key findings from my research:

1. **The gap claim is legitimate**: No existing work simultaneously provides (a) post-retrieval composition, (b) formal approximation guarantees, and (c) distraction-awareness. AdaGReS handles redundancy with formal guarantees but no distraction. LDAR/DynamicRAG/Context-Picker handle distraction but with no formal guarantees. CCBQP and ScalDPP handle relevance-diversity but no distraction.


2. **The "approximately submodular minus modular" instantiation in NLP appears genuinely novel**: Qian's theoretical framework exists for Bayesian experimental design and directed vertex cover, but I haven't found NLP applications of this specific formulation.
3. **The three building blocks check out**: AdaGReS, The Distracting Effect, and the AAMAS 2026 paper are all real and correctly described, and this particular combination hasn't been explored before.
4. **There's a potential novelty concern**: AdaGATE from May 2026 is a concurrent work that addresses multi-hop retrieval, which could overlap with some aspects of this proposal.

Looking at the other related work more carefully, SMART-RAG models inter-passage contradictions rather than answer-conditional interference, which is a different problem. CCBQP's relevance weighting also operates differently from the distraction modeling here. The decomposition between redundancy and distraction—framed as opportunity cost versus interference cost—seems to be the genuine conceptual contribution, and I'm not finding this specific formulation elsewhere with formal optimization treatment.

The two-stage pipeline alternative (filter then AdaGReS) is already addressed in the proposal, and the argument about losing optimality guarantees when pre-filtering is sound. Now I need to examine the core assumptions more carefully.

The modularity assumption for distraction—that it's independent across passages—is a simplification since multiple distractors could compound in practice. The proposal does acknowledge this with the conditional ablation, which is reassuring. The bounded-embedding conditions for the γ-weak DR-submodularity property will need empirical verification, which the proposal plans to do.

The real novelty here is bringing together three separate pieces into one coherent framework: the conceptual split between redundancy and distraction, the theoretical derivation showing γ-weak DR-submodularity holds for the combined objective, and the first NLP application of "approximately submodular minus modular" optimization. That's a legitimate bridging contribution.

The key vulnerability is whether the γ derivation itself is substantial or just mechanical—if it's just plugging the modular subtraction into an existing framework, reviewers might see it as incremental, but if it requires domain-specific analysis for RAG, that strengthens the theoretical contribution. Similarly, claiming to be the first NLP instantiation is a strong positioning but also risky if someone argues it's merely applying existing theory. The framing could emphasize the broader implications beyond just RAG optimization—formalizing when and how to decompose objectives this way has wider significance.

To strengthen the work, I could elevate γ as a practical diagnostic tool that tells you per-query how difficult composition is, position the redundancy-versus-distraction decomposition as a conceptual contribution to RAG itself rather than just a modeling choice, and more explicitly connect this framework to the broader context engineering landscape across in-context learning, tool composition, and multi-document grounding.

But I should also check for real limitations: whether the modularity assumption for distraction effects holds when multiple distractors interact, whether γ is actually computable at scale given the exponential subset space, and how tight the approximations are in practice. I'm noticing a few ways to strengthen the positioning. The "first NLP instantiation" claim is valuable but risks seeming like a straightforward application—I should emphasize what's genuinely domain-specific about the derivation, like the bounded-embedding conditions and the particular structure of how redundancy and distraction interact differently. Beyond that, the redundancy-distraction decomposition could be reframed as a conceptual contribution to RAG itself: not just a modeling choice, but a formal taxonomy identifying distinct causal mechanisms for how context quality degrades, each requiring different mathematical treatment. There's also potential in connecting this back to how LLM attention mechanisms actually work in practice.

The empirical results matter too. If γ consistently comes out near 1, that would suggest monotone greedy is sufficient and the whole non-monotone framework is unnecessary—a genuinely important negative finding that the proposal should explicitly frame as a testable hypothesis rather than glossing over. The distinction between γ ≈ 1 (theoretically valid but practically irrelevant) and γ ≪ 1 (both theoretically and practically important) is crucial for understanding what the work actually contributes. ate the decomposition from modeling choice to conceptual contribution**: The redundancy vs. distraction distinction, with its different causal mechanisms and scaling behaviors, is a genuine conceptual contribution to the RAG literature. Currently framed as motivation for the objective function design; could be elevated to a first-class contribution with broader implications.

2. **γ computability and the practical significance threshold**: The proposal plans to compute γ but doesn't address the computational cost (exponential in theory) or what constitutes a "practically meaningful" γ value. This is important because if γ is always close to 1 or always very small, the theoretical contribution has very different implications.

3. **Framing the theoretical contribution more precisely**: The real novelty lies in demonstrating that the RAG distraction-redundancy problem exhibits a specific γ-weak DR-submodular structure under bounded-embedding conditions, which yields provable approximation guarantees for non-monotone context composition—this is a structural analysis rather than just applying an existing framework to a new domain.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13d63702-c849-4997-8cb5-9e02d600a5e9",
  "isSidechain": false,
  "requestId": "req_011CbYMTKPCzJKtBzkPLZXa6",
  "type": "assistant",
  "uuid": "3502c9b8-75d8-43db-bfec-987297eb0381",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MHv2Y4crhR5b6M32tRwjZM",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 630,
      "cache_read_input_tokens": 29206,
      "output_tokens": 5977,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 630,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5977,
          "cache_read_input_tokens": 29206,
          "cache_creation_input_tokens": 630,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 630
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

_source line 44 · 2026-05-30T07:26:33.735Z_

Now I have sufficient research context. Let me synthesize my findings and produce the evaluation.

---

【状态】: 有发掘空间

【前置调研发现】
- [AdaGReS, arXiv:2512.25052] (Dec 2025): 最直接的前序工作。证明了 redundancy-penalized context selection 的 ε-approximate submodularity，但仅处理 monotone 目标函数。本 proposal 正确地以此为起点并识别其局限。
- [The Distracting Effect, ACL 2025] (arXiv:2505.06914): 提出 per-passage 的 DE_q(p) 度量，量化不相关段落对生成质量的干扰效应。仅做诊断性分析，未进行 set-level 优化。本 proposal 正确地将其作为 modular penalty 的来源。
- [AAMAS 2026 γ-weakly DR-submodular] (arXiv:2601.00611): 提供非单调 γ-弱 DR-submodular 函数的近似保证 Φ_γ，纯理论工作，无 NLP 实证。本 proposal 计划首次将其实例化到 RAG 领域。
- [CCBQP, arXiv:2604.02554] (Apr 2026): Frank-Wolfe 求解 relevance-diversity Pareto 前沿，在 QAMPARI/ASQA 上优于 MMR 和 DPP，但仅处理 relevance-diversity 而非 distraction。
- [Qian, arXiv:1910.05492]: "approximately submodular minus modular" 问题类的理论框架和 GSEMO 算法，应用于贝叶斯实验设计和有向顶点覆盖——搜索未发现任何 NLP/RAG 领域的实例化工作。
- [AdaGATE, arXiv:2605.05245] (May 2026): 最新的并发工作，multi-hop evidence assembly，考虑 gap coverage/redundancy/novelty，但无形式化优化保证，未分解 redundancy vs. distraction 的因果机制。
- [ScalDPP, arXiv:2604.03240] (Apr 2026): 通过 P-Adapter + Diverse Margin Loss 扩展 DPP，仍在 relevance-diversity 范式，需要训练。
- [Vendi-RAG, arXiv:2502.11228] (Feb 2025): 使用 Vendi Score + LLM judge 迭代优化 diversity-quality，无形式化保证，未显式分解 distraction。
- [LDAR, ICLR 2026] / [DynamicRAG, NeurIPS 2025] / [Context-Picker, Dec 2025]: 均为 learned approaches，distraction-aware 但无形式化保证。
- 调研总结：当前 RAG context composition 领域形成了明确的两极分化——形式化方法（AdaGReS, CCBQP, DPP 系列）只处理 relevance-diversity，学习方法（LDAR, DynamicRAG, Context-Picker）处理 distraction 但无理论保证。这个 gap 是真实存在的，proposal 的定位准确。同时，"approximately submodular minus modular" 在 NLP 中的实例化确实是空白。

---

【发掘点 1】
- 维度: 核心 claim 强化 / significance 提升
- 内容: Proposal 目前将 redundancy-distraction 分解主要定位为一个**建模选择**（"我们设计了这样的目标函数"）。建议将其提升为一项**对 RAG 领域的概念性贡献**——即对"额外上下文如何损害生成质量"这一问题的形式化分类学（formal taxonomy of context quality degradation）。具体地：redundancy 作为 opportunity cost（间接损害，边际递减）vs. distraction 作为 interference cost（直接损害，可能叠加）这个二分法，不仅仅是设计目标函数的依据，而是对 RAG 文献中长期混淆的两种不同失效模式的**理论澄清**。目前的 related work（AdaGReS 把一切都归为 redundancy，CCBQP 只看 diversity，SMART-RAG 的 "conflict" 捕捉的是 inter-passage contradiction 而非 answer-conditional interference）恰好证明了这种概念混淆的普遍性。如果将此分解从"Section 3 的建模动机"提升为"Section 1/2 的核心主张之一"，论文的概念贡献层次会显著提升——审稿人会认为这是"改变了我们理解问题的方式"而不仅仅是"提出了一个新的目标函数"。
- 价值: 直接提升 Significance 和 Novelty。一个 conceptual taxonomy contribution 的持久影响力和引用价值远高于一个具体的算法。即使后续有人用更好的算法替代 double-greedy，这个分解框架仍然成立。
- 调研依据: 基于对 AdaGReS（只建模 redundancy）、CCBQP（只建模 diversity）、SMART-RAG（把 conflict 和 distraction 混为一谈）、The Distracting Effect（只做诊断未做优化）的全面对比，发现当前文献确实普遍混淆这两种不同的退化机制，该分解确实填补了概念层面的空白。

【发掘点 2】
- 维度: novelty 锐化 / 前提假设质疑
- 内容: Proposal 的理论贡献核心是"推导 RAG 目标函数的 γ-weak DR-submodularity 参数"。但目前的描述方式有一个潜在的审稿人攻击面：**这个推导是 trivial 的（只是把 modular term 从 approximately submodular function 里减掉，然后直接套用 AAMAS 框架），还是 non-trivial 的（需要 RAG 域的特定分析）？** Proposal 提到了 bounded-embedding conditions（嵌入范数有界、diminishing-return ratio 下界依赖于 c_min/c_max 和最大 pairwise similarity），这些条件的推导确实是 domain-specific 的。建议在 novelty framing 上**更锐利地区分**：核心理论贡献不是"我们把 AAMAS 框架应用到了 NLP"（这听起来 incremental），而是"我们证明了 RAG 的 distraction-redundancy 目标在 bounded-embedding 条件下具有特定的 γ-weak DR-submodular 结构，且 γ 的大小由检索候选池的语义结构（c_min/c_max 比值、最大 pairwise similarity）决定——这意味着近似保证的强度本身编码了组合优化问题的固有难度"。后者将理论贡献从"application of existing theory"重新定位为"structural analysis of a domain-specific problem class"。
- 价值: 直接锐化 Novelty claim，降低被审稿人评价为"incremental theory application"的风险。这是 borderline accept/reject 时的关键分界线。
- 调研依据: Qian (arXiv:1910.05492) 的工作提供了 "approximately submodular minus modular" 的通用理论框架，但其应用（贝叶斯实验设计、有向顶点覆盖）中的 γ 推导都涉及 domain-specific 的结构分析，而非简单的框架套用。本 proposal 的 bounded-embedding 条件分析应参考同样的定位层次。

【发掘点 3】
- 维度: 前提假设质疑
- 内容: γ 的计算方式存在一个**未被显式讨论的实践性问题**。Proposal 写道"Compute γ per-query as the minimum diminishing-return ratio over all passage subsets"——但这在理论上是指数复杂度的（需要遍历所有子集对）。对于 50-200 个候选段落的实际候选池，精确计算 γ 不可行。Proposal 需要明确：(a) 是否使用 γ 的解析下界（从 bounded-embedding conditions 直接推导，无需遍历子集）；(b) 如果需要经验估计，使用什么采样策略，估计误差如何影响近似保证。这不是实验设计问题（不涉及加 ablation），而是**理论 claim 的可操作性问题**——如果 γ 声称既是理论保证的参数又是实践诊断工具，那它必须是可高效计算的。建议在理论部分明确给出 γ 的解析下界公式（基于 c_min, c_max, max pairwise similarity），并将经验测量定位为"验证解析下界的 tightness"，而非"计算 γ 的唯一手段"。
- 价值: 消除理论贡献中的一个逻辑缺口，增强 claim 的 soundness。如果审稿人发现 γ 的定义不可计算，会直接质疑整个理论框架的实用性。这是 Novelty 和 Significance 的防御性强化。
- 调研依据: AAMAS 2026 论文 (arXiv:2601.00611) 中 γ 被定义为函数的全局属性（minimum DR ratio），在理论分析中是分析工具而非需要计算的量。但本 proposal 要将 γ 同时用作 per-query 诊断工具，这个额外的实用性 claim 需要额外的计算可行性论证。

【发掘点 4】
- 维度: significance 提升
- 内容: Proposal 的 broader motivation 部分提到了 context engineering 的普遍性——in-context learning、tool-use composition、multi-document grounding 都展现非单调收益。但这个宏观视角目前仅作为引言叙事，未被真正发掘为贡献。建议在 discussion/conclusion 中明确论述：本文的 "approximately submodular minus modular" 框架不仅适用于 RAG，任何涉及"信息收益（approximately submodular）减去干扰成本（modular）"的上下文组合问题都可以复用此框架——包括 ICL exemplar selection（其中 Sub-CP 只处理了 monotone 情况）、tool-use composition（选择 API 调用组合时某些工具可能引入噪声）、multi-agent 通信（消息组合中的冗余与干扰）。这把论文从"RAG 优化的一个方法"提升为"context engineering 的一个通用理论工具"，显著扩大 audience 和引用面。但注意：这应该是一个 well-scoped 的 discussion，而非 overclaim——核心实证仍然锚定在 RAG，通用性是有理论支撑的展望。
- 价值: 提升 Significance 天花板。AAAI 作为综合性 AI 会议，审稿人群体涵盖 NLP、优化、多智能体等多个领域。一个具有跨领域通用性的框架比一个 RAG-specific 方法更有吸引力。
- 调研依据: Sub-CP (arXiv:2510.05130) 在 ICL 中使用 submodular optimization 处理 exemplar partitioning，但仅处理 monotone 情况。这直接支持了"非单调上下文组合问题广泛存在但理论工具缺失"的论述。

Sources:
- [AdaGReS](https://arxiv.org/pdf/2512.25052)
- [The Distracting Effect (ACL 2025)](https://aclanthology.org/2025.acl-long.892/)
- [AAMAS 2026 γ-weakly DR-submodular](https://arxiv.org/abs/2601.00611)
- [CCBQP](https://arxiv.org/abs/2604.02554)
- [Qian - Approximately Submodular Minus Modular](https://arxiv.org/pdf/1910.05492)
- [AdaGATE](https://arxiv.org/abs/2605.05245)
- [ScalDPP](https://arxiv.org/abs/2604.03240)
- [Vendi-RAG](https://arxiv.org/abs/2502.11228)
- [LDAR (ICLR 2026)](https://arxiv.org/abs/2509.21865)
- [Context-Picker](https://arxiv.org/abs/2512.14465)
- [Sub-CP](https://arxiv.org/abs/2510.05130)
- [SMART-RAG](https://arxiv.org/pdf/2409.13992)
- [Submodular Optimization for Context Engineering (Jina)](https://jina.ai/news/submodular-optimization-for-text-selection-passage-reranking-context-engineering/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3502c9b8-75d8-43db-bfec-987297eb0381",
  "isSidechain": false,
  "requestId": "req_011CbYMTKPCzJKtBzkPLZXa6",
  "type": "assistant",
  "uuid": "6cc9403c-ea7a-4aea-8a6e-ac5062813b69",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MHv2Y4crhR5b6M32tRwjZM",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 630,
      "cache_read_input_tokens": 29206,
      "output_tokens": 5977,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 630,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5977,
          "cache_read_input_tokens": 29206,
          "cache_creation_input_tokens": 630,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 630
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

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition  ## Core Problem  How can post-retrieval context composition for RAG be formalized as a constrained non-monotone…",
  "leafUuid": "6cc9403c-ea7a-4aea-8a6e-ac5062813b69",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Non-monotone submodular context composition for RAG",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition  ## Core Problem  How can post-retrieval context composition for RAG be formalized as a constrained non-monotone…",
  "leafUuid": "6cc9403c-ea7a-4aea-8a6e-ac5062813b69",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Non-monotone submodular context composition for RAG",
  "sessionId": "ab11a6c4-93c1-47ad-ba1a-7958f9c0fef0"
}
```

---
