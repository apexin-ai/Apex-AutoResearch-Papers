# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Non-Monotone Submodular Context C

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/f8388054-0689-4dfc-afb2-fb54b0cc1bf6.jsonl`
- **Structured JSON:** [`0a1f4d1b8ed4c6f5e855.json`](../../sessions/0a/0a1f4d1b8ed4c6f5e855.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T07:35:29.636Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T07:35:29.636Z",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition\n\n## Core Problem\n\nHow can post-retrieval context composition for RAG be formalized as a constrained non-monotone submodular optimization problem that provably distinguishes between redundancy (intra-set semantic overlap) and distraction (answer-conditional interference) as separate penalty terms, yielding greedy approximation guarantees even when adding passages can decrease generation quality?\n\n## Broader Motivation\n\nThe problem of \"when does adding more information provably hurt?\" arises across context engineering: in-context learning (where Sub-CP, arXiv:2510.05130, applies submodular optimization to exemplar partitioning), tool-use composition, and multi-document grounding all exhibit non-monotone returns to context size. This work instantiates the question in RAG post-retrieval composition—including both single-hop and multi-hop QA—where it is most acute and empirically measurable, providing the first framework that decomposes the harm into redundancy and distraction with provable optimization guarantees.\n\n## Research Opportunity\n\nThree independently developed building blocks have converged but never been combined: (1) AdaGReS (arXiv Dec 2025) proved ε-approximate submodularity for redundancy-penalized context selection but only handles monotone objectives; (2) The Distracting Effect (ACL 2025) provides a concrete per-passage distraction measure DE_q(p) = 1−P(NO-RESPONSE|q,p) but performs no set-level optimization; (3) the AAMAS 2026 γ-weakly DR-submodular paper provides approximation guarantees Φ_γ for non-monotone objectives but has zero empirical applications to NLP.\n\nThe critical insight: subtracting a modular distraction penalty from AdaGReS's ε-approximately submodular objective makes the combined function non-monotone and non-submodular. The general problem class of maximizing \"approximately submodular minus modular\" functions has been studied theoretically (Qian, arXiv:1910.05492; Buchbinder et al., FOCS 2012 for the exact submodular case), but has never been instantiated in NLP or RAG. This work provides the first such instantiation, deriving the specific γ-weak DR-submodularity parameter for the RAG distraction-redundancy objective and empirically validating the AAMAS double-greedy framework in this domain.\n\n## Why Decompose Redundancy and Distraction?\n\nRedundancy and distraction damage generation quality through fundamentally different causal mechanisms, necessitating independent modeling:\n\n**Redundancy is an opportunity cost.** Repeated information wastes token budget, displacing other useful passages. Its harm is indirect—the model does not get confused by redundant content, but misses out on complementary evidence. Marginal harm diminishes: the n-th duplicate contributes less incremental information loss. This calls for a pairwise similarity penalty with diminishing marginal structure.\n\n**Distraction is an interference cost.** Irrelevant-but-plausible passages actively mislead the LLM's attention and reasoning, producing incorrect answers even when the gold passage is present. Its harm is direct and may compound: multiple distracting passages can reinforce a misleading narrative. This calls for a per-passage penalty tied to answer-conditional interference (DE_q).\n\nBecause these mechanisms have different scaling behavior and different causal pathways, a single penalty term cannot optimally control both. The decomposition into separate β (redundancy) and λ (distraction) hyperparameters allows independent calibration of each failure mode.\n\n## Research Landscape\n\nCurrent SOTA splits into two disjoint camps with a verified gap.\n\n**Camp 1 (formal guarantees, distraction-blind):** AdaGReS achieves ε-approximate submodularity with adaptive β* but only models redundancy, evaluated on 2 benchmarks. CCBQP (arXiv 2604.02554, Apr 2026) provides Frank-Wolfe with O(nd) iterations and landscape analysis via diagonal loading λ≥2, dominating MMR and DPP on the relevance-diversity Pareto frontier (QAMPARI/ASQA), but handles only relevance-diversity with no distraction term. Note that CCBQP's relevance weighting does not substitute for explicit distraction modeling: as shown in The Distracting Effect (ACL 2025), high-DE passages are often topically related to the query (moderate-to-high relevance) but answer-misleading—relevance-based weighting cannot distinguish these from genuinely helpful passages. SMART-RAG (arXiv:2409.13992, Sep 2024) uses DPP to jointly model relevance, diversity, and conflict (inter-passage contradiction), training-free, but \"conflict\" captures contradictory information between passages, not answer-conditional interference from individually misleading content. ScalDPP (arXiv:2604.03240, Apr 2026) scales DPP via P-Adapter with Diverse Margin Loss but remains in the relevance-diversity paradigm and requires training the P-Adapter.\n\n**Camp 2 (distraction-aware, no formal guarantees):** LDAR (ICLR 2026) is a distraction-aware retriever operating at retrieval time across 6 benchmarks but provides no post-retrieval composition or approximation bounds. DynamicRAG (NeurIPS 2025) uses RL with LLM feedback across 7 benchmarks but offers no optimization guarantees. Context-Picker (arXiv Dec 2025) uses two-stage RL for context selection across 5 benchmarks. Vendi-RAG (arXiv:2502.11228, Feb 2025) uses Vendi Score diversity + LLM judge for iterative diversity-quality optimization on multi-hop QA, but provides no formal guarantees and does not explicitly decompose redundancy from distraction. All learned approaches are distribution-dependent with no formal generalization guarantees under domain shift.\n\n**The gap:** No existing method is simultaneously post-retrieval, formally grounded with provable approximation bounds, and distraction-aware.\n\n## Addressing the Trivial Alternative\n\nA natural two-stage pipeline—first filter high-DE passages via threshold, then run AdaGReS's monotone greedy on survivors—appears to achieve both distraction-awareness and formal guarantees without new theory. Joint optimization is necessary because:\n\n**Pre-filtering forfeits optimality guarantees.** Removing passages before optimization shrinks the feasible set in a data-dependent, non-principled way. The resulting solution has no approximation guarantee relative to the optimal subset of the full candidate set. The joint formulation preserves the full candidate set and provides Φ_γ guarantees over it. A passage with high individual DE_q may still be the optimal choice when its relevance contribution outweighs the distraction cost in the joint objective—threshold filtering irrecoverably discards such passages.\n\nAs an empirical hypothesis, we additionally test whether set-level distraction interaction matters: the ablation includes a conditional DE_q(p|S\\{p}) variant to evaluate whether set-conditioned distraction scoring provides benefit beyond modular DE. The two-stage pipeline itself is included as an explicit ablation baseline (Ablation 7).\n\n## Proposed Approach\n\nDefine the set objective:\n\nf(S) = Σ_{p∈S} rel(q,p) − β·Σ_{p,p'∈S} sim(p,p') − λ·Σ_{p∈S} DE_q(p)\n\nwhere rel(q,p) is query-passage relevance (embedding cosine similarity), sim(p,p') is pairwise passage similarity (redundancy), and DE_q(p) is the per-passage Distracting Effect score (ACL 2025) computed via LLM no-response probability.\n\n**Why non-monotone:** The distraction penalty Σ DE_q(p) grows linearly with |S|. Beyond a critical set size, accumulated distraction cost overwhelms relevance gains, making f decrease with added passages. This non-monotonicity invalidates standard monotone greedy guarantees (AdaGReS).\n\n**Computational advantage of modular DE:** Since DE_q(p) depends only on the (q,p) pair, all DE scores can be pre-computed and cached before the greedy optimization begins. The DE computation cost is O(n) LLM calls (one per candidate passage), amortized across the optimization.\n\n**Theoretical contribution:** The relevance − redundancy component inherits AdaGReS's ε-approximate submodularity. Subtracting the modular distraction term yields a non-monotone, non-submodular function in the \"approximately submodular minus modular\" problem class (cf. Qian, arXiv:1910.05492). Our specific contribution is deriving the γ-weak DR-submodularity parameter for this RAG-specific objective under bounded-embedding conditions, enabling the AAMAS 2026 double-greedy framework with Φ_γ > γe^{−γ} approximation guarantee.\n\nThe bounded-embedding conditions require: (a) embedding norms bounded in [c_min, c_max] with c_min > 0; (b) the diminishing-return ratio of the relevance-redundancy component lower-bounded by γ > 0, which depends on the ratio c_min/c_max and the maximum pairwise similarity in the candidate set. When the candidate pool contains near-duplicate passages (sim ≈ 1), γ may degrade; we empirically measure γ on each benchmark and discuss graceful degradation.\n\n**γ as a diagnostic of composition difficulty.** Beyond its role as an algorithm parameter, γ encodes a structural property of the retrieval pool: it characterizes the gap between monotone greedy and non-monotone optimization for a given query's candidate set. When γ ≈ 1 (semantically diverse, low-redundancy pool), monotone greedy suffices and non-monotone optimization offers marginal gains. When γ ≪ 1 (high redundancy, high distraction), non-monotone optimization becomes essential. We empirically validate this by analyzing the correlation between per-query γ values and the accuracy improvement of our method over monotone baselines, establishing γ as a practical diagnostic for when sophisticated context composition is worthwhile.\n\n**Comparison with classical algorithms:** For exact non-monotone submodular functions, Buchbinder et al. (FOCS 2012) provide a 1/2-approximation via randomized double-greedy, tighter than AAMAS's Φ_γ when γ ≈ 1. Our empirically measured γ determines which framework is more appropriate. Both algorithms are included in the experimental comparison.\n\n## Experimental Design\n\n**Benchmarks:** Natural Questions (NQ), ASQA, QAMPARI, HotpotQA.\n\n**Metrics per benchmark:**\n- NQ: Exact Match (EM), token-level F1\n- ASQA: ROUGE-L, Disambig-F1 (D-F1), citation precision/recall (ALCE framework)\n- QAMPARI: Entity-level F1, entity recall\n- HotpotQA: EM, F1, supporting fact precision/recall\n- Cross-benchmark: tokens per query, wall-clock latency per query, redundancy ratio\n\n**Models:** Qwen3-Embedding-8B (retrieval + similarity), Qwen3-8B (DE scoring + secondary generator), Llama-4-Scout (primary generator).\n\n**Baselines (three groups):**\n- Simple heuristic: top-k, MMR\n- Formal optimization: AdaGReS, CCBQP, SMART-RAG\n- Learned: DynamicRAG, LDAR, Context-Picker, Vendi-RAG\n\n**LDAR comparison protocol:** Two settings: (a) Retrieval-controlled—all methods use Qwen3-Embedding-8B top-N candidates, comparing post-retrieval composition only; (b) End-to-end—LDAR uses its own retriever vs. proposed method with Qwen3-Embedding-8B + composition, comparing paradigms.\n\n**Ablation studies:**\n1. Component isolation: (a) f without distraction (= relevance − redundancy), (b) f without redundancy (= relevance − distraction), (c) full f → marginal contribution of each penalty\n2. Hyperparameter sensitivity: β × λ grid (5×5), Pareto surface\n3. Algorithm comparison: AAMAS double-greedy vs. Buchbinder et al. randomized double-greedy vs. standard greedy vs. random\n4. DE scoring model: Qwen3-8B DE vs. Llama-4-Scout self-DE → cross-model transferability\n5. Per-passage DE vs. conditional DE_q(p|S\\{p}): set-conditional scoring benefit vs. cost\n6. Selection set size k: impact on f and downstream accuracy\n7. Joint optimization vs. two-stage pipeline: DE threshold τ ∈ {0.3, 0.5, 0.7} filter → AdaGReS greedy vs. full joint optimization\n8. Cross-generator validation: full comparison on NQ + ASQA with Qwen3-8B as generator, for proposed method + AdaGReS + DynamicRAG\n9. Candidate pool size: top-50 / top-100 / top-200 → sensitivity and DE cost scaling\n\n**Domain-shift evaluation:** Train/tune learned baselines (DynamicRAG, Context-Picker) on one benchmark distribution, evaluate on a different benchmark. Proposed method uses identical hyperparameters across all benchmarks without retuning.\n\n**Compute-normalized comparison:** Decompose costs into three stages: (1) retrieval + embedding (shared); (2) selection/composition (DE pre-computation, optimization algorithm, reranking); (3) generation (variable token count from different selections). Plot accuracy-vs-selection-cost and accuracy-vs-total-cost Pareto curves. Provide concrete wall-clock estimates for DE pre-computation (Qwen3-8B throughput on target hardware).\n\n**Cross-model DE calibration:** On validation subsets, compute DE using both Qwen3-8B and Llama-4-Scout, report Spearman/Pearson correlation.\n\n**γ measurement and analysis:** Compute γ per-query as the minimum diminishing-return ratio over all passage subsets. Report distribution statistics (mean, std, min, percentiles) per benchmark. Analyze correlation between per-query γ and accuracy improvement over monotone baselines. Specifically examine γ behavior in high-redundancy multi-hop scenarios (HotpotQA) vs. single-hop (NQ).\n\n**Bounded-embedding verification:** Report embedding norm distributions and pairwise similarity statistics for Qwen3-Embedding-8B on each benchmark corpus.\n\n**Statistical rigor:** 3-5 independent runs per configuration, mean ± std, paired bootstrap significance tests.\n\n## Key References\n\n- AdaGReS: Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG (arXiv Dec 2025)\n- The Distracting Effect: Understanding Irrelevant Passages in RAG (ACL 2025)\n- Stronger Approximation Guarantees for Non-Monotone γ-Weakly DR-Submodular Maximization (AAMAS 2026)\n- Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming (arXiv 2604.02554, Apr 2026)\n- Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding (ICLR 2026)\n- DynamicRAG: Leveraging Outputs of LLM as Feedback for Dynamic Reranking in RAG (NeurIPS 2025)\n- Context-Picker: Dynamic Context Selection Using Multi-stage Reinforcement Learning (arXiv Dec 2025)\n- AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop RAG (arXiv May 2026)\n- SMART-RAG: Selection using Determinantal Matrices for Augmented Retrieval (arXiv:2409.13992, Sep 2024)\n- ScalDPP: Scaling DPPs for RAG — Density Meets Diversity (arXiv:2604.03240, Apr 2026)\n- Vendi-RAG: Adaptively Trading-Off Diversity and Quality (arXiv:2502.11228, Feb 2025)\n- Sub-CP: Submodular Context Partitioning for In-Context Learning (arXiv:2510.05130, Oct 2025)\n- Qian: Multi-objective Evolutionary Algorithms for Approximately Submodular Minus Modular (arXiv:1910.05492)\n- Buchbinder, Feldman, Naor, Schwartz: A Tight (1/2)-Approximation for Unconstrained Submodular Maximization (FOCS 2012)\n- ALCE: Enabling Large Language Models to Generate Text with Citations (Gao et al., EMNLP 2023)"
}
```

---

### Runtime record

_source line 2 · 2026-05-30T07:35:29.642Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T07:35:29.642Z",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6"
}
```

---

## Round 1

45 recorded events

### User

_source line 3 · 2026-05-30T07:35:29.657Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
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
  "promptId": "5f6b118c-9ebd-44f6-a29c-8cd2acf87653",
  "type": "user",
  "uuid": "db3c0fa0-55ed-4409-93f5-7cdc075cb539",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T07:35:29.656Z_

```json
{
  "parentUuid": "db3c0fa0-55ed-4409-93f5-7cdc075cb539",
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
  "uuid": "795bbb19-5d12-4540-988d-6134c5d402c5",
  "timestamp": "2026-05-30T07:35:29.656Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T07:35:29.656Z_

```json
{
  "parentUuid": "795bbb19-5d12-4540-988d-6134c5d402c5",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "79e0b7ff-987b-4c91-a4a2-5b42182b2c27",
  "timestamp": "2026-05-30T07:35:29.656Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition  ## Core Problem  How can…",
  "leafUuid": "79e0b7ff-987b-4c91-a4a2-5b42182b2c27",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Non-monotone submodular optimization for RAG context composition",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6"
}
```

---

### Assistant

_source line 8 · 2026-05-30T07:35:39.192Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for AAAI 2026 as the "出口评审 agent" (exit review agent). I need to:

1. First conduct thorough literature search using WebSearch
2. Then evaluate the proposal across 5 dimensions
3. Give probability estimates

Let me start by searching for the key topics in this proposal to understand the current landscape.

The proposal is about: Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition for RAG.

Key things to search:


1. AdaGReS and submodular optimization for RAG
2. Distracting Effect in RAG (ACL 2025)
3. Non-monotone submodular maximization in NLP
4. Post-retrieval context composition/selection for RAG
5. CCBQP and diversity-aware retrieval

Let me load WebSearch first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79e0b7ff-987b-4c91-a4a2-5b42182b2c27",
  "isSidechain": false,
  "requestId": "req_011CbYNKBNeLAXRLBGvDPccd",
  "type": "assistant",
  "uuid": "9b88767e-199e-49c3-a0db-16d75f6acbc3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HDY2Bgr4ReXW9QK4ujHwi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8020,
      "cache_read_input_tokens": 11014,
      "output_tokens": 301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8020,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 301,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 8020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8020
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

_source line 9 · 2026-05-30T07:35:39.203Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013TULTnpbb4gkMJwfpTZHqj`</summary>

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
  "parentUuid": "9b88767e-199e-49c3-a0db-16d75f6acbc3",
  "isSidechain": false,
  "requestId": "req_011CbYNKBNeLAXRLBGvDPccd",
  "type": "assistant",
  "uuid": "7c1141c4-06c4-45ed-96ad-a79003fcffee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017HDY2Bgr4ReXW9QK4ujHwi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8020,
      "cache_read_input_tokens": 11014,
      "output_tokens": 301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8020,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 301,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 8020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8020
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

_source line 10 · 2026-05-30T07:35:39.212Z_

<details><summary>↩ Tool result · `toolu_013TULTnpbb4gkMJwfpTZHqj`</summary>

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
  "parentUuid": "7c1141c4-06c4-45ed-96ad-a79003fcffee",
  "isSidechain": false,
  "promptId": "5f6b118c-9ebd-44f6-a29c-8cd2acf87653",
  "type": "user",
  "uuid": "d09472e1-2dbc-4f53-bdf3-fad8e23e2075",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "7c1141c4-06c4-45ed-96ad-a79003fcffee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-30T07:35:42.839Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me conduct the literature search. I need to search for:

1. AdaGReS submodular optimization RAG context selection
2. Distracting Effect RAG ACL 2025
3. Non-monotone submodular maximization NLP/RAG
4. Post-retrieval context composition RAG 2025 2026
5. CCBQP diversity-aware retrieval RAG

Let me run multiple searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d09472e1-2dbc-4f53-bdf3-fad8e23e2075",
  "isSidechain": false,
  "requestId": "req_011CbYNKtRhHKDih3f4bwQJY",
  "type": "assistant",
  "uuid": "b153a05b-69c2-4b89-a447-f94daa4f8da3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KBtnkQ9e6Vj8DaZHetj8vc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 19034,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 829,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 366,
          "cache_read_input_tokens": 19034,
          "cache_creation_input_tokens": 829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 829
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

_source line 12 · 2026-05-30T07:35:43.767Z_

I'll now conduct thorough literature searches to understand the current landscape before evaluating this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b153a05b-69c2-4b89-a447-f94daa4f8da3",
  "isSidechain": false,
  "requestId": "req_011CbYNKtRhHKDih3f4bwQJY",
  "type": "assistant",
  "uuid": "39f532a3-e390-4188-af98-6573121530bb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KBtnkQ9e6Vj8DaZHetj8vc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 19034,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 829,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 366,
          "cache_read_input_tokens": 19034,
          "cache_creation_input_tokens": 829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 829
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

_source line 13 · 2026-05-30T07:35:44.288Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UTaSj26H7RKT3vNfLQZhan`</summary>

```json
{
  "query": "AdaGReS adaptive greedy context selection submodular RAG redundancy 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39f532a3-e390-4188-af98-6573121530bb",
  "isSidechain": false,
  "requestId": "req_011CbYNKtRhHKDih3f4bwQJY",
  "type": "assistant",
  "uuid": "871d739a-6f11-4d27-b46d-ab126443fe99",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KBtnkQ9e6Vj8DaZHetj8vc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 19034,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 829,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 366,
          "cache_read_input_tokens": 19034,
          "cache_creation_input_tokens": 829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 829
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

_source line 14 · 2026-05-30T07:35:44.784Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JNFbQhBemXS48ERMn6yWQq`</summary>

```json
{
  "query": "Distracting Effect irrelevant passages RAG ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "871d739a-6f11-4d27-b46d-ab126443fe99",
  "isSidechain": false,
  "requestId": "req_011CbYNKtRhHKDih3f4bwQJY",
  "type": "assistant",
  "uuid": "7d8b1640-75af-4046-a82d-8e1b6fd560e8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KBtnkQ9e6Vj8DaZHetj8vc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 19034,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 829,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 366,
          "cache_read_input_tokens": 19034,
          "cache_creation_input_tokens": 829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 829
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

_source line 15 · 2026-05-30T07:35:45.283Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CF6bQo5CEkprnJBLVUQ4ES`</summary>

```json
{
  "query": "non-monotone submodular maximization weakly DR-submodular AAMAS 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d8b1640-75af-4046-a82d-8e1b6fd560e8",
  "isSidechain": false,
  "requestId": "req_011CbYNKtRhHKDih3f4bwQJY",
  "type": "assistant",
  "uuid": "6afca3e7-0c8f-44db-9d18-52ccfdb9ad51",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KBtnkQ9e6Vj8DaZHetj8vc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 19034,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 829,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 366,
          "cache_read_input_tokens": 19034,
          "cache_creation_input_tokens": 829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 829
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

_source line 16 · 2026-05-30T07:35:45.838Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lhhre3hbTxaBnNoMkni2Ga`</summary>

```json
{
  "query": "post-retrieval context selection composition RAG optimization 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6afca3e7-0c8f-44db-9d18-52ccfdb9ad51",
  "isSidechain": false,
  "requestId": "req_011CbYNKtRhHKDih3f4bwQJY",
  "type": "assistant",
  "uuid": "54448b3c-f5fe-44fd-ba66-09bde058a1c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KBtnkQ9e6Vj8DaZHetj8vc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 19034,
      "output_tokens": 366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 829,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 366,
          "cache_read_input_tokens": 19034,
          "cache_creation_input_tokens": 829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 829
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

_source line 17 · 2026-05-30T07:35:50.828Z_

<details><summary>↩ Tool result · `toolu_01UTaSj26H7RKT3vNfLQZhan`</summary>

```text
Web search results for query: "AdaGReS adaptive greedy context selection submodular RAG redundancy 2025"

Links: [{"title":"AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG","url":"https://arxiv.org/html/2512.25052"},{"title":"[2512.25052] AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG","url":"https://arxiv.org/abs/2512.25052"},{"title":"(PDF) AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG","url":"https://www.researchgate.net/publication/399276683_AdaGReSAdaptive_Greedy_Context_Selection_via_Redundancy-Aware_Scoring_for_Token-Budgeted_RAG"},{"title":"AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG","url":"https://arxiv.org/pdf/2512.25052"},{"title":"AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop Retrieval-Augmented Generation","url":"https://arxiv.org/html/2605.05245"}]

Based on the search results, I found relevant information about AdaGReS:

AdaGReS is a redundancy-aware context selection framework for token-budgeted RAG that optimizes a set-level objective combining query-chunk relevance and intra-set redundancy penalties. 

The framework performs greedy selection under a token-budget constraint using marginal gains derived from the objective, and introduces a closed-form, instance-adaptive calibration of the relevance–redundancy trade-off parameter to eliminate manual tuning and to adapt to candidate-pool statistics and budget limits.

The proposed objective exhibits epsilon-approximate submodularity under practical embedding similarity conditions, yielding near-optimality guarantees for greedy selection.

Experiments on open-domain question answering (Natural Questions) and a high-redundancy biomedical (drug) corpus demonstrate consistent improvements in redundancy control and context quality, translating to better end-to-end answer quality and robustness across settings.

The paper appears to have been published in December 2025, with the ArXiv identifier 2512.25052.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "871d739a-6f11-4d27-b46d-ab126443fe99",
  "isSidechain": false,
  "promptId": "5f6b118c-9ebd-44f6-a29c-8cd2acf87653",
  "type": "user",
  "uuid": "c940d1ec-1d98-4165-8e0b-e66ec32dc976",
  "toolUseResult": {
    "query": "AdaGReS adaptive greedy context selection submodular RAG redundancy 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_019uAwRfxn3RpyrPmEqzpaoa",
        "content": [
          {
            "title": "AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG",
            "url": "https://arxiv.org/html/2512.25052"
          },
          {
            "title": "[2512.25052] AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG",
            "url": "https://arxiv.org/abs/2512.25052"
          },
          {
            "title": "(PDF) AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG",
            "url": "https://www.researchgate.net/publication/399276683_AdaGReSAdaptive_Greedy_Context_Selection_via_Redundancy-Aware_Scoring_for_Token-Budgeted_RAG"
          },
          {
            "title": "AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG",
            "url": "https://arxiv.org/pdf/2512.25052"
          },
          {
            "title": "AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2605.05245"
          }
        ]
      },
      "Based on the search results, I found relevant information about AdaGReS:\n\nAdaGReS is a redundancy-aware context selection framework for token-budgeted RAG that optimizes a set-level objective combining query-chunk relevance and intra-set redundancy penalties. \n\nThe framework performs greedy selection under a token-budget constraint using marginal gains derived from the objective, and introduces a closed-form, instance-adaptive calibration of the relevance–redundancy trade-off parameter to eliminate manual tuning and to adapt to candidate-pool statistics and budget limits.\n\nThe proposed objective exhibits epsilon-approximate submodularity under practical embedding similarity conditions, yielding near-optimality guarantees for greedy selection.\n\nExperiments on open-domain question answering (Natural Questions) and a high-redundancy biomedical (drug) corpus demonstrate consistent improvements in redundancy control and context quality, translating to better end-to-end answer quality and robustness across settings.\n\nThe paper appears to have been published in December 2025, with the ArXiv identifier 2512.25052."
    ],
    "durationSeconds": 6.534156253999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "871d739a-6f11-4d27-b46d-ab126443fe99",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-30T07:35:51.533Z_

<details><summary>↩ Tool result · `toolu_01JNFbQhBemXS48ERMn6yWQq`</summary>

```text
Web search results for query: "Distracting Effect irrelevant passages RAG ACL 2025"

Links: [{"title":"The Distracting Effect: Understanding Irrelevant Passages in RAG (ACL 2025) - YouTube","url":"https://www.youtube.com/watch?v=BtLsxjA5D0A"},{"title":"The Distracting Effect: Understanding Irrelevant Passages in RAG - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.892/"},{"title":"RSTLess group on X: \"\"The Distracting Effect: Understanding Irrelevant Passages in RAG\" co-authored by @FlorinCuconasu was accepted at #ACL2025NLP main conference! This work analyzes how different types of distracting passages affect LLMs and achieves 7.5% accuracy gains via targeted fine-tuning.\" / X","url":"https://x.com/RSTLessGroup/status/1923374823595483384"},{"title":"The Distracting Effect: Understanding Irrelevant Passages in RAG","url":"https://arxiv.org/pdf/2505.06914"},{"title":"[2505.06914] The Distracting Effect: Understanding Irrelevant Passages in RAG","url":"https://arxiv.org/abs/2505.06914"},{"title":"The Distracting Effect: Understanding Irrelevant Passages in RAG","url":"https://arxiv.org/html/2505.06914v1"}]

I found research on "The Distracting Effect: Understanding Irrelevant Passages in RAG" accepted at ACL 2025. Here's what the paper is about:

## Overview

A well-known issue with Retrieval Augmented Generation (RAG) is that retrieved passages that are irrelevant to the query sometimes distract the answer-generating LLM, causing it to provide an incorrect response.

## Key Contributions

The paper provides a quantifiable measure of the distracting effect of a passage and demonstrates its robustness across LLMs. The contribution is two-fold: first, moving beyond the simple binary classification of irrelevant passages as either completely unrelated vs. distracting, and second, developing and analyzing multiple methods for finding hard distracting passages.

## Results

By fine-tuning LLMs with these carefully selected distracting passages, the research achieves up to a 7.5% increase in answering accuracy compared to counterparts fine-tuned on conventional RAG datasets. Additionally, higher-ranked passages consistently demonstrate greater potential to mislead the model.

The paper is available on arXiv (2505.06914) and the ACL Anthology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d8b1640-75af-4046-a82d-8e1b6fd560e8",
  "isSidechain": false,
  "promptId": "5f6b118c-9ebd-44f6-a29c-8cd2acf87653",
  "type": "user",
  "uuid": "b6110528-03af-4806-b842-cc962fc5d3ca",
  "toolUseResult": {
    "query": "Distracting Effect irrelevant passages RAG ACL 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AxzyoqwZkPt1Kec8mW9Gvf",
        "content": [
          {
            "title": "The Distracting Effect: Understanding Irrelevant Passages in RAG (ACL 2025) - YouTube",
            "url": "https://www.youtube.com/watch?v=BtLsxjA5D0A"
          },
          {
            "title": "The Distracting Effect: Understanding Irrelevant Passages in RAG - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.892/"
          },
          {
            "title": "RSTLess group on X: \"\"The Distracting Effect: Understanding Irrelevant Passages in RAG\" co-authored by @FlorinCuconasu was accepted at #ACL2025NLP main conference! This work analyzes how different types of distracting passages affect LLMs and achieves 7.5% accuracy gains via targeted fine-tuning.\" / X",
            "url": "https://x.com/RSTLessGroup/status/1923374823595483384"
          },
          {
            "title": "The Distracting Effect: Understanding Irrelevant Passages in RAG",
            "url": "https://arxiv.org/pdf/2505.06914"
          },
          {
            "title": "[2505.06914] The Distracting Effect: Understanding Irrelevant Passages in RAG",
            "url": "https://arxiv.org/abs/2505.06914"
          },
          {
            "title": "The Distracting Effect: Understanding Irrelevant Passages in RAG",
            "url": "https://arxiv.org/html/2505.06914v1"
          }
        ]
      },
      "I found research on \"The Distracting Effect: Understanding Irrelevant Passages in RAG\" accepted at ACL 2025. Here's what the paper is about:\n\n## Overview\n\nA well-known issue with Retrieval Augmented Generation (RAG) is that retrieved passages that are irrelevant to the query sometimes distract the answer-generating LLM, causing it to provide an incorrect response.\n\n## Key Contributions\n\nThe paper provides a quantifiable measure of the distracting effect of a passage and demonstrates its robustness across LLMs. The contribution is two-fold: first, moving beyond the simple binary classification of irrelevant passages as either completely unrelated vs. distracting, and second, developing and analyzing multiple methods for finding hard distracting passages.\n\n## Results\n\nBy fine-tuning LLMs with these carefully selected distracting passages, the research achieves up to a 7.5% increase in answering accuracy compared to counterparts fine-tuned on conventional RAG datasets. Additionally, higher-ranked passages consistently demonstrate greater potential to mislead the model.\n\nThe paper is available on arXiv (2505.06914) and the ACL Anthology."
    ],
    "durationSeconds": 6.745767861,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7d8b1640-75af-4046-a82d-8e1b6fd560e8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-30T07:35:52.398Z_

<details><summary>↩ Tool result · `toolu_01CF6bQo5CEkprnJBLVUQ4ES`</summary>

```text
Web search results for query: "non-monotone submodular maximization weakly DR-submodular AAMAS 2026"

Links: [{"title":"Stronger Approximation Guarantees for Non-Monotone 𝛾-Weakly DR-Submodular Maximization","url":"https://arxiv.org/html/2601.00611"},{"title":"Weakly DR-Submodular Maximization","url":"https://arxiv.org/pdf/2601.00611"},{"title":"[2601.00611] Stronger Approximation Guarantees for Non-Monotone γ-Weakly DR-Submodular Maximization","url":"https://arxiv.org/abs/2601.00611"},{"title":"Non-monotone DR-Submodular Function Maximization","url":"https://arxiv.org/pdf/1612.00960"},{"title":"Maximizing Non-Monotone DR-Submodular Functions with Cardinality   Constraints","url":"https://arxiv.org/pdf/1611.09474"},{"title":"Weakly Submodular Function Maximization Using Local Submodularity Ratio","url":"https://arxiv.org/pdf/2004.14650"},{"title":"DR-Submodular Maximization","url":"https://www.emergentmind.com/topics/dr-submodular-maximization"},{"title":"Regularized Unconstrained Weakly Submodular Maximization","url":"https://arxiv.org/pdf/2408.04620"}]

Based on the search results, I found a highly relevant paper on this topic:

The paper "Stronger Approximation Guarantees for Non-Monotone γ-Weakly DR-Submodular Maximization" will be presented at the International Conference on Autonomous Agents and Multiagent Systems (AAMAS) in May 2026.

The work studies the maximization of a nonnegative, non-monotone γ-weakly DR-submodular function over a down-closed convex body. The main result is an approximation algorithm whose guarantee depends smoothly on γ; when γ=1 (the DR-submodular case) the bound recovers the 0.401 approximation factor, while for γ<1 the guarantee degrades gracefully and improves upon previously reported bounds.

The approach combines a Frank-Wolfe-guided continuous-greedy framework with a γ-aware double-greedy step. γ-weakly DR-submodular objectives naturally arise when full DR-submodular models are augmented with practical penalties, and these augmentations retain the weak DR structure while inducing non-monotonicity.

The paper was posted to arXiv on January 2, 2026, and is authored by Hareshkumar Jadav, Ranveer Singh, and Vaneet Aggarwal.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6afca3e7-0c8f-44db-9d18-52ccfdb9ad51",
  "isSidechain": false,
  "promptId": "5f6b118c-9ebd-44f6-a29c-8cd2acf87653",
  "type": "user",
  "uuid": "19e271b1-3536-4c86-86b5-cbb180174b50",
  "toolUseResult": {
    "query": "non-monotone submodular maximization weakly DR-submodular AAMAS 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VU8AjreW9Jv4TUKCCy5hWN",
        "content": [
          {
            "title": "Stronger Approximation Guarantees for Non-Monotone 𝛾-Weakly DR-Submodular Maximization",
            "url": "https://arxiv.org/html/2601.00611"
          },
          {
            "title": "Weakly DR-Submodular Maximization",
            "url": "https://arxiv.org/pdf/2601.00611"
          },
          {
            "title": "[2601.00611] Stronger Approximation Guarantees for Non-Monotone γ-Weakly DR-Submodular Maximization",
            "url": "https://arxiv.org/abs/2601.00611"
          },
          {
            "title": "Non-monotone DR-Submodular Function Maximization",
            "url": "https://arxiv.org/pdf/1612.00960"
          },
          {
            "title": "Maximizing Non-Monotone DR-Submodular Functions with Cardinality   Constraints",
            "url": "https://arxiv.org/pdf/1611.09474"
          },
          {
            "title": "Weakly Submodular Function Maximization Using Local Submodularity Ratio",
            "url": "https://arxiv.org/pdf/2004.14650"
          },
          {
            "title": "DR-Submodular Maximization",
            "url": "https://www.emergentmind.com/topics/dr-submodular-maximization"
          },
          {
            "title": "Regularized Unconstrained Weakly Submodular Maximization",
            "url": "https://arxiv.org/pdf/2408.04620"
          }
        ]
      },
      "Based on the search results, I found a highly relevant paper on this topic:\n\nThe paper \"Stronger Approximation Guarantees for Non-Monotone γ-Weakly DR-Submodular Maximization\" will be presented at the International Conference on Autonomous Agents and Multiagent Systems (AAMAS) in May 2026.\n\nThe work studies the maximization of a nonnegative, non-monotone γ-weakly DR-submodular function over a down-closed convex body. The main result is an approximation algorithm whose guarantee depends smoothly on γ; when γ=1 (the DR-submodular case) the bound recovers the 0.401 approximation factor, while for γ<1 the guarantee degrades gracefully and improves upon previously reported bounds.\n\nThe approach combines a Frank-Wolfe-guided continuous-greedy framework with a γ-aware double-greedy step. γ-weakly DR-submodular objectives naturally arise when full DR-submodular models are augmented with practical penalties, and these augmentations retain the weak DR structure while inducing non-monotonicity.\n\nThe paper was posted to arXiv on January 2, 2026, and is authored by Hareshkumar Jadav, Ranveer Singh, and Vaneet Aggarwal."
    ],
    "durationSeconds": 7.112073712000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6afca3e7-0c8f-44db-9d18-52ccfdb9ad51",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-30T07:35:54.476Z_

<details><summary>↩ Tool result · `toolu_01Lhhre3hbTxaBnNoMkni2Ga`</summary>

```text
Web search results for query: "post-retrieval context selection composition RAG optimization 2025 2026"

Links: [{"title":"RAG Techniques Compared: A Practical Guide to Retrieval Augmented Generation in 2026","url":"https://blog.starmorph.com/blog/rag-techniques-compared-best-practices-guide"},{"title":"RAG in 2026: How Retrieval-Augmented Generation Works for Enterprise AI","url":"https://www.techment.com/blogs/rag-in-2026/"},{"title":"From RAG to Context - A 2025 year-end review of RAG | RAGFlow","url":"https://ragflow.io/blog/rag-review-2025-from-rag-to-context"},{"title":"In-Context Retrieval-Augmented Generation (RAG)","url":"https://www.emergentmind.com/topics/in-context-retrieval-augmented-generation-rag"},{"title":"AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG","url":"https://arxiv.org/pdf/2512.25052"},{"title":"RAG Is Not Dead: Advanced Retrieval Patterns That Actually Work in 2026 - DEV Community","url":"https://dev.to/young_gao/rag-is-not-dead-advanced-retrieval-patterns-that-actually-work-in-2026-2gbo"},{"title":"The 2025 Guide to Retrieval-Augmented Generation (RAG)","url":"https://www.edenai.co/post/the-2025-guide-to-retrieval-augmented-generation-rag"}]

Based on the search results, here's what I found about post-retrieval context selection and composition for RAG optimization in 2025-2026:

## Post-Retrieval Optimization Approaches

Advanced RAG wraps the naive pipeline with pre-retrieval and post-retrieval optimizations, with the core idea being to transform the query before retrieval and re-rank results after retrieval. The pipeline includes Context Selection as a key stage before the LLM generates responses.

## Key Techniques and Advances

Advanced retrieval stacks now include cross-encoders, multi-stage retrieval, and contextual filtering for higher precision. Hybrid retrieval and re-ranking together improve precision by 25-40% over naive RAG with relatively modest latency and cost increases.

## Recent Focus Areas (2025-2026)

Recent research has focused on shifting some responsibilities traditionally handled by retrievers to the generation model, applying reinforcement learning (RL) and curriculum learning, and leveraging diverse context composition and training objectives to improve faithfulness, scalability, and citation accuracy.

A persistent challenge is ensuring that retrieved results are not only highly relevant but also exhibit sufficient diversity in content, as systems tend to return overlapping or near-duplicate chunks under top-k retrieval.

## Production Maturity

60% of new RAG deployments in 2026 include systematic evaluation from day one, up from less than 30% in early 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54448b3c-f5fe-44fd-ba66-09bde058a1c9",
  "isSidechain": false,
  "promptId": "5f6b118c-9ebd-44f6-a29c-8cd2acf87653",
  "type": "user",
  "uuid": "60b70ac2-23fe-4096-b7ac-e43e678c219d",
  "toolUseResult": {
    "query": "post-retrieval context selection composition RAG optimization 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BzbfN2dG1vuqiHKtS8UvDT",
        "content": [
          {
            "title": "RAG Techniques Compared: A Practical Guide to Retrieval Augmented Generation in 2026",
            "url": "https://blog.starmorph.com/blog/rag-techniques-compared-best-practices-guide"
          },
          {
            "title": "RAG in 2026: How Retrieval-Augmented Generation Works for Enterprise AI",
            "url": "https://www.techment.com/blogs/rag-in-2026/"
          },
          {
            "title": "From RAG to Context - A 2025 year-end review of RAG | RAGFlow",
            "url": "https://ragflow.io/blog/rag-review-2025-from-rag-to-context"
          },
          {
            "title": "In-Context Retrieval-Augmented Generation (RAG)",
            "url": "https://www.emergentmind.com/topics/in-context-retrieval-augmented-generation-rag"
          },
          {
            "title": "AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG",
            "url": "https://arxiv.org/pdf/2512.25052"
          },
          {
            "title": "RAG Is Not Dead: Advanced Retrieval Patterns That Actually Work in 2026 - DEV Community",
            "url": "https://dev.to/young_gao/rag-is-not-dead-advanced-retrieval-patterns-that-actually-work-in-2026-2gbo"
          },
          {
            "title": "The 2025 Guide to Retrieval-Augmented Generation (RAG)",
            "url": "https://www.edenai.co/post/the-2025-guide-to-retrieval-augmented-generation-rag"
          }
        ]
      },
      "Based on the search results, here's what I found about post-retrieval context selection and composition for RAG optimization in 2025-2026:\n\n## Post-Retrieval Optimization Approaches\n\nAdvanced RAG wraps the naive pipeline with pre-retrieval and post-retrieval optimizations, with the core idea being to transform the query before retrieval and re-rank results after retrieval. The pipeline includes Context Selection as a key stage before the LLM generates responses.\n\n## Key Techniques and Advances\n\nAdvanced retrieval stacks now include cross-encoders, multi-stage retrieval, and contextual filtering for higher precision. Hybrid retrieval and re-ranking together improve precision by 25-40% over naive RAG with relatively modest latency and cost increases.\n\n## Recent Focus Areas (2025-2026)\n\nRecent research has focused on shifting some responsibilities traditionally handled by retrievers to the generation model, applying reinforcement learning (RL) and curriculum learning, and leveraging diverse context composition and training objectives to improve faithfulness, scalability, and citation accuracy.\n\nA persistent challenge is ensuring that retrieved results are not only highly relevant but also exhibit sufficient diversity in content, as systems tend to return overlapping or near-duplicate chunks under top-k retrieval.\n\n## Production Maturity\n\n60% of new RAG deployments in 2026 include systematic evaluation from day one, up from less than 30% in early 2025."
    ],
    "durationSeconds": 8.635867999999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "54448b3c-f5fe-44fd-ba66-09bde058a1c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition  ## Core Problem  How can…",
  "leafUuid": "60b70ac2-23fe-4096-b7ac-e43e678c219d",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Non-monotone submodular optimization for RAG context composition",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6"
}
```

---

### Assistant

_source line 23 · 2026-05-30T07:35:56.910Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have some initial results. Let me now search for more specific competing works mentioned in the proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60b70ac2-23fe-4096-b7ac-e43e678c219d",
  "isSidechain": false,
  "requestId": "req_011CbYNM1KxPBhEgD9v7tWMi",
  "type": "assistant",
  "uuid": "45c3e85b-c345-4d9e-8861-22f4fffafc75",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013SLWXwSmARFTre2LKbwvkP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3189,
      "cache_read_input_tokens": 19863,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 288,
          "cache_read_input_tokens": 19863,
          "cache_creation_input_tokens": 3189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3189
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

_source line 24 · 2026-05-30T07:35:57.406Z_

Good, let me search for more specific competing works and related methods.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45c3e85b-c345-4d9e-8861-22f4fffafc75",
  "isSidechain": false,
  "requestId": "req_011CbYNM1KxPBhEgD9v7tWMi",
  "type": "assistant",
  "uuid": "745ea5bd-a144-46f8-a887-017ec390d385",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013SLWXwSmARFTre2LKbwvkP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3189,
      "cache_read_input_tokens": 19863,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 288,
          "cache_read_input_tokens": 19863,
          "cache_creation_input_tokens": 3189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3189
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

_source line 25 · 2026-05-30T07:35:58.352Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R1C4inMPXGtCgCHG1zjEaj`</summary>

```json
{
  "query": "CCBQP cardinality-constrained binary quadratic programming diversity retrieval RAG 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "745ea5bd-a144-46f8-a887-017ec390d385",
  "isSidechain": false,
  "requestId": "req_011CbYNM1KxPBhEgD9v7tWMi",
  "type": "assistant",
  "uuid": "97af7687-0178-4dcc-ab6c-67d23a9f2bff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013SLWXwSmARFTre2LKbwvkP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3189,
      "cache_read_input_tokens": 19863,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 288,
          "cache_read_input_tokens": 19863,
          "cache_creation_input_tokens": 3189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3189
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

_source line 26 · 2026-05-30T07:35:59.296Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0137qYZ29RMkzQZxCnLRND6t`</summary>

```json
{
  "query": "DynamicRAG LLM feedback dynamic reranking NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97af7687-0178-4dcc-ab6c-67d23a9f2bff",
  "isSidechain": false,
  "requestId": "req_011CbYNM1KxPBhEgD9v7tWMi",
  "type": "assistant",
  "uuid": "94cc32d2-e757-4daa-a8d3-3c1592f7424d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013SLWXwSmARFTre2LKbwvkP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3189,
      "cache_read_input_tokens": 19863,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 288,
          "cache_read_input_tokens": 19863,
          "cache_creation_input_tokens": 3189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3189
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

_source line 27 · 2026-05-30T07:36:00.239Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JshQGMY9JKSJUssnkKBU4K`</summary>

```json
{
  "query": "LDAR distraction-aware retrieval ICLR 2026 knowledge grounding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94cc32d2-e757-4daa-a8d3-3c1592f7424d",
  "isSidechain": false,
  "requestId": "req_011CbYNM1KxPBhEgD9v7tWMi",
  "type": "assistant",
  "uuid": "177a234c-2818-4985-9442-aa13a1f9f124",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013SLWXwSmARFTre2LKbwvkP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3189,
      "cache_read_input_tokens": 19863,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 288,
          "cache_read_input_tokens": 19863,
          "cache_creation_input_tokens": 3189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3189
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

_source line 28 · 2026-05-30T07:36:00.642Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Vq3bqSKQQPqBkjDBy2DqDZ`</summary>

```json
{
  "query": "submodular optimization context selection NLP information retrieval 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "177a234c-2818-4985-9442-aa13a1f9f124",
  "isSidechain": false,
  "requestId": "req_011CbYNM1KxPBhEgD9v7tWMi",
  "type": "assistant",
  "uuid": "d458a447-f5e6-4cef-9f72-a827b41074d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013SLWXwSmARFTre2LKbwvkP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3189,
      "cache_read_input_tokens": 19863,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3189,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 288,
          "cache_read_input_tokens": 19863,
          "cache_creation_input_tokens": 3189,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3189
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

_source line 29 · 2026-05-30T07:36:04.903Z_

<details><summary>↩ Tool result · `toolu_0137qYZ29RMkzQZxCnLRND6t`</summary>

```text
Web search results for query: "DynamicRAG LLM feedback dynamic reranking NeurIPS 2025"

Links: [{"title":"DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation | OpenReview","url":"https://openreview.net/forum?id=NuCtKoflsV"},{"title":"GitHub - GasolSun36/DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation · GitHub","url":"https://github.com/GasolSun36/DynamicRAG"},{"title":"DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation","url":"https://arxiv.org/html/2505.07233v2"},{"title":"DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2505.07233"},{"title":"[2505.07233] DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2505.07233"},{"title":"DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation | Space Frontiers","url":"https://spacefrontiers.org/r/10.48550/arxiv.2505.07233"},{"title":"DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250507233S/abstract"},{"title":"NeurIPS Poster DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation","url":"https://neurips.cc/virtual/2025/poster/118330"},{"title":"Paper page - DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation","url":"https://huggingface.co/papers/2505.07233"}]

Based on the search results, I found detailed information about DynamicRAG and its NeurIPS 2025 presentation:

## Overview

DynamicRAG is a novel RAG framework where the reranker dynamically adjusts both the order and number of retrieved documents based on the query, and the paper was accepted as a NeurIPS 2025 poster.

## Key Technical Approach

The reranker dynamically adjusts both the order and number of retrieved documents based on the query, and is modeled as an agent optimized through reinforcement learning (RL), using rewards derived from LLM output quality.

## Problem Addressed

The challenge of selecting the optimal number of documents (k) remains unsolved: too few may omit critical information, while too many introduce noise and inefficiencies. Although recent studies have explored LLM-based rerankers, they primarily leverage internal model knowledge and overlook the rich supervisory signals that LLMs can provide, such as using response quality as feedback for optimizing reranking decisions.

## Results and Availability

Across seven knowledge-intensive datasets, DynamicRAG demonstrates superior performance, achieving state-of-the-art results. The paper was accepted by NeurIPS 2025, and the model, data and code are available at https://github.com/GasolSun36/DynamicRAG.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94cc32d2-e757-4daa-a8d3-3c1592f7424d",
  "isSidechain": false,
  "promptId": "5f6b118c-9ebd-44f6-a29c-8cd2acf87653",
  "type": "user",
  "uuid": "00d26a98-aaf5-4422-8b80-174e07b7cf40",
  "toolUseResult": {
    "query": "DynamicRAG LLM feedback dynamic reranking NeurIPS 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_019a4zfC4pZKZLmpPb26zxcd",
        "content": [
          {
            "title": "DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation | OpenReview",
            "url": "https://openreview.net/forum?id=NuCtKoflsV"
          },
          {
            "title": "GitHub - GasolSun36/DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation · GitHub",
            "url": "https://github.com/GasolSun36/DynamicRAG"
          },
          {
            "title": "DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2505.07233v2"
          },
          {
            "title": "DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2505.07233"
          },
          {
            "title": "[2505.07233] DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/abs/2505.07233"
          },
          {
            "title": "DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation | Space Frontiers",
            "url": "https://spacefrontiers.org/r/10.48550/arxiv.2505.07233"
          },
          {
            "title": "DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250507233S/abstract"
          },
          {
            "title": "NeurIPS Poster DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation",
            "url": "https://neurips.cc/virtual/2025/poster/118330"
          },
          {
            "title": "Paper page - DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation",
            "url": "https://huggingface.co/papers/2505.07233"
          }
        ]
      },
      "Based on the search results, I found detailed information about DynamicRAG and its NeurIPS 2025 presentation:\n\n## Overview\n\nDynamicRAG is a novel RAG framework where the reranker dynamically adjusts both the order and number of retrieved documents based on the query, and the paper was accepted as a NeurIPS 2025 poster.\n\n## Key Technical Approach\n\nThe reranker dynamically adjusts both the order and number of retrieved documents based on the query, and is modeled as an agent optimized through reinforcement learning (RL), using rewards derived from LLM output quality.\n\n## Problem Addressed\n\nThe challenge of selecting the optimal number of documents (k) remains unsolved: too few may omit critical information, while too many introduce noise and inefficiencies. Although recent studies have explored LLM-based rerankers, they primarily leverage internal model knowledge and overlook the rich supervisory signals that LLMs can provide, such as using response quality as feedback for optimizing reranking decisions.\n\n## Results and Availability\n\nAcross seven knowledge-intensive datasets, DynamicRAG demonstrates superior performance, achieving state-of-the-art results. The paper was accepted by NeurIPS 2025, and the model, data and code are available at https://github.com/GasolSun36/DynamicRAG."
    ],
    "durationSeconds": 5.603292428999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "94cc32d2-e757-4daa-a8d3-3c1592f7424d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-30T07:36:05.309Z_

<details><summary>↩ Tool result · `toolu_01R1C4inMPXGtCgCHG1zjEaj`</summary>

```text
Web search results for query: "CCBQP cardinality-constrained binary quadratic programming diversity retrieval RAG 2026"

Links: [{"title":"[2604.02554] Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming","url":"https://arxiv.org/abs/2604.02554"},{"title":"Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming","url":"https://arxiv.org/html/2604.02554"},{"title":"Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming","url":"https://arxiv.org/pdf/2604.02554"},{"title":"Scaling DPPs for RAG: Density Meets Diversity","url":"https://arxiv.org/pdf/2604.03240"},{"title":"Cardinality-Constrained Binary Quadratic Optimization via Extreme Point Pursuit, with Application to the Densest K-Subgraph Problem | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10447398/"}]

Based on the search results, I found relevant information about your query:

A principled formulation of diversity retrieval as cardinality-constrained binary quadratic programming (CCBQP) has been proposed, which explicitly balances relevance and semantic diversity through an interpretable trade-off parameter.

Diversity-aware retrieval is essential for Retrieval-Augmented Generation (RAG), yet existing methods lack theoretical guarantees and face scalability issues as the number of retrieved passages increases.

Recent advances in combinatorial optimization have led to the development of a non-convex tight continuous relaxation and a Frank-Wolfe based algorithm with landscape analysis and convergence guarantees. Experiments demonstrate that this method consistently dominates baselines on the relevance-diversity Pareto frontier, while achieving significant speedup.

This research was published as an arXiv paper (2604.02554) by Qiheng Lu from the University of Virginia on April 2, 2026, addressing the problem of balancing relevance and diversity in retrieval-augmented generation systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97af7687-0178-4dcc-ab6c-67d23a9f2bff",
  "isSidechain": false,
  "promptId": "5f6b118c-9ebd-44f6-a29c-8cd2acf87653",
  "type": "user",
  "uuid": "e0bf41b6-f1c4-4f19-91dc-d9a0dd77d43f",
  "toolUseResult": {
    "query": "CCBQP cardinality-constrained binary quadratic programming diversity retrieval RAG 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01595V2JJMNgqA3SikwrTjhL",
        "content": [
          {
            "title": "[2604.02554] Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming",
            "url": "https://arxiv.org/abs/2604.02554"
          },
          {
            "title": "Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming",
            "url": "https://arxiv.org/html/2604.02554"
          },
          {
            "title": "Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming",
            "url": "https://arxiv.org/pdf/2604.02554"
          },
          {
            "title": "Scaling DPPs for RAG: Density Meets Diversity",
            "url": "https://arxiv.org/pdf/2604.03240"
          },
          {
            "title": "Cardinality-Constrained Binary Quadratic Optimization via Extreme Point Pursuit, with Application to the Densest K-Subgraph Problem | IEEE Conference Publication | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/document/10447398/"
          }
        ]
      },
      "Based on the search results, I found relevant information about your query:\n\nA principled formulation of diversity retrieval as cardinality-constrained binary quadratic programming (CCBQP) has been proposed, which explicitly balances relevance and semantic diversity through an interpretable trade-off parameter.\n\nDiversity-aware retrieval is essential for Retrieval-Augmented Generation (RAG), yet existing methods lack theoretical guarantees and face scalability issues as the number of retrieved passages increases.\n\nRecent advances in combinatorial optimization have led to the development of a non-convex tight continuous relaxation and a Frank-Wolfe based algorithm with landscape analysis and convergence guarantees. Experiments demonstrate that this method consistently dominates baselines on the relevance-diversity Pareto frontier, while achieving significant speedup.\n\nThis research was published as an arXiv paper (2604.02554) by Qiheng Lu from the University of Virginia on April 2, 2026, addressing the problem of balancing relevance and diversity in retrieval-augmented generation systems."
    ],
    "durationSeconds": 6.952083973000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "97af7687-0178-4dcc-ab6c-67d23a9f2bff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-30T07:36:07.006Z_

<details><summary>↩ Tool result · `toolu_01JshQGMY9JKSJUssnkKBU4K`</summary>

```text
Web search results for query: "LDAR distraction-aware retrieval ICLR 2026 knowledge grounding"

Links: [{"title":"Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding","url":"https://arxiv.org/pdf/2509.21865"},{"title":"Downloads 2026","url":"https://iclr.cc/Downloads/2026"},{"title":"ICLR 2026 Workshops","url":"https://iclr.cc/virtual/2026/events/workshop"},{"title":"ICLR 2026 Schedule","url":"https://iclr.cc/virtual/2026/calendar"},{"title":"When RAG Hurts: Diagnosing and Mitigating Attention Distraction in Retrieval-Augmented LVLMs","url":"https://arxiv.org/pdf/2602.00344"},{"title":"The Distracting Effect: Understanding Irrelevant Passages in RAG","url":"https://arxiv.org/pdf/2505.06914"}]

Based on the search results, I found relevant information about LDAR and its ICLR 2026 presentation:

LDAR (Learning Distraction-Aware Retrieval) is an adaptive retriever that learns to retrieve contexts in a way that mitigates interference from distracting passages, thereby achieving significantly higher performance with reduced token usage compared to long-context approaches.

The approach addresses limitations including token inefficiency when handling large and potentially redundant contexts, the 'lost in the middle' phenomenon, and amplified distraction under limited model capacity that degrades LLM output quality.

Extensive experiments across diverse LLM architectures and six knowledge-intensive benchmarks demonstrate the effectiveness and robustness of the approach, highlighting the importance of balancing the trade-off between information coverage and distraction.

The paper titled "Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding" has been accepted to ICLR 2026, as indicated in the conference's downloads and schedule listings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "177a234c-2818-4985-9442-aa13a1f9f124",
  "isSidechain": false,
  "promptId": "5f6b118c-9ebd-44f6-a29c-8cd2acf87653",
  "type": "user",
  "uuid": "c0b1070f-16a5-4f4f-b608-e4a2ecc4da2d",
  "toolUseResult": {
    "query": "LDAR distraction-aware retrieval ICLR 2026 knowledge grounding",
    "results": [
      {
        "tool_use_id": "srvtoolu_018BzQx3wkBRpczVGj3YnyCM",
        "content": [
          {
            "title": "Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding",
            "url": "https://arxiv.org/pdf/2509.21865"
          },
          {
            "title": "Downloads 2026",
            "url": "https://iclr.cc/Downloads/2026"
          },
          {
            "title": "ICLR 2026 Workshops",
            "url": "https://iclr.cc/virtual/2026/events/workshop"
          },
          {
            "title": "ICLR 2026 Schedule",
            "url": "https://iclr.cc/virtual/2026/calendar"
          },
          {
            "title": "When RAG Hurts: Diagnosing and Mitigating Attention Distraction in Retrieval-Augmented LVLMs",
            "url": "https://arxiv.org/pdf/2602.00344"
          },
          {
            "title": "The Distracting Effect: Understanding Irrelevant Passages in RAG",
            "url": "https://arxiv.org/pdf/2505.06914"
          }
        ]
      },
      "Based on the search results, I found relevant information about LDAR and its ICLR 2026 presentation:\n\nLDAR (Learning Distraction-Aware Retrieval) is an adaptive retriever that learns to retrieve contexts in a way that mitigates interference from distracting passages, thereby achieving significantly higher performance with reduced token usage compared to long-context approaches.\n\nThe approach addresses limitations including token inefficiency when handling large and potentially redundant contexts, the 'lost in the middle' phenomenon, and amplified distraction under limited model capacity that degrades LLM output quality.\n\nExtensive experiments across diverse LLM architectures and six knowledge-intensive benchmarks demonstrate the effectiveness and robustness of the approach, highlighting the importance of balancing the trade-off between information coverage and distraction.\n\nThe paper titled \"Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding\" has been accepted to ICLR 2026, as indicated in the conference's downloads and schedule listings."
    ],
    "durationSeconds": 6.763647811999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "177a234c-2818-4985-9442-aa13a1f9f124",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-30T07:36:08.172Z_

<details><summary>↩ Tool result · `toolu_01Vq3bqSKQQPqBkjDBy2DqDZ`</summary>

```text
Web search results for query: "submodular optimization context selection NLP information retrieval 2024 2025 2026"

Links: [{"title":"Submodular Optimization for Text Selection, Passage Reranking & Context Engineering","url":"https://jina.ai/news/submodular-optimization-for-text-selection-passage-reranking-context-engineering/"},{"title":"Submodular Context Partitioning and Compression for In-Context Learning","url":"https://arxiv.org/pdf/2510.05130"},{"title":"Sub-SA: Strengthen In-context Learning via Submodular Selective   Annotation","url":"https://arxiv.org/pdf/2407.05693"},{"title":"InSQuAD: In-Context Learning for Efficient Retrieval via Submodular Mutual Information to Enforce Quality and Diversity","url":"https://arxiv.org/pdf/2508.21003"},{"title":"Submodlib: A Submodular Optimization Library","url":"https://arxiv.org/pdf/2202.10680"},{"title":"Optimizing Keyphrase Ranking for Relevance and Diversity Using   Submodular Function Optimization (SFO)","url":"https://arxiv.org/pdf/2410.20080"}]

I've completed the web search. Here are the results for your query on submodular optimization for context selection in NLP and information retrieval (2024-2026):

**Key Research Findings:**

1. **Submodular Context Partitioning (Sub-CP)** - A block-aware context selection framework that leverages submodular objectives to control the degree of diversity within each block, published in 2025. Extensive experiments across diverse tasks on multiple datasets show that Sub-CP consistently improves performance across model scales.

2. **Text Selection and Passage Reranking** - Submodular optimization is applied to context engineering through query fan-out, text selection, and passage reranking. This was discussed in a July 2025 article.

3. **Sub-SA: Submodular Selective Annotation** - A submodular function is designed that facilitates effective subset selection for annotation and demonstrates the characteristics of monotonicity and submodularity for improving in-context learning, published in 2024.

4. **InSQuAD** - Drawing on Submodular Mutual Information (SMI) functions, InSQuAD naturally incorporates Quality, Diversity, and Order among exemplars for in-context learning in information retrieval, published in 2025.

5. **Keyphrase Ranking** - A novel keyphrase ranking method that leverages submodular function optimization to balance relevance and diversity, published in 2024.

These recent works demonstrate the growing application of submodular optimization techniques for improving context selection, diversity handling, and selection tasks in NLP systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d458a447-f5e6-4cef-9f72-a827b41074d1",
  "isSidechain": false,
  "promptId": "5f6b118c-9ebd-44f6-a29c-8cd2acf87653",
  "type": "user",
  "uuid": "5fac736d-aeeb-41bd-b0c4-86a3c1f002fd",
  "toolUseResult": {
    "query": "submodular optimization context selection NLP information retrieval 2024 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CjgunRWd1VhJXD7isTe2iz",
        "content": [
          {
            "title": "Submodular Optimization for Text Selection, Passage Reranking & Context Engineering",
            "url": "https://jina.ai/news/submodular-optimization-for-text-selection-passage-reranking-context-engineering/"
          },
          {
            "title": "Submodular Context Partitioning and Compression for In-Context Learning",
            "url": "https://arxiv.org/pdf/2510.05130"
          },
          {
            "title": "Sub-SA: Strengthen In-context Learning via Submodular Selective   Annotation",
            "url": "https://arxiv.org/pdf/2407.05693"
          },
          {
            "title": "InSQuAD: In-Context Learning for Efficient Retrieval via Submodular Mutual Information to Enforce Quality and Diversity",
            "url": "https://arxiv.org/pdf/2508.21003"
          },
          {
            "title": "Submodlib: A Submodular Optimization Library",
            "url": "https://arxiv.org/pdf/2202.10680"
          },
          {
            "title": "Optimizing Keyphrase Ranking for Relevance and Diversity Using   Submodular Function Optimization (SFO)",
            "url": "https://arxiv.org/pdf/2410.20080"
          }
        ]
      },
      "I've completed the web search. Here are the results for your query on submodular optimization for context selection in NLP and information retrieval (2024-2026):\n\n**Key Research Findings:**\n\n1. **Submodular Context Partitioning (Sub-CP)** - A block-aware context selection framework that leverages submodular objectives to control the degree of diversity within each block, published in 2025. Extensive experiments across diverse tasks on multiple datasets show that Sub-CP consistently improves performance across model scales.\n\n2. **Text Selection and Passage Reranking** - Submodular optimization is applied to context engineering through query fan-out, text selection, and passage reranking. This was discussed in a July 2025 article.\n\n3. **Sub-SA: Submodular Selective Annotation** - A submodular function is designed that facilitates effective subset selection for annotation and demonstrates the characteristics of monotonicity and submodularity for improving in-context learning, published in 2024.\n\n4. **InSQuAD** - Drawing on Submodular Mutual Information (SMI) functions, InSQuAD naturally incorporates Quality, Diversity, and Order among exemplars for in-context learning in information retrieval, published in 2025.\n\n5. **Keyphrase Ranking** - A novel keyphrase ranking method that leverages submodular function optimization to balance relevance and diversity, published in 2024.\n\nThese recent works demonstrate the growing application of submodular optimization techniques for improving context selection, diversity handling, and selection tasks in NLP systems."
    ],
    "durationSeconds": 7.525888424999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d458a447-f5e6-4cef-9f72-a827b41074d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-30T07:36:08.186Z_

```json
{
  "parentUuid": "5fac736d-aeeb-41bd-b0c4-86a3c1f002fd",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "9df7d677-926e-4105-8702-ee1fac33f793",
  "timestamp": "2026-05-30T07:36:08.186Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 34 · 2026-05-30T07:36:14.145Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have a solid foundation. Let me do one more round of searches to look at some key specifics I want to verify - particularly around Vendi-RAG, Context-Picker, and whether there are any existing works that combine submodular optimization with distraction awareness in RAG.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9df7d677-926e-4105-8702-ee1fac33f793",
  "isSidechain": false,
  "requestId": "req_011CbYNN1wwcd1hBDnEBJMpk",
  "type": "assistant",
  "uuid": "8f1adcb4-2c28-48bd-9d04-a62208e9d2b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zA9T71noGi63d2eWzdhzq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3161,
      "cache_read_input_tokens": 23052,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3161,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 213,
          "cache_read_input_tokens": 23052,
          "cache_creation_input_tokens": 3161,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3161
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

_source line 35 · 2026-05-30T07:36:14.342Z_

Let me do one more round of targeted searches to complete the picture.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f1adcb4-2c28-48bd-9d04-a62208e9d2b0",
  "isSidechain": false,
  "requestId": "req_011CbYNN1wwcd1hBDnEBJMpk",
  "type": "assistant",
  "uuid": "31ac087c-aaf5-4fe7-b046-54a728a5742a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zA9T71noGi63d2eWzdhzq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3161,
      "cache_read_input_tokens": 23052,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3161,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 213,
          "cache_read_input_tokens": 23052,
          "cache_creation_input_tokens": 3161,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3161
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

_source line 36 · 2026-05-30T07:36:14.479Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GmZdd8VEUY1DArojXv8FfA`</summary>

```json
{
  "query": "Vendi-RAG diversity quality trading off multi-hop QA 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31ac087c-aaf5-4fe7-b046-54a728a5742a",
  "isSidechain": false,
  "requestId": "req_011CbYNN1wwcd1hBDnEBJMpk",
  "type": "assistant",
  "uuid": "1e2f4f49-2413-4e2e-b208-842f6276c7fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zA9T71noGi63d2eWzdhzq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3161,
      "cache_read_input_tokens": 23052,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3161,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 213,
          "cache_read_input_tokens": 23052,
          "cache_creation_input_tokens": 3161,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3161
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

_source line 37 · 2026-05-30T07:36:15.239Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013PLVahdFFV2NwNcbh7hfHR`</summary>

```json
{
  "query": "\"approximately submodular minus modular\" optimization Qian evolutionary 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e2f4f49-2413-4e2e-b208-842f6276c7fd",
  "isSidechain": false,
  "requestId": "req_011CbYNN1wwcd1hBDnEBJMpk",
  "type": "assistant",
  "uuid": "f27ed90c-2ae0-465c-adfd-6211e58e6180",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013zA9T71noGi63d2eWzdhzq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3161,
      "cache_read_input_tokens": 23052,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3161,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 213,
          "cache_read_input_tokens": 23052,
          "cache_creation_input_tokens": 3161,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3161
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

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition  ## Core Problem  How can…",
  "leafUuid": "f27ed90c-2ae0-465c-adfd-6211e58e6180",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Non-monotone submodular optimization for RAG context composition",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6"
}
```

---

### Tool result

_source line 40 · 2026-05-30T07:36:19.699Z_

<details><summary>↩ Tool result · `toolu_013PLVahdFFV2NwNcbh7hfHR`</summary>

```text
Web search results for query: ""approximately submodular minus modular" optimization Qian evolutionary 2019"

Links: [{"title":"[1910.05492] Multi-objective Evolutionary Algorithms are Still Good: Maximizing Monotone Approximately Submodular Minus Modular Functions","url":"https://arxiv.org/abs/1910.05492"},{"title":"Maximizing Non-monotone/Non-submodular Functions by Multi-objective Evolutionary Algorithms | Request PDF","url":"https://www.researchgate.net/publication/321180686_Maximizing_Non-monotoneNon-submodular_Functions_by_Multi-objective_Evolutionary_Algorithms"},{"title":"On Maximizing the Difference Between an Approximately Submodular Function and a Linear Function Subject to a Matroid Constraint | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-030-92681-6_7"},{"title":"Maximizing Monotone Approximately Submodular Minus ...","url":"https://www.lamda.nju.edu.cn/qianc/ecj20-submodular-final.pdf"},{"title":"Multi-Objective Evolutionary Algorithms","url":"https://www.emergentmind.com/topics/multi-objective-evolutionary-algorithms"},{"title":"Multiobjective Evolutionary Algorithms Are Still Good: Maximizing Monotone Approximately Submodular Minus Modular Functions | Evolutionary Computation | MIT Press","url":"https://direct.mit.edu/evco/article/doi/10.1162/evco_a_00288/97355/Multi-objective-Evolutionary-Algorithms-are-Still"},{"title":"Multi-objective Evolutionary Algorithms are Still Good: Maximizing   Monotone Approximately Submodular Minus Modular Functions","url":"https://arxiv.org/pdf/1910.05492"},{"title":"[1711.07214] Maximizing Submodular or Monotone Approximately Submodular Functions by Multi-objective Evolutionary Algorithms","url":"https://arxiv.org/abs/1711.07214"}]

I found the paper you're looking for. The work is "Multi-objective Evolutionary Algorithms are Still Good: Maximizing Monotone Approximately Submodular Minus Modular Functions" by Chao Qian from the National Key Laboratory for Novel Software Technology at Nanjing University.

The paper studies the problem class of maximizing monotone approximately submodular minus modular functions (f = g - c) with a size constraint, where g is a non-negative monotone approximately submodular function and c is a non-negative modular function. The researchers prove that the GSEMO (a simple multi-objective evolutionary algorithm) can achieve the best-known polynomial-time approximation guarantee, with empirical studies on applications in Bayesian experimental design and directed vertex cover demonstrating the algorithm's performance.

The paper was originally posted on arXiv in October 2019 and was later published in the journal Evolutionary Computation in 2021.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f27ed90c-2ae0-465c-adfd-6211e58e6180",
  "isSidechain": false,
  "promptId": "5f6b118c-9ebd-44f6-a29c-8cd2acf87653",
  "type": "user",
  "uuid": "ba9b1ca8-8228-4c52-8dbe-1363cc5facfa",
  "toolUseResult": {
    "query": "\"approximately submodular minus modular\" optimization Qian evolutionary 2019",
    "results": [
      {
        "tool_use_id": "srvtoolu_01W3CJRjJ8WbFvySjnV2c1UH",
        "content": [
          {
            "title": "[1910.05492] Multi-objective Evolutionary Algorithms are Still Good: Maximizing Monotone Approximately Submodular Minus Modular Functions",
            "url": "https://arxiv.org/abs/1910.05492"
          },
          {
            "title": "Maximizing Non-monotone/Non-submodular Functions by Multi-objective Evolutionary Algorithms | Request PDF",
            "url": "https://www.researchgate.net/publication/321180686_Maximizing_Non-monotoneNon-submodular_Functions_by_Multi-objective_Evolutionary_Algorithms"
          },
          {
            "title": "On Maximizing the Difference Between an Approximately Submodular Function and a Linear Function Subject to a Matroid Constraint | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-3-030-92681-6_7"
          },
          {
            "title": "Maximizing Monotone Approximately Submodular Minus ...",
            "url": "https://www.lamda.nju.edu.cn/qianc/ecj20-submodular-final.pdf"
          },
          {
            "title": "Multi-Objective Evolutionary Algorithms",
            "url": "https://www.emergentmind.com/topics/multi-objective-evolutionary-algorithms"
          },
          {
            "title": "Multiobjective Evolutionary Algorithms Are Still Good: Maximizing Monotone Approximately Submodular Minus Modular Functions | Evolutionary Computation | MIT Press",
            "url": "https://direct.mit.edu/evco/article/doi/10.1162/evco_a_00288/97355/Multi-objective-Evolutionary-Algorithms-are-Still"
          },
          {
            "title": "Multi-objective Evolutionary Algorithms are Still Good: Maximizing   Monotone Approximately Submodular Minus Modular Functions",
            "url": "https://arxiv.org/pdf/1910.05492"
          },
          {
            "title": "[1711.07214] Maximizing Submodular or Monotone Approximately Submodular Functions by Multi-objective Evolutionary Algorithms",
            "url": "https://arxiv.org/abs/1711.07214"
          }
        ]
      },
      "I found the paper you're looking for. The work is \"Multi-objective Evolutionary Algorithms are Still Good: Maximizing Monotone Approximately Submodular Minus Modular Functions\" by Chao Qian from the National Key Laboratory for Novel Software Technology at Nanjing University.\n\nThe paper studies the problem class of maximizing monotone approximately submodular minus modular functions (f = g - c) with a size constraint, where g is a non-negative monotone approximately submodular function and c is a non-negative modular function. The researchers prove that the GSEMO (a simple multi-objective evolutionary algorithm) can achieve the best-known polynomial-time approximation guarantee, with empirical studies on applications in Bayesian experimental design and directed vertex cover demonstrating the algorithm's performance.\n\nThe paper was originally posted on arXiv in October 2019 and was later published in the journal Evolutionary Computation in 2021."
    ],
    "durationSeconds": 4.456645942000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f27ed90c-2ae0-465c-adfd-6211e58e6180",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-30T07:36:21.805Z_

<details><summary>↩ Tool result · `toolu_01GmZdd8VEUY1DArojXv8FfA`</summary>

```text
Web search results for query: "Vendi-RAG diversity quality trading off multi-hop QA 2025"

Links: [{"title":"[2502.11228] Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs","url":"https://arxiv.org/abs/2502.11228"},{"title":"(PDF) Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs","url":"https://www.researchgate.net/publication/389090989_Vendi-RAG_Adaptively_Trading-Off_Diversity_And_Quality_Significantly_Improves_Retrieval_Augmented_Generation_With_LLMs"},{"title":"Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs","url":"https://arxiv.org/html/2502.11228v2"},{"title":"[Literature Review] Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs","url":"https://www.themoonlight.io/en/review/vendi-rag-adaptively-trading-off-diversity-and-quality-significantly-improves-retrieval-augmented-generation-with-llms"},{"title":"Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs | Papers With Code","url":"https://paperswithcode.com/paper/vendi-rag-adaptively-trading-off-diversity"},{"title":"dblp: Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs.","url":"https://dblp.org/rec/journals/corr/abs-2502-11228.html"},{"title":"Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs | Article Information | J-GLOBAL","url":"https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=202502218784102922"}]

Based on the search results, here's what I found about Vendi-RAG:

## Overview

Vendi-RAG is a framework based on an iterative process that jointly optimizes retrieval diversity and answer quality, leading to significantly higher accuracy for multi-hop QA tasks.

## The Problem It Addresses

Traditional RAG systems primarily focus on relevance-based retrieval and often struggle with redundancy, especially when reasoning requires connecting information from multiple sources.

## How It Works

Vendi-RAG leverages the Vendi Score (VS), a flexible similarity-based diversity metric, to promote semantic diversity in document retrieval. It then uses an LLM judge that evaluates candidate answers, generated after a reasoning step, and outputs a score that the retriever uses to balance relevance and diversity among the retrieved documents during each iteration.

## Performance Results

The framework achieves significant accuracy improvements over traditional single-step and multi-step RAG approaches, with accuracy increases reaching up to +4.2% on HotpotQA, +4.1% on 2WikiMultiHopQA, and +1.3% on MuSiQue compared to Adaptive-RAG, the current best baseline.

The benefits of Vendi-RAG are even more pronounced as the number of retrieved documents increases.

The paper was published on arXiv in February 2025 by Mohammad Reza Rezaei and Adji Bousso Dieng.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e2f4f49-2413-4e2e-b208-842f6276c7fd",
  "isSidechain": false,
  "promptId": "5f6b118c-9ebd-44f6-a29c-8cd2acf87653",
  "type": "user",
  "uuid": "355f132a-0fad-459e-8bd4-a91883890164",
  "toolUseResult": {
    "query": "Vendi-RAG diversity quality trading off multi-hop QA 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JM31vWpsqWULe1syhTFewd",
        "content": [
          {
            "title": "[2502.11228] Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs",
            "url": "https://arxiv.org/abs/2502.11228"
          },
          {
            "title": "(PDF) Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs",
            "url": "https://www.researchgate.net/publication/389090989_Vendi-RAG_Adaptively_Trading-Off_Diversity_And_Quality_Significantly_Improves_Retrieval_Augmented_Generation_With_LLMs"
          },
          {
            "title": "Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs",
            "url": "https://arxiv.org/html/2502.11228v2"
          },
          {
            "title": "[Literature Review] Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs",
            "url": "https://www.themoonlight.io/en/review/vendi-rag-adaptively-trading-off-diversity-and-quality-significantly-improves-retrieval-augmented-generation-with-llms"
          },
          {
            "title": "Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs | Papers With Code",
            "url": "https://paperswithcode.com/paper/vendi-rag-adaptively-trading-off-diversity"
          },
          {
            "title": "dblp: Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs.",
            "url": "https://dblp.org/rec/journals/corr/abs-2502-11228.html"
          },
          {
            "title": "Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs | Article Information | J-GLOBAL",
            "url": "https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=202502218784102922"
          }
        ]
      },
      "Based on the search results, here's what I found about Vendi-RAG:\n\n## Overview\n\nVendi-RAG is a framework based on an iterative process that jointly optimizes retrieval diversity and answer quality, leading to significantly higher accuracy for multi-hop QA tasks.\n\n## The Problem It Addresses\n\nTraditional RAG systems primarily focus on relevance-based retrieval and often struggle with redundancy, especially when reasoning requires connecting information from multiple sources.\n\n## How It Works\n\nVendi-RAG leverages the Vendi Score (VS), a flexible similarity-based diversity metric, to promote semantic diversity in document retrieval. It then uses an LLM judge that evaluates candidate answers, generated after a reasoning step, and outputs a score that the retriever uses to balance relevance and diversity among the retrieved documents during each iteration.\n\n## Performance Results\n\nThe framework achieves significant accuracy improvements over traditional single-step and multi-step RAG approaches, with accuracy increases reaching up to +4.2% on HotpotQA, +4.1% on 2WikiMultiHopQA, and +1.3% on MuSiQue compared to Adaptive-RAG, the current best baseline.\n\nThe benefits of Vendi-RAG are even more pronounced as the number of retrieved documents increases.\n\nThe paper was published on arXiv in February 2025 by Mohammad Reza Rezaei and Adji Bousso Dieng."
    ],
    "durationSeconds": 7.321554279000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1e2f4f49-2413-4e2e-b208-842f6276c7fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-30T07:37:09.652Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture of the landscape. Let me synthesize my findings and provide the evaluation.

Let me organize my thoughts:

**What the proposal is doing:**
The proposal formalizes post-retrieval context composition for RAG as a constrained non-monotone submodular optimization problem. It combines:
1. AdaGReS's ε-approximately submodular relevance-redundancy objective
2. The Distracting Effect's per-passage distraction measure DE_q(p)
3. AAMAS 2026's γ-weakly DR-submodular approximation guarantees


The core contribution is positioning this as the first work to simultaneously decompose redundancy and distraction as separate penalty terms, provide provable approximation guarantees for non-monotone context composition in RAG, and bridge the gap between formal optimization approaches and distraction-aware methods.

**Evaluation:**

The research problem is well-identified—the observation that no existing method combines post-retrieval formalization, formal grounding, and distraction-awareness is compelling. The decomposition of redundancy versus distraction is clearly motivated with sound causal reasoning, and this represents a genuine gap in the literature. The method evaluation is underway.

The core innovation combines three existing building blocks, with novelty emerging from the specific combination, deriving the γ-weak DR-submodularity parameter for the RAG objective, and providing the first NLP instantiation of "approximately submodular minus modular." The theoretical contribution—deriving γ for this specific objective—is meaningful, though reviewers might question its depth if the derivation amounts to straightforward subtraction of a modular function from an approximately submodular one. The modular DE assumption (where distraction depends only on the query-passage pair, not the full set) is a simplification that could face scrutiny, though the authors acknowledge this with an ablation study. The two-stage pipeline alternative is well-addressed as a baseline comparison.

The method itself is a weighted combination of relevance, similarity, and distraction terms—a fairly standard objective form. The theoretical contribution lies in proving this falls into the γ-weakly DR-submodular class with approximation guarantees, though a reviewer might view this as applying known results rather than developing fundamentally new theory. However, the instantiation proves non-trivial: deriving the specific γ parameter, establishing that bounded-embedding conditions suffice, and providing the first empirical validation of this framework in NLP. I'd rate the innovation as moderately strong overall.

The experimental evaluation is impressively comprehensive, spanning four benchmarks, eight-plus baselines across three categories, and nine ablation studies. The LDAR comparison protocol thoughtfully separates retrieval-controlled from end-to-end evaluation, and the domain-shift analysis adds valuable robustness assessment.

Beyond that, the compute-normalized comparisons and γ measurement provide empirical grounding for the theory, while the statistical rigor—multiple runs with bootstrap tests—and cross-model DE calibration demonstrate careful methodology. This is genuinely one of the proposal's strongest components.

On feasibility, the main bottleneck is DE computation requiring O(n) LLM calls per query, which for 100-200 candidates is substantial but workable. All components rely on off-the-shelf models and standard algorithms with no training required, which aligns with the training-free advantage claim. The theoretical derivation of γ is clear enough to execute, so the primary risk remains the computational cost of scoring.

The writing itself is crisp—the gap identification is precise, the two-camp framing is compelling, and the trivial alternative section preemptively handles a major objection. Using γ as a diagnostic tool adds interpretability. Overall, the proposal identifies a genuine gap where no existing method combines post-retrieval filtering, formal grounding, and distraction awareness, backed by strong literature awareness and a thoughtful experimental plan. The main vulnerability is that reviewers might perceive the core method as incremental—essentially combining known components rather than introducing fundamentally new ideas. distraction penalty from a known submodular objective and applied a known algorithm."
- The theoretical contribution (deriving γ for this specific objective) might be seen as a straightforward application of AAMAS 2026 theory rather than new theory.
- The modular DE assumption might not hold in practice (set-level distraction interactions).
- DE computation adds significant cost; if the empirical gains are marginal, the cost-benefit may not be favorable.
- Experimental success depends heavily on whether the decomposition actually leads to significant improvements over simpler baselines.

**Probability estimation:**
This is a well-crafted proposal with a clear gap, solid theoretical framing, and comprehensive experiments. The main risk is perceived incrementality ("combination of three known pieces"). 

For AAAI:
- The theoretical angle (first NLP instantiation of approximately submodular minus modular) is interesting
- The practical relevance (RAG is very hot) helps
- The comprehensive experimental design is a strong point
- But the novelty might be questioned by theory-oriented reviewers

I'd estimate: 30-42%, median ~36%.

The proposal is solid and competitive, filling a genuine gap, though it faces the "combination paper" criticism that could undermine its novelty score. However, reconsidering more carefully: the gap is real and well-articulated, the theoretical contribution is non-trivial in deriving the specific γ parameter and establishing bounded-embedding conditions, the "γ as diagnostic" framing is genuinely novel, and the experimental design is exceptionally thorough. The training-free nature with guarantees is a particularly strong selling point that distinguishes this from incremental work.

Weighing against this: the objective function is straightforward, the algorithm comes from AAMAS 2026, and the distraction-elimination concept from ACL 2025 are both existing pieces. While their combination is novel in context, it might not feel sufficiently deep to overcome reviewer skepticism about combination papers. I'm settling on 30-42% with a median around 35-36%—it's a solid, competitive paper that could go either way depending on how individual reviewers view bridging work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "355f132a-0fad-459e-8bd4-a91883890164",
  "isSidechain": false,
  "requestId": "req_011CbYNP2CMGEfrH3si3QFiV",
  "type": "assistant",
  "uuid": "8ba8626d-dbc6-4c92-ba6f-2baa43e8cb7c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CBZcT3YUW5PvTbSb5Vuptz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 771,
      "cache_creation_input_tokens": 1155,
      "cache_read_input_tokens": 26213,
      "output_tokens": 6895,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1155,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 771,
          "output_tokens": 6895,
          "cache_read_input_tokens": 26213,
          "cache_creation_input_tokens": 1155,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1155
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

_source line 43 · 2026-05-30T07:39:08.196Z_

Now I have sufficient information to provide a comprehensive evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- [AdaGReS (arXiv:2512.25052)](https://arxiv.org/abs/2512.25052) (Dec 2025): 直接前驱工作。证明了relevance-redundancy目标的ε-近似子模性，在NQ和生物医学语料上验证了贪心选择的有效性。但仅处理单调目标，无distraction建模。本proposal的Camp 1核心组件。
- [The Distracting Effect (arXiv:2505.06914)](https://aclanthology.org/2025.acl-long.892/) (ACL 2025): 直接前驱工作。提出per-passage distraction度量DE_q(p)，证明不相关但看似合理的passage会主动误导LLM。通过fine-tuning实现7.5%精度提升，但无集合级优化。本proposal的Camp 2核心组件。
- [γ-Weakly DR-Submodular (arXiv:2601.00611)](https://arxiv.org/abs/2601.00611) (AAMAS 2026): 理论工具。提供非单调γ-弱DR-子模函数的double-greedy近似保证Φ_γ，γ=1时恢复0.401近似因子。纯理论工作，无NLP实证应用。本proposal的算法框架来源。
- [CCBQP (arXiv:2604.02554)](https://arxiv.org/abs/2604.02554) (Apr 2026): 最强竞争者之一。将diversity retrieval建模为CCBQP，Frank-Wolfe算法+landscape分析，在QAMPARI/ASQA上主导relevance-diversity Pareto前沿。但仅处理relevance-diversity，无distraction项。Proposal正确指出其relevance加权不能替代显式distraction建模。
- [DynamicRAG (arXiv:2505.07233)](https://openreview.net/forum?id=NuCtKoflsV) (NeurIPS 2025): 基于RL的动态reranking，跨7个数据集SOTA。但无优化保证，分布依赖性强。Proposal的Camp 2 baseline。
- [LDAR (arXiv:2509.21865)](https://arxiv.org/pdf/2509.21865) (ICLR 2026): Distraction-aware retriever，在retrieval阶段操作，跨6个benchmark验证。但非post-retrieval组合，无近似保证。Proposal设计了两种对比协议（retrieval-controlled + end-to-end），考虑周全。
- [Vendi-RAG (arXiv:2502.11228)](https://arxiv.org/abs/2502.11228) (Feb 2025): 基于Vendi Score的diversity-quality迭代优化，在多跳QA上+4.2%。无formal guarantees，未显式分解redundancy与distraction。
- [Qian (arXiv:1910.05492)](https://arxiv.org/abs/1910.05492) (2019/ECJ 2021): "approximately submodular minus modular"问题类的理论分析，证明GSEMO的近似保证。本proposal所实例化的问题类的理论基础，但从未在NLP/RAG中实例化。
- [Sub-CP (arXiv:2510.05130)](https://arxiv.org/pdf/2510.05130) (Oct 2025): 子模优化用于ICL的exemplar选择，验证了子模框架在NLP context selection中的有效性。
- [Jina AI blog on Submodular Optimization for Context Engineering](https://jina.ai/news/submodular-optimization-for-text-selection-passage-reranking-context-engineering/) (Jul 2025): 工业界对子模优化用于context engineering的综述，验证了这一方向的实际关注度。

- **调研总结**: RAG post-retrieval context composition领域明确分裂为"有形式化保证但忽视distraction"和"distraction-aware但无形式化保证"两个阵营。该proposal精准识别了这一gap，且所引用的三个building block（AdaGReS、DE measure、AAMAS double-greedy）均已被独立验证。领域内尚无工作同时满足post-retrieval + formally grounded + distraction-aware三个条件，gap确实存在。CCBQP和ScalDPP是最近期的formal optimization竞争者，但均限于relevance-diversity范式。

【整体印象】: 
作为审稿人，第一反应是这是一篇**构思精巧、gap识别极其清晰的bridging paper**。它不是在已有方向上做增量改进，而是识别了两个独立发展的阵营之间的确切空白，并提出了一个理论上有根据的桥接方案。proposal的写作质量极高，论证逻辑严密，实验设计堪称教科书级别。

倾向：**weak accept**。主要的犹豫在于：核心贡献是否足够"深"——objective function形式（Σrel - β·Σsim - λ·ΣDE）本身较为直观，理论贡献的核心（推导特定于RAG的γ参数）可能被认为是AAMAS 2026框架的直接应用而非独立理论创新。但gap的真实性、分解的因果动机、和实验设计的完整性综合来看，这应该是一篇有竞争力的投稿。

【核心贡献】: 
1. **首次将RAG post-retrieval composition形式化为非单调子模优化问题**，显式分解redundancy（机会成本）和distraction（干扰成本）为独立惩罚项，具有清晰的因果机制区分。
2. **首次在NLP/RAG中实例化"approximately submodular minus modular"问题类**，推导了bounded-embedding条件下的γ-弱DR-子模性参数，实现AAMAS double-greedy框架的可证明近似保证。
3. **γ作为context composition难度的诊断指标**——这是一个有实际价值的副产品，可以指导何时需要复杂的非单调优化vs.简单贪心。

对领域的价值：中等偏高。这个工作如果实验验证成功，将为RAG context composition提供第一个同时具备formal guarantees和distraction-awareness的框架。对于要求可解释性和可靠性的应用场景（如医疗、法律RAG），这种形式化保证尤其有价值。

【方法合理性】: 
方法在逻辑上是合理的。三个组件（relevance-redundancy from AdaGReS, DE measure from ACL 2025, double-greedy from AAMAS 2026）的组合有清晰的理论基础。

**关键假设的合理性:**
- **DE的模块性假设**（DE_q(p)仅依赖(q,p)对）：这是一个合理的简化。虽然集合级distraction交互可能存在（如多个misleading passages强化错误叙事），但proposal明智地将此作为ablation（Ablation 5: conditional DE）而非核心假设的修改。
- **Bounded-embedding条件**：要求embedding norms有界、c_min > 0，这在使用normalized embeddings的现代模型中是自然满足的。

**更简单的替代方案:**
- **两阶段pipeline**（DE阈值过滤 → AdaGReS贪心）：proposal已主动讨论并作为Ablation 7，论证了联合优化的理论优势（保留完整可行集的近似保证）。这是非常好的预防性写作。
- **MMR + DE后过滤**：更简单但无形式化保证。
- **直接用DynamicRAG/Context-Picker的RL方法**：经验性能可能更好但无保证，且分布依赖。

方法的主要风险在于：当γ值在实际数据上退化（如高冗余候选池中γ ≪ 1）时，Φ_γ保证可能变得trivially weak，此时形式化保证的实际价值降低。Proposal承认了这一点并计划实证测量γ分布。

【5 维度打分】:
  1. 研究问题: 【强】 — 问题定义精准，gap identification是这篇proposal最强的部分。"no existing method is simultaneously post-retrieval, formally grounded, and distraction-aware"这一声明经调研验证属实。CCBQP（Apr 2026）和LDAR（ICLR 2026）是最新竞争者，但前者无distraction项，后者非post-retrieval且无形式化保证。Redundancy与distraction的因果机制分解（机会成本vs.干扰成本）有清晰的认知科学/信息论动机。研究问题对RAG领域有明确的理论和实践价值。

  2. 方法与创新: 【中】 — 核心objective f(S) = Σrel - β·Σsim - λ·ΣDE形式较为直观，是三个已有组件的加权组合。理论贡献（推导γ）的深度取决于推导的技术难度——如果bounded-embedding条件下γ的推导是straightforward的（从AdaGReS的ε-近似子模性直接减去模块函数），reviewers可能认为这是AAMAS 2026框架的routine application。与Qian (2019)的"approximately submodular minus modular"问题类的联系是一个有价值的理论定位，但本文是instantiation而非extension。γ-as-diagnostic是一个genuinely novel的conceptual contribution，但需要实证验证。与CCBQP对比：CCBQP的Frank-Wolfe + landscape analysis在技术深度上可能更强；与DynamicRAG对比：后者虽无保证但RL优化可能在实践中更强。创新的主要价值在于bridging两个阵营，而非任何单一组件的突破。

  3. 实验设计: 【强】 — 这是proposal最突出的亮点之一。4个benchmarks（NQ, ASQA, QAMPARI, HotpotQA）覆盖单跳、多跳、长形式、多实体QA。8+ baselines分三组（heuristic, formal optimization, learned），与CCBQP、SMART-RAG、ScalDPP等最新formal optimization方法以及DynamicRAG、LDAR等最新learned方法的全面对比。9个ablation studies系统性地验证每个设计决策。LDAR的dual-protocol对比设计（retrieval-controlled vs. end-to-end）非常thoughtful。Domain-shift evaluation、compute-normalized comparison、cross-model DE calibration、γ measurement and analysis、bounded-embedding verification——每一项都直接回应了可能的reviewer质疑。统计严谨性（3-5 runs, bootstrap tests）达标。唯一的小遗憾是没有提到human evaluation，但对于这类以自动指标为主的QA任务，这是可接受的。

  4. 可行性: 【强】 — 核心方法training-free，使用off-the-shelf模型（Qwen3系列, Llama-4-Scout）。DE计算O(n) LLM calls per query是主要计算开销，但可预计算和缓存。Double-greedy算法本身是多项式时间。不需要构建新benchmark、不需要训练新模型。主要资源需求：(1) DE预计算的LLM推理（Qwen3-8B，可在单GPU上运行）；(2) 8+个baseline的复现/运行；(3) 4个benchmark上的全面实验。这些都是一个2-3人团队在2-3个月内可完成的工作量。理论推导（γ的推导）的可行性取决于AAMAS 2026框架的技术细节，但从proposal的描述来看作者已经有了清晰的推导路径。

  5. 写作与呈现: 【强】 — Proposal的结构化程度和论证质量都很高。"Two camps" framing非常有效地传达了gap。"Why Decompose Redundancy and Distraction?"节的因果机制分析是说服力很强的论证。"Addressing the Trivial Alternative"节主动回应了最明显的反驳。"γ as diagnostic"的叙事增加了conceptual depth。文献引用全面且准确（经调研验证）。唯一的建议：正式论文中需要更紧凑——proposal中的许多细节（如9个ablation的完整列表）需要精简以适应8页限制。

【概率估计】: [28% - 40%] 中位 34%

【估计理由】: 
这篇proposal处于"solid but not spectacular"的区间。具体推理如下：

**上拉因素：**
- Gap identification极其清晰且经验证属实（+）
- 实验设计完备，远超平均proposal水平（+）
- Training-free + provable guarantees在RAG领域具有独特定位（+）
- RAG是当前AI热点方向，reviewer基数大且关注度高（+）
- 写作质量高，proactive defenses到位（+）
- 跨多个benchmark的全面验证计划（+）

**下拉因素：**
- 核心方法是三个已知组件的组合，novelty depth可能被质疑（−）
- 理论贡献可能被视为AAMAS 2026框架的routine instantiation（−）
- 形式化保证的实际意义取决于γ的实证值——如果γ ≪ 1，保证可能trivially weak（−）
- 经验性能是否真正优于DynamicRAG等RL方法尚未验证——formal guarantees在reviewer心中的权重可能低于实证SOTA（−）
- AAAI reviewer pool多样，可能遇到不重视理论保证或不熟悉子模优化的reviewer（−）

**定位对标：**
- 比纯incremental improvement强（30%基线以上）
- 但比提出genuinely新理论/新范式的工作弱（45%以上需要更强的novelty或surprising empirical results）
- 最终结果高度依赖于实验是否能展现显著且一致的改进，尤其是相对于两阶段pipeline和DynamicRAG

【主要风险】: 
1. **"Combination Paper"质疑**: 最大的拒稿风险。Reviewer可能指出：objective function是三个已知项的线性组合，算法是已有的double-greedy，DE measure是已有的——"what is genuinely new here?"。尽管proposal的论证（gap的存在、γ推导、首次NLP instantiation）是合理的，但如果遇到偏向deep novelty的reviewer，这一点可能成为致命伤。
2. **Formal guarantees vs. Empirical performance的张力**: 如果实验结果显示DynamicRAG或Context-Picker等RL方法在多数benchmark上仍然优于本方法，那么"provable guarantees"的卖点将大打折扣——reviewer会问"如果RL方法在实践中更好，形式化保证的价值在哪里？"。这是一个实验阶段才能回答的风险，但对中稿概率有重大影响。

【实施评估】:
  - 计算资源: 中等。DE预计算需要Qwen3-8B推理（O(n) calls/query, n=50-200），主生成需要Llama-4-Scout。单节点多GPU（2-4× A100/H100）即可。Baseline复现（DynamicRAG等RL方法）可能需要额外训练资源。
  - 数据需求: 低。所有benchmark（NQ, ASQA, QAMPARI, HotpotQA）均为公开数据集，无需新数据收集。
  - 人工介入: 极低。方法training-free，无需人工标注。仅需手动调参β×λ grid（已自动化）和结果分析。
  - 训练需求: 自身方法无训练。但baseline复现（DynamicRAG, Context-Picker的RL训练）需要训练资源。LDAR可能需要其distraction-aware retriever的训练。
  - 新 Benchmark: 不需要。使用现有benchmark。
  - 预估周期: 2-3个月。理论推导（γ derivation）~2-3周；DE预计算pipeline搭建~1-2周；实验（全benchmark × 全baseline × ablation）~4-6周；论文写作~2-3周。适合一个AAAI 2026的投稿周期。
```

Sources:
- [AdaGReS: Adaptive Greedy Context Selection](https://arxiv.org/abs/2512.25052)
- [The Distracting Effect: Understanding Irrelevant Passages in RAG (ACL 2025)](https://aclanthology.org/2025.acl-long.892/)
- [γ-Weakly DR-Submodular Maximization (AAMAS 2026)](https://arxiv.org/abs/2601.00611)
- [CCBQP: Diversity-Aware Retrieval via Binary Quadratic Programming](https://arxiv.org/abs/2604.02554)
- [DynamicRAG (NeurIPS 2025)](https://openreview.net/forum?id=NuCtKoflsV)
- [LDAR: Distraction-Aware Retrieval (ICLR 2026)](https://arxiv.org/pdf/2509.21865)
- [Vendi-RAG: Diversity and Quality Trading-Off](https://arxiv.org/abs/2502.11228)
- [Qian: Approximately Submodular Minus Modular](https://arxiv.org/abs/1910.05492)
- [Sub-CP: Submodular Context Partitioning](https://arxiv.org/pdf/2510.05130)
- [Jina AI: Submodular Optimization for Context Engineering](https://jina.ai/news/submodular-optimization-for-text-selection-passage-reranking-context-engineering/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ba8626d-dbc6-4c92-ba6f-2baa43e8cb7c",
  "isSidechain": false,
  "requestId": "req_011CbYNP2CMGEfrH3si3QFiV",
  "type": "assistant",
  "uuid": "288fcc77-df77-43c8-a5dc-a4eca5af063b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CBZcT3YUW5PvTbSb5Vuptz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 771,
      "cache_creation_input_tokens": 1155,
      "cache_read_input_tokens": 26213,
      "output_tokens": 6895,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1155,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 771,
          "output_tokens": 6895,
          "cache_read_input_tokens": 26213,
          "cache_creation_input_tokens": 1155,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1155
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

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition  ## Core Problem  How can…",
  "leafUuid": "288fcc77-df77-43c8-a5dc-a4eca5af063b",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Non-monotone submodular optimization for RAG context composition",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition  ## Core Problem  How can…",
  "leafUuid": "288fcc77-df77-43c8-a5dc-a4eca5af063b",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Non-monotone submodular optimization for RAG context composition",
  "sessionId": "f8388054-0689-4dfc-afb2-fb54b0cc1bf6"
}
```

---
