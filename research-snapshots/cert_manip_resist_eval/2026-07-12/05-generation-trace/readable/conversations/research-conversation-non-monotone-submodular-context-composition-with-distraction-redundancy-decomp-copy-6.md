# Research conversation: Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition ## Core Problem How can post-retri

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 58
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-3/f38fdf25-2bc6-4f3e-8501-0aa918175ef7.jsonl`
- **Structured JSON:** [`bb1b037c2050391eb7a1.json`](../../sessions/bb/bb1b037c2050391eb7a1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T07:11:09.290Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T07:11:09.290Z",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "content": "# Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition\n\n## Core Problem\n\nHow can post-retrieval context composition for RAG be formalized as a constrained non-monotone submodular optimization problem that provably distinguishes between redundancy (intra-set semantic overlap) and distraction (answer-conditional interference) as separate penalty terms, yielding greedy approximation guarantees even when adding passages can decrease generation quality?\n\n## Broader Motivation\n\nThe problem of \"when does adding more information provably hurt?\" arises across context engineering: in-context learning (where Sub-CP, arXiv:2510.05130, applies submodular optimization to exemplar partitioning), tool-use composition, and multi-document grounding all exhibit non-monotone returns to context size. This work instantiates the question in RAG post-retrieval composition, where it is most acute and empirically measurable, providing the first framework that decomposes the harm into redundancy and distraction with provable optimization guarantees.\n\n## Research Opportunity\n\nThree independently developed building blocks have converged but never been combined: (1) AdaGReS (arXiv Dec 2025) proved ε-approximate submodularity for redundancy-penalized context selection but only handles monotone objectives; (2) The Distracting Effect (ACL 2025) provides a concrete per-passage distraction measure DE_q(p) = 1−P(NO-RESPONSE|q,p) but performs no set-level optimization; (3) the AAMAS 2026 γ-weakly DR-submodular paper provides approximation guarantees Φ_γ for non-monotone objectives but has zero empirical applications to NLP.\n\nThe critical insight: subtracting a modular distraction penalty from AdaGReS's ε-approximately submodular objective makes the combined function non-monotone and non-submodular. The general problem class of maximizing \"approximately submodular minus modular\" functions has been studied theoretically (Qian, arXiv:1910.05492; Buchbinder et al., FOCS 2012 for the exact submodular case), but has never been instantiated in NLP or RAG. This work provides the first such instantiation, deriving the specific γ-weak DR-submodularity parameter for the RAG distraction-redundancy objective and empirically validating the AAMAS double-greedy framework in this domain.\n\n## Research Landscape\n\nCurrent SOTA splits into two disjoint camps with a verified gap.\n\n**Camp 1 (formal guarantees, distraction-blind):** AdaGReS achieves ε-approximate submodularity with adaptive β* but only models redundancy, evaluated on 2 benchmarks. CCBQP (arXiv 2604.02554, Apr 2026) provides Frank-Wolfe with O(nd) iterations and landscape analysis via diagonal loading λ≥2, dominating MMR and DPP on the relevance-diversity Pareto frontier (QAMPARI/ASQA), but handles only relevance-diversity with no distraction term. SMART-RAG (arXiv:2409.13992, Sep 2024) uses DPP to jointly model relevance, diversity, and conflict, training-free, but lacks distraction modeling and non-monotone optimization guarantees. ScalDPP (arXiv:2604.03240, Apr 2026) scales DPP via P-Adapter with Diverse Margin Loss but remains in the relevance-diversity paradigm.\n\n**Camp 2 (distraction-aware, no formal guarantees):** LDAR (ICLR 2026) is a distraction-aware retriever operating at retrieval time across 6 benchmarks but provides no post-retrieval composition or approximation bounds. DynamicRAG (NeurIPS 2025) uses RL with LLM feedback across 7 benchmarks but offers no optimization guarantees. Context-Picker (arXiv Dec 2025) uses two-stage RL for context selection across 5 benchmarks. Vendi-RAG (arXiv:2502.11228, Feb 2025) uses Vendi Score diversity + LLM judge for iterative diversity-quality optimization on multi-hop QA, but provides no formal guarantees and does not explicitly decompose redundancy from distraction. All learned approaches are distribution-dependent with no formal generalization guarantees under domain shift.\n\n**The gap:** No existing method is simultaneously post-retrieval, formally grounded with provable approximation bounds, and distraction-aware.\n\n## Addressing the Trivial Alternative\n\nA natural two-stage pipeline—first filter high-DE passages via threshold, then run AdaGReS's monotone greedy on survivors—appears to achieve both distraction-awareness and formal guarantees without new theory. Joint optimization is necessary for the following reason:\n\n**Pre-filtering forfeits optimality guarantees.** Removing passages before optimization shrinks the feasible set in a data-dependent, non-principled way. The resulting solution has no approximation guarantee relative to the optimal subset of the full candidate set. The joint formulation preserves the full candidate set and provides Φ_γ guarantees over it. A passage with high individual DE_q may still be the optimal choice when its relevance contribution outweighs the distraction cost in the joint objective—threshold filtering irrecoverably discards such passages.\n\nAdditionally, we treat set-level distraction interaction as an empirical hypothesis: while the base formulation uses modular (per-passage) DE for computational tractability, the ablation study includes a conditional DE_q(p|S\\{p}) variant to test whether set-conditioned distraction scoring provides additional benefit. If confirmed, this would constitute an additional empirical contribution beyond the formal optimization framework.\n\n## Proposed Approach\n\nDefine the set objective:\n\nf(S) = Σ_{p∈S} rel(q,p) − β·Σ_{p,p'∈S} sim(p,p') − λ·Σ_{p∈S} DE_q(p)\n\nwhere rel(q,p) is query-passage relevance (embedding cosine similarity), sim(p,p') is pairwise passage similarity (redundancy), and DE_q(p) is the per-passage Distracting Effect score (ACL 2025) computed via LLM no-response probability.\n\n**Why non-monotone:** The distraction penalty Σ DE_q(p) grows linearly with |S|. Beyond a critical set size, accumulated distraction cost overwhelms relevance gains, making f decrease with added passages. This non-monotonicity invalidates standard monotone greedy guarantees (AdaGReS).\n\n**Computational advantage of modular DE:** Since DE_q(p) depends only on the (q,p) pair, all DE scores can be pre-computed and cached before the greedy optimization begins. The DE computation cost is O(n) LLM calls (one per candidate passage), amortized across the optimization, rather than O(n·k) calls that a set-conditional formulation would require.\n\n**Theoretical contribution:** The relevance − redundancy component inherits AdaGReS's ε-approximate submodularity. Subtracting the modular distraction term yields a non-monotone, non-submodular function in the \"approximately submodular minus modular\" problem class (cf. Qian, arXiv:1910.05492). Our specific contribution is deriving the γ-weak DR-submodularity parameter for this RAG-specific objective under bounded-embedding conditions, enabling the AAMAS 2026 double-greedy framework with Φ_γ > γe^{−γ} approximation guarantee.\n\nThe bounded-embedding conditions require: (a) embedding norms bounded in [c_min, c_max] with c_min > 0; (b) pairwise cosine similarity curvature bounded—specifically, the diminishing-return ratio of the relevance-redundancy component must be lower-bounded by γ > 0, which depends on the ratio c_min/c_max and the maximum pairwise similarity in the candidate set. When the candidate pool contains near-duplicate passages (sim ≈ 1), γ may degrade; we empirically measure γ on each benchmark and discuss graceful degradation of the guarantee when γ is small.\n\n**Comparison with classical algorithms:** For exact non-monotone submodular functions, Buchbinder et al. (FOCS 2012) provide a 1/2-approximation via randomized double-greedy, which is tighter than AAMAS's Φ_γ when γ ≈ 1. Our empirically measured γ determines which framework is more appropriate. Both algorithms are included in the experimental comparison.\n\n## Experimental Design\n\n**Benchmarks:** Natural Questions (NQ), ASQA, QAMPARI.\n\n**Metrics per benchmark:**\n- NQ: Exact Match (EM), token-level F1\n- ASQA: ROUGE-L, Disambig-F1 (D-F1), citation precision/recall (ALCE framework)\n- QAMPARI: Entity-level F1, entity recall\n- Cross-benchmark: tokens per query, wall-clock latency per query, redundancy ratio\n\n**Models:** Qwen3-Embedding-8B (retrieval + similarity), Qwen3-8B (DE scoring), Llama-4-Scout (primary generator), Qwen3-8B (secondary generator for cross-generator validation on NQ).\n\n**Baselines (three groups):**\n- Simple heuristic: top-k, MMR\n- Formal optimization: AdaGReS, CCBQP, SMART-RAG\n- Learned: DynamicRAG, LDAR, Context-Picker\n\n**LDAR comparison protocol:** Two settings: (a) Retrieval-controlled—all methods use Qwen3-Embedding-8B top-100 candidates, comparing post-retrieval composition only (LDAR's post-retrieval component if applicable); (b) End-to-end—LDAR uses its own retriever vs. proposed method with Qwen3-Embedding-8B + composition, comparing paradigms (distraction-aware retrieval vs. distraction-aware composition).\n\n**Ablation studies:**\n1. Component isolation: (a) f without distraction (= AdaGReS-like), (b) f without redundancy, (c) full f → marginal contribution of each penalty\n2. Hyperparameter sensitivity: β × λ grid (5×5), Pareto surface\n3. Algorithm comparison: AAMAS double-greedy vs. Buchbinder et al. randomized double-greedy vs. standard greedy vs. random\n4. DE scoring model: Qwen3-8B DE vs. Llama-4-Scout self-DE → cross-model transferability\n5. Per-passage DE vs. conditional DE_q(p|S\\{p}): set-conditional scoring benefit vs. cost\n6. Selection set size k: impact on f and downstream accuracy\n7. Joint optimization vs. two-stage pipeline: DE threshold τ ∈ {0.3, 0.5, 0.7} filter → AdaGReS greedy vs. full joint optimization → validate necessity of joint approach\n8. Cross-generator validation: full baseline comparison on NQ with Qwen3-8B as generator\n\n**Domain-shift evaluation:** Train/tune learned baselines (DynamicRAG, Context-Picker) on one benchmark distribution, evaluate on a different benchmark. Proposed method uses identical hyperparameters across all benchmarks without retuning. This directly tests the claimed robustness advantage of formal guarantees over learned approaches under distribution shift.\n\n**Compute-normalized comparison:** Report per-query inference cost (LLM calls, total tokens, wall-clock time) for all methods. Plot accuracy-vs-compute Pareto curves. Explicitly report DE pre-computation cost as a separate line item.\n\n**Cross-model DE calibration:** On a validation subset, compute DE using both Qwen3-8B and Llama-4-Scout, report Spearman/Pearson correlation.\n\n**Bounded-embedding verification:** Report embedding norm distributions and pairwise similarity statistics for Qwen3-Embedding-8B on each benchmark. Report empirically measured γ and discuss its implications for which algorithmic framework (AAMAS vs. Buchbinder) is more appropriate.\n\n**Statistical rigor:** 3-5 independent runs per configuration, mean ± std, paired bootstrap significance tests.\n\n## Key References\n\n- AdaGReS: Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG (arXiv Dec 2025)\n- The Distracting Effect: Understanding Irrelevant Passages in RAG (ACL 2025)\n- Stronger Approximation Guarantees for Non-Monotone γ-Weakly DR-Submodular Maximization (AAMAS 2026)\n- Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming (arXiv 2604.02554, Apr 2026)\n- Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding (ICLR 2026)\n- DynamicRAG: Leveraging Outputs of LLM as Feedback for Dynamic Reranking in RAG (NeurIPS 2025)\n- Context-Picker: Dynamic Context Selection Using Multi-stage Reinforcement Learning (arXiv Dec 2025)\n- AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop RAG (arXiv May 2026)\n- SMART-RAG: Selection using Determinantal Matrices for Augmented Retrieval (arXiv:2409.13992, Sep 2024)\n- ScalDPP: Scaling DPPs for RAG — Density Meets Diversity (arXiv:2604.03240, Apr 2026)\n- Vendi-RAG: Adaptively Trading-Off Diversity and Quality (arXiv:2502.11228, Feb 2025)\n- Sub-CP: Submodular Context Partitioning for In-Context Learning (arXiv:2510.05130, Oct 2025)\n- Qian: Multi-objective Evolutionary Algorithms for Approximately Submodular Minus Modular (arXiv:1910.05492)\n- Buchbinder, Feldman, Naor, Schwartz: A Tight (1/2)-Approximation for Unconstrained Submodular Maximization (FOCS 2012)"
}
```

---

### Runtime record

_source line 2 · 2026-05-30T07:11:09.297Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T07:11:09.297Z",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7"
}
```

---

## Round 1

56 recorded events

### User

_source line 3 · 2026-05-30T07:11:09.320Z_

# Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition

## Core Problem

How can post-retrieval context composition for RAG be formalized as a constrained non-monotone submodular optimization problem that provably distinguishes between redundancy (intra-set semantic overlap) and distraction (answer-conditional interference) as separate penalty terms, yielding greedy approximation guarantees even when adding passages can decrease generation quality?

## Broader Motivation

The problem of "when does adding more information provably hurt?" arises across context engineering: in-context learning (where Sub-CP, arXiv:2510.05130, applies submodular optimization to exemplar partitioning), tool-use composition, and multi-document grounding all exhibit non-monotone returns to context size. This work instantiates the question in RAG post-retrieval composition, where it is most acute and empirically measurable, providing the first framework that decomposes the harm into redundancy and distraction with provable optimization guarantees.

## Research Opportunity

Three independently developed building blocks have converged but never been combined: (1) AdaGReS (arXiv Dec 2025) proved ε-approximate submodularity for redundancy-penalized context selection but only handles monotone objectives; (2) The Distracting Effect (ACL 2025) provides a concrete per-passage distraction measure DE_q(p) = 1−P(NO-RESPONSE|q,p) but performs no set-level optimization; (3) the AAMAS 2026 γ-weakly DR-submodular paper provides approximation guarantees Φ_γ for non-monotone objectives but has zero empirical applications to NLP.

The critical insight: subtracting a modular distraction penalty from AdaGReS's ε-approximately submodular objective makes the combined function non-monotone and non-submodular. The general problem class of maximizing "approximately submodular minus modular" functions has been studied theoretically (Qian, arXiv:1910.05492; Buchbinder et al., FOCS 2012 for the exact submodular case), but has never been instantiated in NLP or RAG. This work provides the first such instantiation, deriving the specific γ-weak DR-submodularity parameter for the RAG distraction-redundancy objective and empirically validating the AAMAS double-greedy framework in this domain.

## Research Landscape

Current SOTA splits into two disjoint camps with a verified gap.

**Camp 1 (formal guarantees, distraction-blind):** AdaGReS achieves ε-approximate submodularity with adaptive β* but only models redundancy, evaluated on 2 benchmarks. CCBQP (arXiv 2604.02554, Apr 2026) provides Frank-Wolfe with O(nd) iterations and landscape analysis via diagonal loading λ≥2, dominating MMR and DPP on the relevance-diversity Pareto frontier (QAMPARI/ASQA), but handles only relevance-diversity with no distraction term. SMART-RAG (arXiv:2409.13992, Sep 2024) uses DPP to jointly model relevance, diversity, and conflict, training-free, but lacks distraction modeling and non-monotone optimization guarantees. ScalDPP (arXiv:2604.03240, Apr 2026) scales DPP via P-Adapter with Diverse Margin Loss but remains in the relevance-diversity paradigm.

**Camp 2 (distraction-aware, no formal guarantees):** LDAR (ICLR 2026) is a distraction-aware retriever operating at retrieval time across 6 benchmarks but provides no post-retrieval composition or approximation bounds. DynamicRAG (NeurIPS 2025) uses RL with LLM feedback across 7 benchmarks but offers no optimization guarantees. Context-Picker (arXiv Dec 2025) uses two-stage RL for context selection across 5 benchmarks. Vendi-RAG (arXiv:2502.11228, Feb 2025) uses Vendi Score diversity + LLM judge for iterative diversity-quality optimization on multi-hop QA, but provides no formal guarantees and does not explicitly decompose redundancy from distraction. All learned approaches are distribution-dependent with no formal generalization guarantees under domain shift.

**The gap:** No existing method is simultaneously post-retrieval, formally grounded with provable approximation bounds, and distraction-aware.

## Addressing the Trivial Alternative

A natural two-stage pipeline—first filter high-DE passages via threshold, then run AdaGReS's monotone greedy on survivors—appears to achieve both distraction-awareness and formal guarantees without new theory. Joint optimization is necessary for the following reason:

**Pre-filtering forfeits optimality guarantees.** Removing passages before optimization shrinks the feasible set in a data-dependent, non-principled way. The resulting solution has no approximation guarantee relative to the optimal subset of the full candidate set. The joint formulation preserves the full candidate set and provides Φ_γ guarantees over it. A passage with high individual DE_q may still be the optimal choice when its relevance contribution outweighs the distraction cost in the joint objective—threshold filtering irrecoverably discards such passages.

Additionally, we treat set-level distraction interaction as an empirical hypothesis: while the base formulation uses modular (per-passage) DE for computational tractability, the ablation study includes a conditional DE_q(p|S\{p}) variant to test whether set-conditioned distraction scoring provides additional benefit. If confirmed, this would constitute an additional empirical contribution beyond the formal optimization framework.

## Proposed Approach

Define the set objective:

f(S) = Σ_{p∈S} rel(q,p) − β·Σ_{p,p'∈S} sim(p,p') − λ·Σ_{p∈S} DE_q(p)

where rel(q,p) is query-passage relevance (embedding cosine similarity), sim(p,p') is pairwise passage similarity (redundancy), and DE_q(p) is the per-passage Distracting Effect score (ACL 2025) computed via LLM no-response probability.

**Why non-monotone:** The distraction penalty Σ DE_q(p) grows linearly with |S|. Beyond a critical set size, accumulated distraction cost overwhelms relevance gains, making f decrease with added passages. This non-monotonicity invalidates standard monotone greedy guarantees (AdaGReS).

**Computational advantage of modular DE:** Since DE_q(p) depends only on the (q,p) pair, all DE scores can be pre-computed and cached before the greedy optimization begins. The DE computation cost is O(n) LLM calls (one per candidate passage), amortized across the optimization, rather than O(n·k) calls that a set-conditional formulation would require.

**Theoretical contribution:** The relevance − redundancy component inherits AdaGReS's ε-approximate submodularity. Subtracting the modular distraction term yields a non-monotone, non-submodular function in the "approximately submodular minus modular" problem class (cf. Qian, arXiv:1910.05492). Our specific contribution is deriving the γ-weak DR-submodularity parameter for this RAG-specific objective under bounded-embedding conditions, enabling the AAMAS 2026 double-greedy framework with Φ_γ > γe^{−γ} approximation guarantee.

The bounded-embedding conditions require: (a) embedding norms bounded in [c_min, c_max] with c_min > 0; (b) pairwise cosine similarity curvature bounded—specifically, the diminishing-return ratio of the relevance-redundancy component must be lower-bounded by γ > 0, which depends on the ratio c_min/c_max and the maximum pairwise similarity in the candidate set. When the candidate pool contains near-duplicate passages (sim ≈ 1), γ may degrade; we empirically measure γ on each benchmark and discuss graceful degradation of the guarantee when γ is small.

**Comparison with classical algorithms:** For exact non-monotone submodular functions, Buchbinder et al. (FOCS 2012) provide a 1/2-approximation via randomized double-greedy, which is tighter than AAMAS's Φ_γ when γ ≈ 1. Our empirically measured γ determines which framework is more appropriate. Both algorithms are included in the experimental comparison.

## Experimental Design

**Benchmarks:** Natural Questions (NQ), ASQA, QAMPARI.

**Metrics per benchmark:**
- NQ: Exact Match (EM), token-level F1
- ASQA: ROUGE-L, Disambig-F1 (D-F1), citation precision/recall (ALCE framework)
- QAMPARI: Entity-level F1, entity recall
- Cross-benchmark: tokens per query, wall-clock latency per query, redundancy ratio

**Models:** Qwen3-Embedding-8B (retrieval + similarity), Qwen3-8B (DE scoring), Llama-4-Scout (primary generator), Qwen3-8B (secondary generator for cross-generator validation on NQ).

**Baselines (three groups):**
- Simple heuristic: top-k, MMR
- Formal optimization: AdaGReS, CCBQP, SMART-RAG
- Learned: DynamicRAG, LDAR, Context-Picker

**LDAR comparison protocol:** Two settings: (a) Retrieval-controlled—all methods use Qwen3-Embedding-8B top-100 candidates, comparing post-retrieval composition only (LDAR's post-retrieval component if applicable); (b) End-to-end—LDAR uses its own retriever vs. proposed method with Qwen3-Embedding-8B + composition, comparing paradigms (distraction-aware retrieval vs. distraction-aware composition).

**Ablation studies:**
1. Component isolation: (a) f without distraction (= AdaGReS-like), (b) f without redundancy, (c) full f → marginal contribution of each penalty
2. Hyperparameter sensitivity: β × λ grid (5×5), Pareto surface
3. Algorithm comparison: AAMAS double-greedy vs. Buchbinder et al. randomized double-greedy vs. standard greedy vs. random
4. DE scoring model: Qwen3-8B DE vs. Llama-4-Scout self-DE → cross-model transferability
5. Per-passage DE vs. conditional DE_q(p|S\{p}): set-conditional scoring benefit vs. cost
6. Selection set size k: impact on f and downstream accuracy
7. Joint optimization vs. two-stage pipeline: DE threshold τ ∈ {0.3, 0.5, 0.7} filter → AdaGReS greedy vs. full joint optimization → validate necessity of joint approach
8. Cross-generator validation: full baseline comparison on NQ with Qwen3-8B as generator

**Domain-shift evaluation:** Train/tune learned baselines (DynamicRAG, Context-Picker) on one benchmark distribution, evaluate on a different benchmark. Proposed method uses identical hyperparameters across all benchmarks without retuning. This directly tests the claimed robustness advantage of formal guarantees over learned approaches under distribution shift.

**Compute-normalized comparison:** Report per-query inference cost (LLM calls, total tokens, wall-clock time) for all methods. Plot accuracy-vs-compute Pareto curves. Explicitly report DE pre-computation cost as a separate line item.

**Cross-model DE calibration:** On a validation subset, compute DE using both Qwen3-8B and Llama-4-Scout, report Spearman/Pearson correlation.

**Bounded-embedding verification:** Report embedding norm distributions and pairwise similarity statistics for Qwen3-Embedding-8B on each benchmark. Report empirically measured γ and discuss its implications for which algorithmic framework (AAMAS vs. Buchbinder) is more appropriate.

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "5d3abe21-235c-45be-ad4b-bb4a82a5a4e1",
  "type": "user",
  "uuid": "cf44d4a3-9d36-48ff-907c-97ac424f446c",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T07:11:09.319Z_

```json
{
  "parentUuid": "cf44d4a3-9d36-48ff-907c-97ac424f446c",
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
  "uuid": "f761c8d5-e774-4fbe-a8ce-0e4fc026bd3c",
  "timestamp": "2026-05-30T07:11:09.319Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T07:11:09.319Z_

```json
{
  "parentUuid": "f761c8d5-e774-4fbe-a8ce-0e4fc026bd3c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "de9f8748-0af7-4eb9-bb22-c4f4c064a3a8",
  "timestamp": "2026-05-30T07:11:09.319Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Non-monotone submodular context composition for RAG",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7"
}
```

---

### Assistant

_source line 7 · 2026-05-30T07:11:19.533Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to act as the "发掘 agent" (Discovery Agent) to analyze a research proposal about "Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition" for RAG systems. 

Let me first read and understand the proposal thoroughly, then do WebSearch for related work and recent developments before giving my analysis.

The proposal is about:
1. Formalizing post-retrieval context composition for RAG as a constrained non-monotone submodular optimization problem
2. Decomposing harm into redundancy (intra-set overlap) and distraction (answer-conditional interference)


3. Combining AdaGReS for handling redundancy with a distraction effect measure, leveraging recent theoretical guarantees for weakly DR-submodular functions
4. The core objective function balances relevance against both redundancy and distraction penalties across the selected passages

Now I need to search for related work and recent developments in this area.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de9f8748-0af7-4eb9-bb22-c4f4c064a3a8",
  "isSidechain": false,
  "requestId": "req_011CbYLTXqSeBTxmRHPTo1ub",
  "type": "assistant",
  "uuid": "8e7785a3-bd66-4835-82c6-02d3ab43defd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D7ABuT82rydHGzk4tpVWhr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4810,
      "cache_read_input_tokens": 14184,
      "output_tokens": 379,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4810,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 379,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 4810,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4810
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

_source line 8 · 2026-05-30T07:11:19.538Z_

I'll start by reading the proposal carefully and then conducting thorough literature research before making any judgments. Let me search for the most relevant recent work across multiple dimensions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e7785a3-bd66-4835-82c6-02d3ab43defd",
  "isSidechain": false,
  "requestId": "req_011CbYLTXqSeBTxmRHPTo1ub",
  "type": "assistant",
  "uuid": "839fe20e-bfaf-42a8-902e-d6aab29b77d2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D7ABuT82rydHGzk4tpVWhr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4810,
      "cache_read_input_tokens": 14184,
      "output_tokens": 379,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4810,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 379,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 4810,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4810
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

_source line 9 · 2026-05-30T07:11:19.704Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01E9858UavDaYP6dYaLRE1W7`</summary>

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
  "parentUuid": "839fe20e-bfaf-42a8-902e-d6aab29b77d2",
  "isSidechain": false,
  "requestId": "req_011CbYLTXqSeBTxmRHPTo1ub",
  "type": "assistant",
  "uuid": "7fb1cff7-6fa4-4f87-95cd-df524a681614",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D7ABuT82rydHGzk4tpVWhr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4810,
      "cache_read_input_tokens": 14184,
      "output_tokens": 379,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4810,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 379,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 4810,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4810
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

_source line 10 · 2026-05-30T07:11:19.716Z_

<details><summary>↩ Tool result · `toolu_01E9858UavDaYP6dYaLRE1W7`</summary>

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
  "parentUuid": "7fb1cff7-6fa4-4f87-95cd-df524a681614",
  "isSidechain": false,
  "promptId": "5d3abe21-235c-45be-ad4b-bb4a82a5a4e1",
  "type": "user",
  "uuid": "f0b7f821-1760-486a-9815-d0c7ab068fda",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "7fb1cff7-6fa4-4f87-95cd-df524a681614",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition  ## Core Problem  How can post-retrieval context composition for RAG be formalized as a constrained non-monotone…",
  "leafUuid": "f0b7f821-1760-486a-9815-d0c7ab068fda",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Non-monotone submodular context composition for RAG",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7"
}
```

---

### Assistant

_source line 13 · 2026-05-30T07:11:22.600Z_

Now let me conduct the prerequisite research. I'll search for the key related works and recent developments in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0b7f821-1760-486a-9815-d0c7ab068fda",
  "isSidechain": false,
  "requestId": "req_011CbYLUJQ5uqg9jeSBdxrRA",
  "type": "assistant",
  "uuid": "4e10c282-6821-4923-b276-c5ddd84298c6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Et4mmF6tVp1XFzR4gpN5tm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 907,
      "cache_read_input_tokens": 18994,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 907,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 96,
          "cache_read_input_tokens": 18994,
          "cache_creation_input_tokens": 907,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 907
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

_source line 14 · 2026-05-30T07:11:22.975Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018y873VfDN5Xj6pXxyiBbQU`</summary>

```json
{
  "query": "AdaGReS adaptive greedy context selection redundancy RAG submodular 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e10c282-6821-4923-b276-c5ddd84298c6",
  "isSidechain": false,
  "requestId": "req_011CbYLUJQ5uqg9jeSBdxrRA",
  "type": "assistant",
  "uuid": "b787db6e-3dea-4a72-bbe7-ce918fb1e4e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Et4mmF6tVp1XFzR4gpN5tm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 907,
      "cache_read_input_tokens": 18994,
      "output_tokens": 96,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 907,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 96,
          "cache_read_input_tokens": 18994,
          "cache_creation_input_tokens": 907,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 907
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

_source line 15 · 2026-05-30T07:11:29.075Z_

<details><summary>↩ Tool result · `toolu_018y873VfDN5Xj6pXxyiBbQU`</summary>

```text
Web search results for query: "AdaGReS adaptive greedy context selection redundancy RAG submodular 2025"

Links: [{"title":"[2512.25052] AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG","url":"https://arxiv.org/abs/2512.25052"},{"title":"AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG","url":"https://arxiv.org/html/2512.25052"},{"title":"AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG","url":"https://arxiv.org/pdf/2512.25052"},{"title":"(PDF) AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG","url":"https://www.researchgate.net/publication/399276683_AdaGReSAdaptive_Greedy_Context_Selection_via_Redundancy-Aware_Scoring_for_Token-Budgeted_RAG"},{"title":"AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop Retrieval-Augmented Generation","url":"https://arxiv.org/html/2605.05245"}]

Based on the search results, I found detailed information about AdaGReS:

## AdaGReS: Adaptive Greedy Context Selection

AdaGReS is a redundancy-aware context selection framework for token-budgeted RAG that optimizes a set-level objective combining query-chunk relevance and intra-set redundancy penalties.

### Key Features

AdaGReS performs greedy selection under a token-budget constraint using marginal gains derived from the objective, and introduces a closed-form, instance-adaptive calibration of the relevance-redundancy trade-off parameter to eliminate manual tuning and adapt to candidate-pool statistics and budget limits.

### Theoretical Foundation

The proposed objective exhibits epsilon-approximate submodularity under practical embedding similarity conditions, yielding near-optimality guarantees for greedy selection.

### Problem Context

Retrieval-augmented generation (RAG) is highly sensitive to the quality of selected context, yet standard top-k retrieval often returns redundant or near-duplicate chunks that waste token budget and degrade downstream generation.

### Evaluation

The paper includes experiments on open-domain question answering (Natural Questions) and a high-redundancy biomedical (drug) corpus that demonstrate consistent improvements in redundancy control and context quality.

The paper was published in December 2025 on arXiv (paper ID: 2512.25052).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b787db6e-3dea-4a72-bbe7-ce918fb1e4e3",
  "isSidechain": false,
  "promptId": "5d3abe21-235c-45be-ad4b-bb4a82a5a4e1",
  "type": "user",
  "uuid": "a7b6770d-1c9c-4ae7-a4b5-747999f540b8",
  "toolUseResult": {
    "query": "AdaGReS adaptive greedy context selection redundancy RAG submodular 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GUzPCaRkAG2fHUx9oXEjbY",
        "content": [
          {
            "title": "[2512.25052] AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG",
            "url": "https://arxiv.org/abs/2512.25052"
          },
          {
            "title": "AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG",
            "url": "https://arxiv.org/html/2512.25052"
          },
          {
            "title": "AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG",
            "url": "https://arxiv.org/pdf/2512.25052"
          },
          {
            "title": "(PDF) AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG",
            "url": "https://www.researchgate.net/publication/399276683_AdaGReSAdaptive_Greedy_Context_Selection_via_Redundancy-Aware_Scoring_for_Token-Budgeted_RAG"
          },
          {
            "title": "AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2605.05245"
          }
        ]
      },
      "Based on the search results, I found detailed information about AdaGReS:\n\n## AdaGReS: Adaptive Greedy Context Selection\n\nAdaGReS is a redundancy-aware context selection framework for token-budgeted RAG that optimizes a set-level objective combining query-chunk relevance and intra-set redundancy penalties.\n\n### Key Features\n\nAdaGReS performs greedy selection under a token-budget constraint using marginal gains derived from the objective, and introduces a closed-form, instance-adaptive calibration of the relevance-redundancy trade-off parameter to eliminate manual tuning and adapt to candidate-pool statistics and budget limits.\n\n### Theoretical Foundation\n\nThe proposed objective exhibits epsilon-approximate submodularity under practical embedding similarity conditions, yielding near-optimality guarantees for greedy selection.\n\n### Problem Context\n\nRetrieval-augmented generation (RAG) is highly sensitive to the quality of selected context, yet standard top-k retrieval often returns redundant or near-duplicate chunks that waste token budget and degrade downstream generation.\n\n### Evaluation\n\nThe paper includes experiments on open-domain question answering (Natural Questions) and a high-redundancy biomedical (drug) corpus that demonstrate consistent improvements in redundancy control and context quality.\n\nThe paper was published in December 2025 on arXiv (paper ID: 2512.25052)."
    ],
    "durationSeconds": 6.090778359,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b787db6e-3dea-4a72-bbe7-ce918fb1e4e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-30T07:11:33.738Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NWjvTDa17YKDDe3jaePQzm`</summary>

```json
{
  "query": "distracting effect irrelevant passages RAG ACL 2025 no-response probability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7b6770d-1c9c-4ae7-a4b5-747999f540b8",
  "isSidechain": false,
  "requestId": "req_011CbYLUzUqxn1sWjkVqeQJa",
  "type": "assistant",
  "uuid": "834a3b37-c8c8-4f4b-b9eb-9c4c55ad7ef9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ci4rSXWAQCZrcMQC7LSesE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 781,
      "cache_read_input_tokens": 19901,
      "output_tokens": 71,
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
          "output_tokens": 71,
          "cache_read_input_tokens": 19901,
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

_source line 17 · 2026-05-30T07:11:41.530Z_

<details><summary>↩ Tool result · `toolu_01NWjvTDa17YKDDe3jaePQzm`</summary>

```text
Web search results for query: "distracting effect irrelevant passages RAG ACL 2025 no-response probability"

Links: [{"title":"The Distracting Effect: Understanding Irrelevant Passages in RAG - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.892/"},{"title":"The Distracting Effect: Understanding Irrelevant Passages in RAG (ACL 2025) - YouTube","url":"https://www.youtube.com/watch?v=BtLsxjA5D0A"},{"title":"The Distracting Effect: Understanding Irrelevant Passages in RAG","url":"https://arxiv.org/html/2505.06914v1"},{"title":"The Distracting Effect: Understanding Irrelevant Passages ...","url":"https://aclanthology.org/2025.acl-long.892.pdf"},{"title":"The Distracting Effect: Understanding Irrelevant Passages in RAG","url":"https://arxiv.org/pdf/2505.06914"},{"title":"[2505.06914] The Distracting Effect: Understanding Irrelevant Passages in RAG","url":"https://arxiv.org/abs/2505.06914"},{"title":"Paper page - The Distracting Effect: Understanding Irrelevant Passages in RAG","url":"https://huggingface.co/papers/2505.06914"},{"title":"Redefining Retrieval Evaluation in the Era of LLMs","url":"https://aclanthology.org/2026.eacl-long.391.pdf"}]

I found relevant information about the paper "The Distracting Effect: Understanding Irrelevant Passages in RAG" presented at ACL 2025. Here are the key findings:

## Paper Overview

Retrieved passages that are irrelevant to the query sometimes distract the answer-generating LLM, causing it to provide an incorrect response. The paper sheds light on this issue and formulates the distracting effect of a passage with respect to a query and an LLM, providing a quantifiable measure of the distracting effect of a passage and demonstrating its robustness across LLMs.

## Key Contributions

The contribution is two-fold: first, moving beyond the simple binary classification of irrelevant passages as either completely unrelated vs. distracting, and second, developing and analyzing multiple methods for finding hard distracting passages.

## Results

By fine-tuning LLMs with carefully selected distracting passages, they achieve up to a 7.5% increase in answering accuracy compared to counterparts fine-tuned on conventional RAG datasets.

## Measurement Approach

The research proposes a continuous score to measure the distracting effect of irrelevant passages, computing the distracting effect DEq(p) of an irrelevant passage p for question q as the probability of the LLM answer.

The paper was authored by Chen Amiraz, Florin Cuconasu, Simone Filice, and Zohar Karnin and published at the 63rd Annual Meeting of the Association for Computational Linguistics in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "834a3b37-c8c8-4f4b-b9eb-9c4c55ad7ef9",
  "isSidechain": false,
  "promptId": "5d3abe21-235c-45be-ad4b-bb4a82a5a4e1",
  "type": "user",
  "uuid": "c7ef396b-67d0-4b39-8b03-45bb8d8356ba",
  "toolUseResult": {
    "query": "distracting effect irrelevant passages RAG ACL 2025 no-response probability",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KPaEtNPBD9HVanro2DBhXG",
        "content": [
          {
            "title": "The Distracting Effect: Understanding Irrelevant Passages in RAG - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.892/"
          },
          {
            "title": "The Distracting Effect: Understanding Irrelevant Passages in RAG (ACL 2025) - YouTube",
            "url": "https://www.youtube.com/watch?v=BtLsxjA5D0A"
          },
          {
            "title": "The Distracting Effect: Understanding Irrelevant Passages in RAG",
            "url": "https://arxiv.org/html/2505.06914v1"
          },
          {
            "title": "The Distracting Effect: Understanding Irrelevant Passages ...",
            "url": "https://aclanthology.org/2025.acl-long.892.pdf"
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
            "title": "Paper page - The Distracting Effect: Understanding Irrelevant Passages in RAG",
            "url": "https://huggingface.co/papers/2505.06914"
          },
          {
            "title": "Redefining Retrieval Evaluation in the Era of LLMs",
            "url": "https://aclanthology.org/2026.eacl-long.391.pdf"
          }
        ]
      },
      "I found relevant information about the paper \"The Distracting Effect: Understanding Irrelevant Passages in RAG\" presented at ACL 2025. Here are the key findings:\n\n## Paper Overview\n\nRetrieved passages that are irrelevant to the query sometimes distract the answer-generating LLM, causing it to provide an incorrect response. The paper sheds light on this issue and formulates the distracting effect of a passage with respect to a query and an LLM, providing a quantifiable measure of the distracting effect of a passage and demonstrating its robustness across LLMs.\n\n## Key Contributions\n\nThe contribution is two-fold: first, moving beyond the simple binary classification of irrelevant passages as either completely unrelated vs. distracting, and second, developing and analyzing multiple methods for finding hard distracting passages.\n\n## Results\n\nBy fine-tuning LLMs with carefully selected distracting passages, they achieve up to a 7.5% increase in answering accuracy compared to counterparts fine-tuned on conventional RAG datasets.\n\n## Measurement Approach\n\nThe research proposes a continuous score to measure the distracting effect of irrelevant passages, computing the distracting effect DEq(p) of an irrelevant passage p for question q as the probability of the LLM answer.\n\nThe paper was authored by Chen Amiraz, Florin Cuconasu, Simone Filice, and Zohar Karnin and published at the 63rd Annual Meeting of the Association for Computational Linguistics in 2025."
    ],
    "durationSeconds": 7.787991620000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "834a3b37-c8c8-4f4b-b9eb-9c4c55ad7ef9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-30T07:11:44.253Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013VV9FHQxrgnqsAP7HV8mUA`</summary>

```json
{
  "query": "gamma weakly DR-submodular non-monotone maximization approximation guarantee AAMAS 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7ef396b-67d0-4b39-8b03-45bb8d8356ba",
  "isSidechain": false,
  "requestId": "req_011CbYLVuQn36DmazN84JUu2",
  "type": "assistant",
  "uuid": "b2444591-3807-4f5f-b34b-f0c09c133782",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X3kd33Jd6Lkxq8u1v4e4ny",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 841,
      "cache_read_input_tokens": 20682,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 841,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 20682,
          "cache_creation_input_tokens": 841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 841
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

_source line 19 · 2026-05-30T07:11:51.659Z_

<details><summary>↩ Tool result · `toolu_013VV9FHQxrgnqsAP7HV8mUA`</summary>

```text
Web search results for query: "gamma weakly DR-submodular non-monotone maximization approximation guarantee AAMAS 2026"

Links: [{"title":"Stronger Approximation Guarantees for Non-Monotone 𝛾-Weakly DR-Submodular Maximization","url":"https://arxiv.org/html/2601.00611"},{"title":"Stronger Approximation Guarantees for Non-Monotone γ-Weakly","url":"https://arxiv.org/pdf/2601.00611"},{"title":"[2601.00611] Stronger Approximation Guarantees for Non-Monotone γ-Weakly DR-Submodular Maximization","url":"https://arxiv.org/abs/2601.00611"},{"title":"A Unified Approach for Maximizing Continuous $\\gamma$-weakly DR-submodular Functions – Optimization Online","url":"https://optimization-online.org/2024/03/a-unified-approach-for-maximizing-continuous-gamma-weakly-dr-submodular-functions/"},{"title":"$\\gamma$-weakly $\\theta$-up-concavity: Linearizable Non-Convex Optimization with Applications to DR-Submodular and OSS Functions","url":"https://arxiv.org/pdf/2602.13506"},{"title":"Submodular Maximization Beyond Non-negativity:","url":"https://arxiv.org/pdf/1904.09354"},{"title":"Boosting Gradient Ascent for Continuous DR-submodular Maximization","url":"https://arxiv.org/pdf/2401.08330"},{"title":"Non-monotone DR-submodular Maximization: Approximation and Regret   Guarantees","url":"https://arxiv.org/pdf/1905.09595"},{"title":"[2401.08330] Boosting Gradient Ascent for Continuous DR-submodular Maximization","url":"https://arxiv.org/abs/2401.08330"}]

I found relevant results for your search. The top match is a paper that directly addresses your query:

The paper "Stronger Approximation Guarantees for Non-Monotone γ-Weakly DR-Submodular Maximization" will be presented at the International Conference on Autonomous Agents and Multiagent Systems (AAMAS) in May 2026.

The paper studies the maximization of a nonnegative, non-monotone γ-weakly DR-submodular function over a down-closed convex body, with an approximation algorithm whose guarantee depends smoothly on γ; when γ=1 (the DR-submodular case) the bound recovers a 0.401 approximation factor, while for γ<1 the guarantee degrades gracefully and improves upon previously reported bounds.

The approach combines a Frank-Wolfe-guided continuous-greedy framework with a γ-aware double-greedy step, yielding a simple yet effective procedure for handling non-monotonicity.

The paper was posted on arXiv on January 2, 2026, and is authored by Hareshkumar Jadav, Ranveer Singh, and Vaneet Aggarwal from IIT Indore and Purdue University.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2444591-3807-4f5f-b34b-f0c09c133782",
  "isSidechain": false,
  "promptId": "5d3abe21-235c-45be-ad4b-bb4a82a5a4e1",
  "type": "user",
  "uuid": "41a90430-4a7a-4e91-916f-c982088dd3a4",
  "toolUseResult": {
    "query": "gamma weakly DR-submodular non-monotone maximization approximation guarantee AAMAS 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SEyumNQVnGpvrYeGw3Rvsc",
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
            "title": "A Unified Approach for Maximizing Continuous $\\gamma$-weakly DR-submodular Functions – Optimization Online",
            "url": "https://optimization-online.org/2024/03/a-unified-approach-for-maximizing-continuous-gamma-weakly-dr-submodular-functions/"
          },
          {
            "title": "$\\gamma$-weakly $\\theta$-up-concavity: Linearizable Non-Convex Optimization with Applications to DR-Submodular and OSS Functions",
            "url": "https://arxiv.org/pdf/2602.13506"
          },
          {
            "title": "Submodular Maximization Beyond Non-negativity:",
            "url": "https://arxiv.org/pdf/1904.09354"
          },
          {
            "title": "Boosting Gradient Ascent for Continuous DR-submodular Maximization",
            "url": "https://arxiv.org/pdf/2401.08330"
          },
          {
            "title": "Non-monotone DR-submodular Maximization: Approximation and Regret   Guarantees",
            "url": "https://arxiv.org/pdf/1905.09595"
          },
          {
            "title": "[2401.08330] Boosting Gradient Ascent for Continuous DR-submodular Maximization",
            "url": "https://arxiv.org/abs/2401.08330"
          }
        ]
      },
      "I found relevant results for your search. The top match is a paper that directly addresses your query:\n\nThe paper \"Stronger Approximation Guarantees for Non-Monotone γ-Weakly DR-Submodular Maximization\" will be presented at the International Conference on Autonomous Agents and Multiagent Systems (AAMAS) in May 2026.\n\nThe paper studies the maximization of a nonnegative, non-monotone γ-weakly DR-submodular function over a down-closed convex body, with an approximation algorithm whose guarantee depends smoothly on γ; when γ=1 (the DR-submodular case) the bound recovers a 0.401 approximation factor, while for γ<1 the guarantee degrades gracefully and improves upon previously reported bounds.\n\nThe approach combines a Frank-Wolfe-guided continuous-greedy framework with a γ-aware double-greedy step, yielding a simple yet effective procedure for handling non-monotonicity.\n\nThe paper was posted on arXiv on January 2, 2026, and is authored by Hareshkumar Jadav, Ranveer Singh, and Vaneet Aggarwal from IIT Indore and Purdue University."
    ],
    "durationSeconds": 7.400769387,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b2444591-3807-4f5f-b34b-f0c09c133782",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-30T07:11:54.162Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C5cfGcHH2BcrHYYjxV6amk`</summary>

```json
{
  "query": "CCBQP cardinality constrained binary quadratic programming diversity retrieval RAG 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41a90430-4a7a-4e91-916f-c982088dd3a4",
  "isSidechain": false,
  "requestId": "req_011CbYLWeim4CLpuZbPvnBgt",
  "type": "assistant",
  "uuid": "9d785fd1-cba7-469a-9a57-ca9e8dbe6a92",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LLvGjkKwMTUQchcgxNiLiP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 884,
      "cache_read_input_tokens": 21523,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 884,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 21523,
          "cache_creation_input_tokens": 884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 884
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

_source line 21 · 2026-05-30T07:12:02.780Z_

<details><summary>↩ Tool result · `toolu_01C5cfGcHH2BcrHYYjxV6amk`</summary>

```text
Web search results for query: "CCBQP cardinality constrained binary quadratic programming diversity retrieval RAG 2026"

Links: [{"title":"[2604.02554] Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming","url":"https://arxiv.org/abs/2604.02554"},{"title":"Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming","url":"https://arxiv.org/html/2604.02554"},{"title":"Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming","url":"https://arxiv.org/pdf/2604.02554"},{"title":"Scaling DPPs for RAG: Density Meets Diversity","url":"https://arxiv.org/pdf/2604.03240"},{"title":"Cardinality-Constrained Binary Quadratic Optimization via Extreme Point Pursuit, with Application to the Densest K-Subgraph Problem | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10447398/"}]

Based on the search results, here's what I found:

A recent paper proposes a principled formulation of diversity retrieval as a cardinality-constrained binary quadratic programming (CCBQP), which explicitly balances relevance and semantic diversity through an interpretable trade-off parameter.

The work addresses diversity-aware retrieval for Retrieval-Augmented Generation (RAG), with the goal of overcoming limitations in existing methods that lack theoretical guarantees and face scalability issues as the number of retrieved passages increases.

The researchers developed a non-convex tight continuous relaxation and a Frank–Wolfe based algorithm with landscape analysis and convergence guarantees. Extensive experiments demonstrate that the method consistently dominates baselines on the relevance-diversity Pareto frontier, while achieving significant speedup.

The paper was published on arXiv on April 2, 2026 by Qiheng Lu and Nicholas D. Sidiropoulos from the University of Virginia.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d785fd1-cba7-469a-9a57-ca9e8dbe6a92",
  "isSidechain": false,
  "promptId": "5d3abe21-235c-45be-ad4b-bb4a82a5a4e1",
  "type": "user",
  "uuid": "815bec53-ce69-49d4-90f1-093709c0f391",
  "toolUseResult": {
    "query": "CCBQP cardinality constrained binary quadratic programming diversity retrieval RAG 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ax1bi3tBt7qjaPNXDsuJrZ",
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
      "Based on the search results, here's what I found:\n\nA recent paper proposes a principled formulation of diversity retrieval as a cardinality-constrained binary quadratic programming (CCBQP), which explicitly balances relevance and semantic diversity through an interpretable trade-off parameter.\n\nThe work addresses diversity-aware retrieval for Retrieval-Augmented Generation (RAG), with the goal of overcoming limitations in existing methods that lack theoretical guarantees and face scalability issues as the number of retrieved passages increases.\n\nThe researchers developed a non-convex tight continuous relaxation and a Frank–Wolfe based algorithm with landscape analysis and convergence guarantees. Extensive experiments demonstrate that the method consistently dominates baselines on the relevance-diversity Pareto frontier, while achieving significant speedup.\n\nThe paper was published on arXiv on April 2, 2026 by Qiheng Lu and Nicholas D. Sidiropoulos from the University of Virginia."
    ],
    "durationSeconds": 8.612755116,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9d785fd1-cba7-469a-9a57-ca9e8dbe6a92",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-30T07:12:05.261Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012z3DtrdZ9zvSz5UBcD5t3x`</summary>

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
  "parentUuid": "815bec53-ce69-49d4-90f1-093709c0f391",
  "isSidechain": false,
  "requestId": "req_011CbYLXUBnNBGK7DuuvL4HM",
  "type": "assistant",
  "uuid": "cf78e4f8-7f68-4aee-ae8c-2780206e076c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SNZsBchYWvQxNxN53XLi2w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 618,
      "cache_read_input_tokens": 22407,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 618,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 22407,
          "cache_creation_input_tokens": 618,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 618
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

_source line 23 · 2026-05-30T07:12:11.527Z_

<details><summary>↩ Tool result · `toolu_012z3DtrdZ9zvSz5UBcD5t3x`</summary>

```text
Web search results for query: "LDAR distraction-aware retrieval ICLR 2026 knowledge grounding"

Links: [{"title":"Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding","url":"https://arxiv.org/pdf/2509.21865"},{"title":"Downloads 2026","url":"https://iclr.cc/Downloads/2026"},{"title":"ICLR 2026 Workshops","url":"https://iclr.cc/virtual/2026/events/workshop"},{"title":"ICLR 2026 Schedule","url":"https://iclr.cc/virtual/2026/calendar"},{"title":"When RAG Hurts: Diagnosing and Mitigating Attention Distraction in Retrieval-Augmented LVLMs","url":"https://arxiv.org/pdf/2602.00344"}]

Based on the search results, I found information about LDAR and its connection to ICLR 2026:

LDAR (Learning Distraction-Aware Retrieval) is an adaptive retriever that learns to retrieve contexts in a way that mitigates interference from distracting passages, thereby achieving significantly higher performance with reduced token usage compared to long-context approaches.

The paper is titled "Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding" by Seongwoong Shim, Myunsoo Kim, Jae Hyeon Cho, and Byung-Jun Lee.

The research addresses limitations of long-context approaches including token inefficiency in handling large and potentially redundant contexts, the 'lost in the middle' phenomenon, and amplified distraction that degrades LLM output quality.

Extensive experiments across diverse LLM architectures and six knowledge-intensive benchmarks demonstrate the effectiveness and robustness of the approach, highlighting the importance of balancing the trade-off between information coverage and distraction.

The paper appears on the ICLR 2026 program based on the official conference downloads listing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf78e4f8-7f68-4aee-ae8c-2780206e076c",
  "isSidechain": false,
  "promptId": "5d3abe21-235c-45be-ad4b-bb4a82a5a4e1",
  "type": "user",
  "uuid": "9c093bf1-50f5-4d2b-8f6f-60f2f8db9874",
  "toolUseResult": {
    "query": "LDAR distraction-aware retrieval ICLR 2026 knowledge grounding",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DuvxQzsPrtxiL8GX8carTr",
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
          }
        ]
      },
      "Based on the search results, I found information about LDAR and its connection to ICLR 2026:\n\nLDAR (Learning Distraction-Aware Retrieval) is an adaptive retriever that learns to retrieve contexts in a way that mitigates interference from distracting passages, thereby achieving significantly higher performance with reduced token usage compared to long-context approaches.\n\nThe paper is titled \"Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding\" by Seongwoong Shim, Myunsoo Kim, Jae Hyeon Cho, and Byung-Jun Lee.\n\nThe research addresses limitations of long-context approaches including token inefficiency in handling large and potentially redundant contexts, the 'lost in the middle' phenomenon, and amplified distraction that degrades LLM output quality.\n\nExtensive experiments across diverse LLM architectures and six knowledge-intensive benchmarks demonstrate the effectiveness and robustness of the approach, highlighting the importance of balancing the trade-off between information coverage and distraction.\n\nThe paper appears on the ICLR 2026 program based on the official conference downloads listing."
    ],
    "durationSeconds": 6.261846530000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "cf78e4f8-7f68-4aee-ae8c-2780206e076c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition  ## Core Problem  How can post-retrieval context composition for RAG be formalized as a constrained non-monotone…",
  "leafUuid": "9c093bf1-50f5-4d2b-8f6f-60f2f8db9874",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Non-monotone submodular context composition for RAG",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7"
}
```

---

### Tool call

_source line 26 · 2026-05-30T07:12:14.089Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AvtiWW5rVtMp5PpA5MJyTf`</summary>

```json
{
  "query": "non-monotone submodular optimization NLP text selection context 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c093bf1-50f5-4d2b-8f6f-60f2f8db9874",
  "isSidechain": false,
  "requestId": "req_011CbYLY7coRkXLBu7Cakocb",
  "type": "assistant",
  "uuid": "cabc6f19-8214-4db2-9e5d-668cdb0eca99",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TWtC1Hmx8QdGNKHEuiAC1H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 589,
      "cache_read_input_tokens": 23025,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 589,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 23025,
          "cache_creation_input_tokens": 589,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 589
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

_source line 27 · 2026-05-30T07:12:21.373Z_

<details><summary>↩ Tool result · `toolu_01AvtiWW5rVtMp5PpA5MJyTf`</summary>

```text
Web search results for query: "non-monotone submodular optimization NLP text selection context 2025 2026"

Links: [{"title":"Submodular Optimization for Text Selection, Passage Reranking & Context Engineering","url":"https://jina.ai/news/submodular-optimization-for-text-selection-passage-reranking-context-engineering/"},{"title":"Data Summarization beyond Monotonicity: Non-monotone Two-Stage   Submodular Maximization","url":"https://arxiv.org/pdf/2309.05183"},{"title":"Non-monotone Submodular Optimization: p-Matchoid ...","url":"https://openreview.net/pdf/a1ec52c6c87154f7502cdc32cddd0dda50073cd5.pdf"},{"title":"Practical and Parallelizable Algorithms for Non-Monotone Submodular   Maximization with Size Constraint","url":"https://arxiv.org/pdf/2009.01947"},{"title":"Beyond Pointwise Submodularity: Non-Monotone Adaptive Submodular   Maximization in Linear Time","url":"https://arxiv.org/pdf/2008.05004"},{"title":"Non-monotone Submodular Maximization with Nearly Optimal Adaptivity and   Query Complexity","url":"https://arxiv.org/pdf/1808.06932"},{"title":"Constrained Non-Monotone Submodular Maximization: Offline and Secretary   Algorithms","url":"https://arxiv.org/pdf/1003.1517"}]

I've completed the web search for your query on non-monotone submodular optimization in NLP text selection and context. Here are the relevant findings:

## Key Results

**Recent Research on Non-Monotone Submodular Optimization:**

Real-world scenarios often involve objective functions that are non-monotone, with applications including feature selection, profit maximization, maximum cut, and data summarization.

**Algorithmic Advances:**

- The first constant-factor approximation algorithm for the non-monotone two-stage submodular maximization problem achieves an approximation ratio of 1/2e.
- Parallelizable algorithms for non-monotone submodular maximization with cardinality constraints achieve approximation ratios up to 0.193 - ε with optimal adaptivity and query complexity.
- A linear-time algorithm for non-monotone adaptive submodular maximization achieves a 1/e - ε approximation ratio under cardinality constraints.

**Application to NLP and Context Engineering:**

Submodular optimization provides a principled framework with formal guarantees for reliable, scalable context engineering, offering an alternative to prompt tuning approaches.

The search results include recent work from 2025, showing active research in this area particularly for applications in text selection and context optimization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cabc6f19-8214-4db2-9e5d-668cdb0eca99",
  "isSidechain": false,
  "promptId": "5d3abe21-235c-45be-ad4b-bb4a82a5a4e1",
  "type": "user",
  "uuid": "c91fb8f3-41dd-483a-911a-c89979ac68ec",
  "toolUseResult": {
    "query": "non-monotone submodular optimization NLP text selection context 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QxcRvpkvgvgLfECih399Jh",
        "content": [
          {
            "title": "Submodular Optimization for Text Selection, Passage Reranking & Context Engineering",
            "url": "https://jina.ai/news/submodular-optimization-for-text-selection-passage-reranking-context-engineering/"
          },
          {
            "title": "Data Summarization beyond Monotonicity: Non-monotone Two-Stage   Submodular Maximization",
            "url": "https://arxiv.org/pdf/2309.05183"
          },
          {
            "title": "Non-monotone Submodular Optimization: p-Matchoid ...",
            "url": "https://openreview.net/pdf/a1ec52c6c87154f7502cdc32cddd0dda50073cd5.pdf"
          },
          {
            "title": "Practical and Parallelizable Algorithms for Non-Monotone Submodular   Maximization with Size Constraint",
            "url": "https://arxiv.org/pdf/2009.01947"
          },
          {
            "title": "Beyond Pointwise Submodularity: Non-Monotone Adaptive Submodular   Maximization in Linear Time",
            "url": "https://arxiv.org/pdf/2008.05004"
          },
          {
            "title": "Non-monotone Submodular Maximization with Nearly Optimal Adaptivity and   Query Complexity",
            "url": "https://arxiv.org/pdf/1808.06932"
          },
          {
            "title": "Constrained Non-Monotone Submodular Maximization: Offline and Secretary   Algorithms",
            "url": "https://arxiv.org/pdf/1003.1517"
          }
        ]
      },
      "I've completed the web search for your query on non-monotone submodular optimization in NLP text selection and context. Here are the relevant findings:\n\n## Key Results\n\n**Recent Research on Non-Monotone Submodular Optimization:**\n\nReal-world scenarios often involve objective functions that are non-monotone, with applications including feature selection, profit maximization, maximum cut, and data summarization.\n\n**Algorithmic Advances:**\n\n- The first constant-factor approximation algorithm for the non-monotone two-stage submodular maximization problem achieves an approximation ratio of 1/2e.\n- Parallelizable algorithms for non-monotone submodular maximization with cardinality constraints achieve approximation ratios up to 0.193 - ε with optimal adaptivity and query complexity.\n- A linear-time algorithm for non-monotone adaptive submodular maximization achieves a 1/e - ε approximation ratio under cardinality constraints.\n\n**Application to NLP and Context Engineering:**\n\nSubmodular optimization provides a principled framework with formal guarantees for reliable, scalable context engineering, offering an alternative to prompt tuning approaches.\n\nThe search results include recent work from 2025, showing active research in this area particularly for applications in text selection and context optimization."
    ],
    "durationSeconds": 7.2784688469999965,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "cabc6f19-8214-4db2-9e5d-668cdb0eca99",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-30T07:12:23.964Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JEA6WgFHjdZPfAJxKnf2eX`</summary>

```json
{
  "query": "DynamicRAG reinforcement learning reranking NeurIPS 2025 LLM feedback"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c91fb8f3-41dd-483a-911a-c89979ac68ec",
  "isSidechain": false,
  "requestId": "req_011CbYLYqi7ULt7RgcjnvKQE",
  "type": "assistant",
  "uuid": "d147c846-1fd3-4c33-9bcb-bc4f11f0add1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NxoCyVRTN24YXBgA4rBzVg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 23614,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 769,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 23614,
          "cache_creation_input_tokens": 769,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 769
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

_source line 29 · 2026-05-30T07:12:29.897Z_

<details><summary>↩ Tool result · `toolu_01JEA6WgFHjdZPfAJxKnf2eX`</summary>

```text
Web search results for query: "DynamicRAG reinforcement learning reranking NeurIPS 2025 LLM feedback"

Links: [{"title":"DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation | OpenReview","url":"https://openreview.net/forum?id=NuCtKoflsV"},{"title":"GitHub - GasolSun36/DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation · GitHub","url":"https://github.com/GasolSun36/DynamicRAG"},{"title":"NeurIPS Poster DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation","url":"https://neurips.cc/virtual/2025/poster/118330"},{"title":"DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2505.07233"},{"title":"Optimizing RAG Rerankers with LLM Feedback via Reinforcement Learning","url":"https://arxiv.org/pdf/2604.02091"},{"title":"Optimizing RAG Rerankers with LLM Feedback via Reinforcement Learning","url":"https://arxiv.org/html/2604.02091"},{"title":"DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation","url":"https://arxiv.org/html/2505.07233v2"},{"title":"[2505.07233] DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2505.07233"}]

Based on the search results, here's what I found about DynamicRAG:

## Overview

DynamicRAG is a paper accepted at NeurIPS 2025 that proposes a framework optimizing retrieval-augmented generation by using reinforcement learning to adaptively rerank documents based on LLM's responses as feedback.

## Key Innovation

DynamicRAG is a novel RAG framework where the reranker dynamically adjusts both the order and number of retrieved documents based on the query, modeling the reranker as an agent optimized through reinforcement learning using rewards derived from LLM output quality.

## Problem Addressed

Recent studies exploring LLM-based rerankers primarily leverage internal model knowledge and overlook the rich supervisory signals that LLMs can provide, such as using response quality as feedback for optimizing reranking decisions.

## Training Approach

A reinforcement learning agent serves as the reranker, optimizing document retrieval based on feedback from an LLM, with the training process divided into two stages: Supervised Fine-Tuning via Behavior Cloning, and Reinforcement Learning with LLM Feedback that explores improved trajectories and further optimizes the reranker.

## Performance

Across seven knowledge-intensive datasets, DynamicRAG demonstrates superior performance, achieving state-of-the-art results.

The code and data are available on GitHub at https://github.com/GasolSun36/DynamicRAG.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d147c846-1fd3-4c33-9bcb-bc4f11f0add1",
  "isSidechain": false,
  "promptId": "5d3abe21-235c-45be-ad4b-bb4a82a5a4e1",
  "type": "user",
  "uuid": "ec4ad8e6-e8e3-4701-8eee-b81c6f4a9fd8",
  "toolUseResult": {
    "query": "DynamicRAG reinforcement learning reranking NeurIPS 2025 LLM feedback",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XPc8np23AFwoFatqFGvyP8",
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
            "title": "NeurIPS Poster DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation",
            "url": "https://neurips.cc/virtual/2025/poster/118330"
          },
          {
            "title": "DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2505.07233"
          },
          {
            "title": "Optimizing RAG Rerankers with LLM Feedback via Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2604.02091"
          },
          {
            "title": "Optimizing RAG Rerankers with LLM Feedback via Reinforcement Learning",
            "url": "https://arxiv.org/html/2604.02091"
          },
          {
            "title": "DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2505.07233v2"
          },
          {
            "title": "[2505.07233] DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/abs/2505.07233"
          }
        ]
      },
      "Based on the search results, here's what I found about DynamicRAG:\n\n## Overview\n\nDynamicRAG is a paper accepted at NeurIPS 2025 that proposes a framework optimizing retrieval-augmented generation by using reinforcement learning to adaptively rerank documents based on LLM's responses as feedback.\n\n## Key Innovation\n\nDynamicRAG is a novel RAG framework where the reranker dynamically adjusts both the order and number of retrieved documents based on the query, modeling the reranker as an agent optimized through reinforcement learning using rewards derived from LLM output quality.\n\n## Problem Addressed\n\nRecent studies exploring LLM-based rerankers primarily leverage internal model knowledge and overlook the rich supervisory signals that LLMs can provide, such as using response quality as feedback for optimizing reranking decisions.\n\n## Training Approach\n\nA reinforcement learning agent serves as the reranker, optimizing document retrieval based on feedback from an LLM, with the training process divided into two stages: Supervised Fine-Tuning via Behavior Cloning, and Reinforcement Learning with LLM Feedback that explores improved trajectories and further optimizes the reranker.\n\n## Performance\n\nAcross seven knowledge-intensive datasets, DynamicRAG demonstrates superior performance, achieving state-of-the-art results.\n\nThe code and data are available on GitHub at https://github.com/GasolSun36/DynamicRAG."
    ],
    "durationSeconds": 5.929539808999994,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d147c846-1fd3-4c33-9bcb-bc4f11f0add1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-30T07:12:29.900Z_

```json
{
  "parentUuid": "ec4ad8e6-e8e3-4701-8eee-b81c6f4a9fd8",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "aceb9d3b-b05a-4165-bb20-98dc811acd0a",
  "timestamp": "2026-05-30T07:12:29.900Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-30T07:12:32.998Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XZQZmqYLr72wnfiKkKre7s`</summary>

```json
{
  "query": "\"approximately submodular minus modular\" optimization Qian 2019 evolutionary algorithm"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aceb9d3b-b05a-4165-bb20-98dc811acd0a",
  "isSidechain": false,
  "requestId": "req_011CbYLZU8cZep2EAYrSoXXc",
  "type": "assistant",
  "uuid": "833a1280-688d-4482-9ba5-0a019d0e0c52",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KGEDDwWzB67Dq5WcHSaoc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1019,
      "cache_read_input_tokens": 24383,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1019,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 24383,
          "cache_creation_input_tokens": 1019,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1019
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

_source line 32 · 2026-05-30T07:12:39.307Z_

<details><summary>↩ Tool result · `toolu_01XZQZmqYLr72wnfiKkKre7s`</summary>

```text
Web search results for query: ""approximately submodular minus modular" optimization Qian 2019 evolutionary algorithm"

Links: [{"title":"[1910.05492] Multi-objective Evolutionary Algorithms are Still Good: Maximizing Monotone Approximately Submodular Minus Modular Functions","url":"https://arxiv.org/abs/1910.05492"},{"title":"Maximizing Non-monotone/Non-submodular Functions by Multi-objective Evolutionary Algorithms | Request PDF","url":"https://www.researchgate.net/publication/321180686_Maximizing_Non-monotoneNon-submodular_Functions_by_Multi-objective_Evolutionary_Algorithms"},{"title":"Multi-Objective Evolutionary Algorithms","url":"https://www.emergentmind.com/topics/multi-objective-evolutionary-algorithms"},{"title":"Multiobjective Evolutionary Algorithms Are Still Good: Maximizing Monotone Approximately Submodular Minus Modular Functions | Evolutionary Computation | MIT Press","url":"https://direct.mit.edu/evco/article-abstract/29/4/463/97355/Multiobjective-Evolutionary-Algorithms-Are-Still?redirectedFrom=fulltext"},{"title":"An Efficient Evolutionary Algorithm for Subset Selection ...","url":"https://www.lamda.nju.edu.cn/qianc/aaai20-eamc-final.pdf"},{"title":"Multi-objective Evolutionary Algorithms are Still Good: Maximizing   Monotone Approximately Submodular Minus Modular Functions","url":"https://arxiv.org/pdf/1910.05492"},{"title":"Multi-objective Evolutionary Algorithms are Still Good: Maximizing Monotone Approximately Submodular Minus Modular Functions - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv191005492Q/abstract"}]

I found relevant research on this topic. The work is by Chao Qian and was published in Evolutionary Computation in 2021 (though it was first posted on arXiv in October 2019).

The paper studies the problem class of maximizing monotone approximately submodular minus modular functions (i.e., f = g - c) with a size constraint, where g is a non-negative monotone approximately submodular function and c is a non-negative modular function, resulting in the objective function f being non-monotone nonsubmodular.

The research focuses on a simple multi-objective EA called GSEMO and proves that it can achieve good polynomial-time approximation guarantees for this problem class. Empirical studies on the applications of Bayesian experimental design and directed vertex cover show the excellent performance of the GSEMO.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "833a1280-688d-4482-9ba5-0a019d0e0c52",
  "isSidechain": false,
  "promptId": "5d3abe21-235c-45be-ad4b-bb4a82a5a4e1",
  "type": "user",
  "uuid": "aceb83ab-1bec-4df1-8332-76d552d2182b",
  "toolUseResult": {
    "query": "\"approximately submodular minus modular\" optimization Qian 2019 evolutionary algorithm",
    "results": [
      {
        "tool_use_id": "srvtoolu_012o85YgcMHQM32XGpJpk28M",
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
            "title": "Multi-Objective Evolutionary Algorithms",
            "url": "https://www.emergentmind.com/topics/multi-objective-evolutionary-algorithms"
          },
          {
            "title": "Multiobjective Evolutionary Algorithms Are Still Good: Maximizing Monotone Approximately Submodular Minus Modular Functions | Evolutionary Computation | MIT Press",
            "url": "https://direct.mit.edu/evco/article-abstract/29/4/463/97355/Multiobjective-Evolutionary-Algorithms-Are-Still?redirectedFrom=fulltext"
          },
          {
            "title": "An Efficient Evolutionary Algorithm for Subset Selection ...",
            "url": "https://www.lamda.nju.edu.cn/qianc/aaai20-eamc-final.pdf"
          },
          {
            "title": "Multi-objective Evolutionary Algorithms are Still Good: Maximizing   Monotone Approximately Submodular Minus Modular Functions",
            "url": "https://arxiv.org/pdf/1910.05492"
          },
          {
            "title": "Multi-objective Evolutionary Algorithms are Still Good: Maximizing Monotone Approximately Submodular Minus Modular Functions - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2019arXiv191005492Q/abstract"
          }
        ]
      },
      "I found relevant research on this topic. The work is by Chao Qian and was published in Evolutionary Computation in 2021 (though it was first posted on arXiv in October 2019).\n\nThe paper studies the problem class of maximizing monotone approximately submodular minus modular functions (i.e., f = g - c) with a size constraint, where g is a non-negative monotone approximately submodular function and c is a non-negative modular function, resulting in the objective function f being non-monotone nonsubmodular.\n\nThe research focuses on a simple multi-objective EA called GSEMO and proves that it can achieve good polynomial-time approximation guarantees for this problem class. Empirical studies on the applications of Bayesian experimental design and directed vertex cover show the excellent performance of the GSEMO."
    ],
    "durationSeconds": 6.304209199000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "833a1280-688d-4482-9ba5-0a019d0e0c52",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-30T07:12:47.243Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Kvad7GUmmM9jTnrRTT4gMV`</summary>

```json
{
  "query": "RAG post-retrieval context selection optimization formal guarantees 2025 2026 survey"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aceb83ab-1bec-4df1-8332-76d552d2182b",
  "isSidechain": false,
  "requestId": "req_011CbYLaAkdAf7GeCu8UGAX3",
  "type": "assistant",
  "uuid": "eb0b592a-2445-417e-923d-9c49f1cfdbf7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HrDSutpKECK2t2W5GfUMpV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 743,
      "cache_read_input_tokens": 25402,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 743,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 25402,
          "cache_creation_input_tokens": 743,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 743
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

_source line 34 · 2026-05-30T07:12:55.134Z_

<details><summary>↩ Tool result · `toolu_01Kvad7GUmmM9jTnrRTT4gMV`</summary>

```text
Web search results for query: "RAG post-retrieval context selection optimization formal guarantees 2025 2026 survey"

Links: [{"title":"AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG","url":"https://arxiv.org/pdf/2512.25052"},{"title":"Retrieval-Augmented Generation: A Comprehensive Survey of Architectures, Enhancements, and Robustness Frontiers","url":"https://arxiv.org/html/2506.00054v1"},{"title":"awesome-generative-ai-guide/research_updates/rag_research_table.md at main · aishwaryanr/awesome-generative-ai-guide","url":"https://github.com/aishwaryanr/awesome-generative-ai-guide/blob/main/research_updates/rag_research_table.md"},{"title":"Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction","url":"https://arxiv.org/pdf/2511.17908"},{"title":"(PDF) The Evolution of Retrieval-Augmented Generation (RAG) in AI","url":"https://www.researchgate.net/publication/399423892_The_Evolution_of_Retrieval-Augmented_Generation_RAG_in_AI"},{"title":"From RAG to Context - A 2025 year-end review of RAG | RAGFlow","url":"https://ragflow.io/blog/rag-review-2025-from-rag-to-context"},{"title":"Ranking Free RAG: Replacing Re-ranking with Selection in RAG for Sensitive Domains","url":"https://arxiv.org/pdf/2505.16014"}]

The search returned several highly relevant results on RAG post-retrieval context selection optimization with formal guarantees from 2025-2026. Here's what I found:

## Key Research Areas

**Formal Guarantees & Theoretical Analysis:**

AdaGReS proposes a theoretical analysis showing that the proposed objective exhibits ε-approximate submodularity under practical embedding similarity conditions, yielding near-optimality guarantees for greedy selection. Additionally, context engineering through conformal prediction provides finite-sample coverage guarantees, ensuring that a specified proportion of relevant snippets are retained while irrelevant material is filtered out without additional model training.

**Post-Retrieval Context Selection:**

Conformal prediction is applied immediately after retrieval, offering formal control over context composition and context size. FILCO (Filter Context) enhances retrieval granularity by filtering irrelevant or low-utility spans from retrieved passages before generation, improving the faithfulness and efficiency of RAG outputs.

**Current State (2025-2026):**

As of 2025-2026, RAG has moved into a Modular and Agentic phase, with modern systems that are no longer linear; they are iterative and self-correcting. Sparse Context Selection (Zhu et al., 2025) emphasizes efficient sparse reformulations for both recall and speed.

The research indicates significant progress in combining formal theoretical guarantees with practical context optimization techniques in RAG systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb0b592a-2445-417e-923d-9c49f1cfdbf7",
  "isSidechain": false,
  "promptId": "5d3abe21-235c-45be-ad4b-bb4a82a5a4e1",
  "type": "user",
  "uuid": "c49d0703-6693-4663-8398-40314f57cb05",
  "toolUseResult": {
    "query": "RAG post-retrieval context selection optimization formal guarantees 2025 2026 survey",
    "results": [
      {
        "tool_use_id": "srvtoolu_014jG33zR27CnTQtdg2HKBD1",
        "content": [
          {
            "title": "AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG",
            "url": "https://arxiv.org/pdf/2512.25052"
          },
          {
            "title": "Retrieval-Augmented Generation: A Comprehensive Survey of Architectures, Enhancements, and Robustness Frontiers",
            "url": "https://arxiv.org/html/2506.00054v1"
          },
          {
            "title": "awesome-generative-ai-guide/research_updates/rag_research_table.md at main · aishwaryanr/awesome-generative-ai-guide",
            "url": "https://github.com/aishwaryanr/awesome-generative-ai-guide/blob/main/research_updates/rag_research_table.md"
          },
          {
            "title": "Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction",
            "url": "https://arxiv.org/pdf/2511.17908"
          },
          {
            "title": "(PDF) The Evolution of Retrieval-Augmented Generation (RAG) in AI",
            "url": "https://www.researchgate.net/publication/399423892_The_Evolution_of_Retrieval-Augmented_Generation_RAG_in_AI"
          },
          {
            "title": "From RAG to Context - A 2025 year-end review of RAG | RAGFlow",
            "url": "https://ragflow.io/blog/rag-review-2025-from-rag-to-context"
          },
          {
            "title": "Ranking Free RAG: Replacing Re-ranking with Selection in RAG for Sensitive Domains",
            "url": "https://arxiv.org/pdf/2505.16014"
          }
        ]
      },
      "The search returned several highly relevant results on RAG post-retrieval context selection optimization with formal guarantees from 2025-2026. Here's what I found:\n\n## Key Research Areas\n\n**Formal Guarantees & Theoretical Analysis:**\n\nAdaGReS proposes a theoretical analysis showing that the proposed objective exhibits ε-approximate submodularity under practical embedding similarity conditions, yielding near-optimality guarantees for greedy selection. Additionally, context engineering through conformal prediction provides finite-sample coverage guarantees, ensuring that a specified proportion of relevant snippets are retained while irrelevant material is filtered out without additional model training.\n\n**Post-Retrieval Context Selection:**\n\nConformal prediction is applied immediately after retrieval, offering formal control over context composition and context size. FILCO (Filter Context) enhances retrieval granularity by filtering irrelevant or low-utility spans from retrieved passages before generation, improving the faithfulness and efficiency of RAG outputs.\n\n**Current State (2025-2026):**\n\nAs of 2025-2026, RAG has moved into a Modular and Agentic phase, with modern systems that are no longer linear; they are iterative and self-correcting. Sparse Context Selection (Zhu et al., 2025) emphasizes efficient sparse reformulations for both recall and speed.\n\nThe research indicates significant progress in combining formal theoretical guarantees with practical context optimization techniques in RAG systems."
    ],
    "durationSeconds": 7.880241496999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "eb0b592a-2445-417e-923d-9c49f1cfdbf7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-30T07:12:58.077Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QUL3Y7PTr1QGZBvGAoeQqH`</summary>

```json
{
  "query": "Vendi-RAG vendi score diversity quality RAG 2025 multi-hop"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c49d0703-6693-4663-8398-40314f57cb05",
  "isSidechain": false,
  "requestId": "req_011CbYLbLCfqr7m7tF7WZY8W",
  "type": "assistant",
  "uuid": "e19d3d87-a721-499a-936c-0080ea4ef941",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BB1QUM3DHeFXaW5g4c3a9R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 842,
      "cache_read_input_tokens": 26145,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 842,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 26145,
          "cache_creation_input_tokens": 842,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 842
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

_source line 36 · 2026-05-30T07:13:05.351Z_

<details><summary>↩ Tool result · `toolu_01QUL3Y7PTr1QGZBvGAoeQqH`</summary>

```text
Web search results for query: "Vendi-RAG vendi score diversity quality RAG 2025 multi-hop"

Links: [{"title":"Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs","url":"https://arxiv.org/html/2502.11228v2"},{"title":"[2502.11228] Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs","url":"https://arxiv.org/abs/2502.11228"},{"title":"[Literature Review] Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs","url":"https://www.themoonlight.io/en/review/vendi-rag-adaptively-trading-off-diversity-and-quality-significantly-improves-retrieval-augmented-generation-with-llms"},{"title":"(PDF) Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs","url":"https://www.researchgate.net/publication/389090989_Vendi-RAG_Adaptively_Trading-Off_Diversity_And_Quality_Significantly_Improves_Retrieval_Augmented_Generation_With_LLMs"},{"title":"Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs | Papers With Code","url":"https://paperswithcode.com/paper/vendi-rag-adaptively-trading-off-diversity"},{"title":"Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs | Article Information | J-GLOBAL","url":"https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=202502218784102922"},{"title":"dblp: Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs.","url":"https://dblp.org/rec/journals/corr/abs-2502-11228.html"}]

I've found relevant search results about Vendi-RAG. Here's what the research shows:

## Overview

Vendi-RAG is a framework based on an iterative process that jointly optimizes retrieval diversity and answer quality. The paper was presented by Mohammad R. Rezaei and Adji Bousso Dieng, focusing on improving retrieval-augmented generation in large language models, particularly for multi-hop question-answering tasks.

## Core Problem

Traditional RAG systems primarily focus on relevance-based retrieval and often struggle with redundancy, especially when reasoning requires connecting information from multiple sources.

## Key Innovation

Vendi-RAG leverages the Vendi Score (VS), a flexible similarity-based diversity metric, to promote semantic diversity in document retrieval. It then uses an LLM judge that evaluates candidate answers, generated after a reasoning step, and outputs a score that the retriever uses to balance relevance and diversity among the retrieved documents during each iteration.

## Performance Results

Experiments on three challenging datasets -- HotpotQA, MuSiQue, and 2WikiMultiHopQA -- demonstrate Vendi-RAG's effectiveness in multi-hop reasoning tasks, with accuracy increases reaching up to +4.2% on HotpotQA, +4.1% on 2WikiMultiHopQA, and +1.3% on MuSiQue compared to Adaptive-RAG.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e19d3d87-a721-499a-936c-0080ea4ef941",
  "isSidechain": false,
  "promptId": "5d3abe21-235c-45be-ad4b-bb4a82a5a4e1",
  "type": "user",
  "uuid": "3a431509-6cbb-4e64-96cf-aed60b372afb",
  "toolUseResult": {
    "query": "Vendi-RAG vendi score diversity quality RAG 2025 multi-hop",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UkyJxhTxWRTHbLKmBKrrBh",
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
            "title": "[Literature Review] Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs",
            "url": "https://www.themoonlight.io/en/review/vendi-rag-adaptively-trading-off-diversity-and-quality-significantly-improves-retrieval-augmented-generation-with-llms"
          },
          {
            "title": "(PDF) Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs",
            "url": "https://www.researchgate.net/publication/389090989_Vendi-RAG_Adaptively_Trading-Off_Diversity_And_Quality_Significantly_Improves_Retrieval_Augmented_Generation_With_LLMs"
          },
          {
            "title": "Vendi-RAG: Adaptively Trading-Off Diversity And Quality Significantly Improves Retrieval Augmented Generation With LLMs | Papers With Code",
            "url": "https://paperswithcode.com/paper/vendi-rag-adaptively-trading-off-diversity"
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
      "I've found relevant search results about Vendi-RAG. Here's what the research shows:\n\n## Overview\n\nVendi-RAG is a framework based on an iterative process that jointly optimizes retrieval diversity and answer quality. The paper was presented by Mohammad R. Rezaei and Adji Bousso Dieng, focusing on improving retrieval-augmented generation in large language models, particularly for multi-hop question-answering tasks.\n\n## Core Problem\n\nTraditional RAG systems primarily focus on relevance-based retrieval and often struggle with redundancy, especially when reasoning requires connecting information from multiple sources.\n\n## Key Innovation\n\nVendi-RAG leverages the Vendi Score (VS), a flexible similarity-based diversity metric, to promote semantic diversity in document retrieval. It then uses an LLM judge that evaluates candidate answers, generated after a reasoning step, and outputs a score that the retriever uses to balance relevance and diversity among the retrieved documents during each iteration.\n\n## Performance Results\n\nExperiments on three challenging datasets -- HotpotQA, MuSiQue, and 2WikiMultiHopQA -- demonstrate Vendi-RAG's effectiveness in multi-hop reasoning tasks, with accuracy increases reaching up to +4.2% on HotpotQA, +4.1% on 2WikiMultiHopQA, and +1.3% on MuSiQue compared to Adaptive-RAG."
    ],
    "durationSeconds": 7.269584722999992,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e19d3d87-a721-499a-936c-0080ea4ef941",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition  ## Core Problem  How can post-retrieval context composition for RAG be formalized as a constrained non-monotone…",
  "leafUuid": "3a431509-6cbb-4e64-96cf-aed60b372afb",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Non-monotone submodular context composition for RAG",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7"
}
```

---

### Tool call

_source line 39 · 2026-05-30T07:13:08.206Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017fSM1BRbKZXpcZp167BvaC`</summary>

```json
{
  "query": "submodular context selection in-context learning RAG passage reranking 2025 2026 recent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a431509-6cbb-4e64-96cf-aed60b372afb",
  "isSidechain": false,
  "requestId": "req_011CbYLc5iZemMtUgC32SABt",
  "type": "assistant",
  "uuid": "d9efb253-97b1-47aa-bfe5-88f4d0452e52",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QNSsXKD8YfD1tgn44n34T7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 995,
      "cache_read_input_tokens": 26987,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 995,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 26987,
          "cache_creation_input_tokens": 995,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 995
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

_source line 40 · 2026-05-30T07:13:16.812Z_

<details><summary>↩ Tool result · `toolu_017fSM1BRbKZXpcZp167BvaC`</summary>

```text
Web search results for query: "submodular context selection in-context learning RAG passage reranking 2025 2026 recent"

Links: [{"title":"Submodular Optimization for Text Selection, Passage Reranking & Context Engineering","url":"https://jina.ai/news/submodular-optimization-for-text-selection-passage-reranking-context-engineering/"},{"title":"Submodular Context Partitioning and Compression for In-Context Learning","url":"https://arxiv.org/pdf/2510.05130"},{"title":"From Ranking to Selection: A Simple but Efficient Dynamic Passage Selector for Retrieval Augmented Generation","url":"https://arxiv.org/pdf/2508.09497"},{"title":"Retrieval-Augmented Generation: A Comprehensive Survey of Architectures, Enhancements, and Robustness Frontiers","url":"https://arxiv.org/html/2506.00054v1"},{"title":"Optimizing RAG Rerankers with LLM Feedback via Reinforcement Learning","url":"https://arxiv.org/pdf/2604.02091"},{"title":"Context-Picker: Dynamic context selection using multi-stage reinforcement learning","url":"https://arxiv.org/pdf/2512.14465"},{"title":"AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG","url":"https://arxiv.org/pdf/2512.25052"},{"title":"From RAG to Context - A 2025 year-end review of RAG | RAGFlow","url":"https://ragflow.io/blog/rag-review-2025-from-rag-to-context"}]

Based on the search results, here's what I found on submodular context selection in in-context learning and RAG passage reranking from 2025-2026:

## Recent Research Highlights

### Submodular Context Partitioning for In-Context Learning

Submodular Context Partitioning (Sub-CP) is a block-aware context selection framework that leverages submodular objectives to control the degree of diversity within each block. Extensive experiments across diverse tasks on multiple datasets show that Sub-CP consistently improves performance across model scales.

### Submodular Optimization for Context Engineering

Submodular optimization provides a principled framework with theoretical guarantees for better context engineering. Text selection and passage reranking are integral components of context engineering, particularly in the processes of knowledge base selection, retrieval, and context compression.

### Recent RAG Context Selection Advances

Recent LLM-based rerankers leverage query-aware, list-aware, or generator-aware signals to score and filter contexts. Additionally, recent work provides theoretical analysis and proof of ε-approximate submodularity for context selection objectives, offering theoretical guarantees for the near-global optimality of the greedy selection algorithm.

A persistent challenge in RAG is ensuring that retrieved results are not only highly relevant to queries but also exhibit sufficient diversity in content, as systems tend to return overlapping or near-duplicate chunks under top-k retrieval.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9efb253-97b1-47aa-bfe5-88f4d0452e52",
  "isSidechain": false,
  "promptId": "5d3abe21-235c-45be-ad4b-bb4a82a5a4e1",
  "type": "user",
  "uuid": "e35e0b23-d512-4cf4-85c3-4f027f0c4870",
  "toolUseResult": {
    "query": "submodular context selection in-context learning RAG passage reranking 2025 2026 recent",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TEdVdjeAK6vBBCP6mC4dKt",
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
            "title": "From Ranking to Selection: A Simple but Efficient Dynamic Passage Selector for Retrieval Augmented Generation",
            "url": "https://arxiv.org/pdf/2508.09497"
          },
          {
            "title": "Retrieval-Augmented Generation: A Comprehensive Survey of Architectures, Enhancements, and Robustness Frontiers",
            "url": "https://arxiv.org/html/2506.00054v1"
          },
          {
            "title": "Optimizing RAG Rerankers with LLM Feedback via Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2604.02091"
          },
          {
            "title": "Context-Picker: Dynamic context selection using multi-stage reinforcement learning",
            "url": "https://arxiv.org/pdf/2512.14465"
          },
          {
            "title": "AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG",
            "url": "https://arxiv.org/pdf/2512.25052"
          },
          {
            "title": "From RAG to Context - A 2025 year-end review of RAG | RAGFlow",
            "url": "https://ragflow.io/blog/rag-review-2025-from-rag-to-context"
          }
        ]
      },
      "Based on the search results, here's what I found on submodular context selection in in-context learning and RAG passage reranking from 2025-2026:\n\n## Recent Research Highlights\n\n### Submodular Context Partitioning for In-Context Learning\n\nSubmodular Context Partitioning (Sub-CP) is a block-aware context selection framework that leverages submodular objectives to control the degree of diversity within each block. Extensive experiments across diverse tasks on multiple datasets show that Sub-CP consistently improves performance across model scales.\n\n### Submodular Optimization for Context Engineering\n\nSubmodular optimization provides a principled framework with theoretical guarantees for better context engineering. Text selection and passage reranking are integral components of context engineering, particularly in the processes of knowledge base selection, retrieval, and context compression.\n\n### Recent RAG Context Selection Advances\n\nRecent LLM-based rerankers leverage query-aware, list-aware, or generator-aware signals to score and filter contexts. Additionally, recent work provides theoretical analysis and proof of ε-approximate submodularity for context selection objectives, offering theoretical guarantees for the near-global optimality of the greedy selection algorithm.\n\nA persistent challenge in RAG is ensuring that retrieved results are not only highly relevant to queries but also exhibit sufficient diversity in content, as systems tend to return overlapping or near-duplicate chunks under top-k retrieval."
    ],
    "durationSeconds": 8.601461085000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d9efb253-97b1-47aa-bfe5-88f4d0452e52",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-30T07:13:19.533Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017QuG1MsuijVEBy6MkQQoqT`</summary>

```json
{
  "query": "context distraction interference RAG passage selection set-level optimization 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e35e0b23-d512-4cf4-85c3-4f027f0c4870",
  "isSidechain": false,
  "requestId": "req_011CbYLcvjM9XNJuKPKFtok9",
  "type": "assistant",
  "uuid": "aaf5a5dc-87ad-47d1-bc9a-a750a0373ce9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FrwryxQcjqkbdwKf2RfGfd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 27982,
      "output_tokens": 66,
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
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 27982,
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

_source line 42 · 2026-05-30T07:13:26.361Z_

<details><summary>↩ Tool result · `toolu_017QuG1MsuijVEBy6MkQQoqT`</summary>

```text
Web search results for query: "context distraction interference RAG passage selection set-level optimization 2026"

Links: [{"title":"BEYOND RAG VS. LONG-CONTEXT: LEARNING DISTRACTION ...","url":"https://openreview.net/pdf/e5a4bed78735b15352c5bcbf4d82c0c9e8638922.pdf"},{"title":"In-Context Retrieval-Augmented Generation (RAG)","url":"https://www.emergentmind.com/topics/in-context-retrieval-augmented-generation-rag"},{"title":"Preprint. BEYOND RAG VS. LONG-CONTEXT: LEARNING DISTRACTION-AWARE RETRIEVAL FOR","url":"https://arxiv.org/pdf/2509.21865"},{"title":"Resisting Contextual Interference in RAG via Parametric- ...","url":"https://arxiv.org/pdf/2506.05154"},{"title":"Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating Distractors and Positional Bias","url":"https://arxiv.org/html/2512.14313v1"},{"title":"Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating Distractors and Positional Bias","url":"https://arxiv.org/pdf/2512.14313"},{"title":"The Distracting Effect: Understanding Irrelevant Passages in RAG","url":"https://arxiv.org/pdf/2505.06914"}]

I found several relevant research papers and articles on this topic. Here's what the search reveals:

## Key Research Areas

**Distraction-Aware RAG Retrieval**: Recent work presents a lightweight retriever that learns to select passages to minimize potential interference from distracting passages, solely based on the similarity between the query and passages.

**Set-Level Optimization with Curriculum Learning**: Recent RL frameworks encourage models to optimize for answer factuality and passage-level citation faithfulness under realistic retrieval scenarios with distractors, with samples assigned levels of difficulty based on the number of supporting passages and distractor passages included in the retrieval set.

**Dynamic Context Selection**: Research systematically analyzes the impact of distractors on generation quality and quantifies their effects under varying conditions, while investigating how the position of relevant passages within the context window affects their influence on generation.

**Hard Distractor Passages**: Recent work moves beyond simple binary classification of irrelevant passages and develops multiple methods for finding hard distracting passages, providing a comprehensive framework for identifying and utilizing them.

These results show active research in 2025-2026 on addressing contextual interference in RAG systems through passage selection optimization, curriculum learning approaches, and dynamic context sizing strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aaf5a5dc-87ad-47d1-bc9a-a750a0373ce9",
  "isSidechain": false,
  "promptId": "5d3abe21-235c-45be-ad4b-bb4a82a5a4e1",
  "type": "user",
  "uuid": "63283952-69da-495b-9de6-8d2ff5d1f57e",
  "toolUseResult": {
    "query": "context distraction interference RAG passage selection set-level optimization 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01K9zRvrJwhHx6Qdm6sUbyFU",
        "content": [
          {
            "title": "BEYOND RAG VS. LONG-CONTEXT: LEARNING DISTRACTION ...",
            "url": "https://openreview.net/pdf/e5a4bed78735b15352c5bcbf4d82c0c9e8638922.pdf"
          },
          {
            "title": "In-Context Retrieval-Augmented Generation (RAG)",
            "url": "https://www.emergentmind.com/topics/in-context-retrieval-augmented-generation-rag"
          },
          {
            "title": "Preprint. BEYOND RAG VS. LONG-CONTEXT: LEARNING DISTRACTION-AWARE RETRIEVAL FOR",
            "url": "https://arxiv.org/pdf/2509.21865"
          },
          {
            "title": "Resisting Contextual Interference in RAG via Parametric- ...",
            "url": "https://arxiv.org/pdf/2506.05154"
          },
          {
            "title": "Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating Distractors and Positional Bias",
            "url": "https://arxiv.org/html/2512.14313v1"
          },
          {
            "title": "Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating Distractors and Positional Bias",
            "url": "https://arxiv.org/pdf/2512.14313"
          },
          {
            "title": "The Distracting Effect: Understanding Irrelevant Passages in RAG",
            "url": "https://arxiv.org/pdf/2505.06914"
          }
        ]
      },
      "I found several relevant research papers and articles on this topic. Here's what the search reveals:\n\n## Key Research Areas\n\n**Distraction-Aware RAG Retrieval**: Recent work presents a lightweight retriever that learns to select passages to minimize potential interference from distracting passages, solely based on the similarity between the query and passages.\n\n**Set-Level Optimization with Curriculum Learning**: Recent RL frameworks encourage models to optimize for answer factuality and passage-level citation faithfulness under realistic retrieval scenarios with distractors, with samples assigned levels of difficulty based on the number of supporting passages and distractor passages included in the retrieval set.\n\n**Dynamic Context Selection**: Research systematically analyzes the impact of distractors on generation quality and quantifies their effects under varying conditions, while investigating how the position of relevant passages within the context window affects their influence on generation.\n\n**Hard Distractor Passages**: Recent work moves beyond simple binary classification of irrelevant passages and develops multiple methods for finding hard distracting passages, providing a comprehensive framework for identifying and utilizing them.\n\nThese results show active research in 2025-2026 on addressing contextual interference in RAG systems through passage selection optimization, curriculum learning approaches, and dynamic context sizing strategies."
    ],
    "durationSeconds": 6.824124636000023,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "aaf5a5dc-87ad-47d1-bc9a-a750a0373ce9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-30T07:13:29.587Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LmjLcrjLkPNudiL5q7cWLC`</summary>

```json
{
  "query": "\"dynamic context selection\" \"mitigating distractors\" RAG arXiv 2512.14313 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63283952-69da-495b-9de6-8d2ff5d1f57e",
  "isSidechain": false,
  "requestId": "req_011CbYLdddyCMXvY2vBgdE5i",
  "type": "assistant",
  "uuid": "ea5159a4-20e9-4170-b38a-0d9a83d29ffc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XwgR1cTb6QEHYrCnuUEZwk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 727,
      "cache_read_input_tokens": 28811,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 28811,
          "cache_creation_input_tokens": 727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 727
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

_source line 44 · 2026-05-30T07:13:36.484Z_

<details><summary>↩ Tool result · `toolu_01LmjLcrjLkPNudiL5q7cWLC`</summary>

```text
Web search results for query: ""dynamic context selection" "mitigating distractors" RAG arXiv 2512.14313 2025"

Links: [{"title":"[2512.14313] Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating Distractors and Positional Bias","url":"https://arxiv.org/abs/2512.14313"},{"title":"Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating","url":"https://arxiv.org/pdf/2512.14313"},{"title":"Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating Distractors and Positional Bias","url":"https://arxiv.org/html/2512.14313v1"},{"title":"Dynamic context selection using multi-stage reinforcement ...","url":"https://arxiv.org/pdf/2512.14465"},{"title":"Context-Picker: Dynamic Context Selection Using Multi-stage Reinforcement Learning","url":"https://arxiv.org/html/2512.14465"},{"title":"[2512.10787v1] Replace, Don't Expand: Mitigating Context Dilution in Multi-Hop RAG via Fixed-Budget Evidence Assembly","url":"https://arxiv.org/abs/2512.10787v1"}]

I found the paper you were looking for! Here's what the search revealed:

"Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating Distractors and Positional Bias" is arXiv paper 2512.14313, submitted on December 16, 2025, with authors Malika Iratni, Mohand Boughanem, and Taoufiq Dkaki.

The paper addresses two key challenges in RAG systems:

1. **Distractors**: Standard RAG systems typically rely on a fixed top k retrieval strategy, which can either miss relevant information or introduce semantically irrelevant passages, known as distractors, that degrade output quality.

2. **Positional Bias**: The positioning of retrieved passages within the input context can influence the model attention and generation outcomes. Context placed in the middle tends to be overlooked, which is an issue known as the "lost in the middle" phenomenon.

The work systematically analyzes the impact of distractors on generation quality, and quantifies their effects under varying conditions.

You can access the paper directly at https://arxiv.org/abs/2512.14313.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea5159a4-20e9-4170-b38a-0d9a83d29ffc",
  "isSidechain": false,
  "promptId": "5d3abe21-235c-45be-ad4b-bb4a82a5a4e1",
  "type": "user",
  "uuid": "86fc47b2-993c-4339-b957-8d9c0586fe1a",
  "toolUseResult": {
    "query": "\"dynamic context selection\" \"mitigating distractors\" RAG arXiv 2512.14313 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01F4qU9Wgi99chhViGHk3hh9",
        "content": [
          {
            "title": "[2512.14313] Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating Distractors and Positional Bias",
            "url": "https://arxiv.org/abs/2512.14313"
          },
          {
            "title": "Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating",
            "url": "https://arxiv.org/pdf/2512.14313"
          },
          {
            "title": "Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating Distractors and Positional Bias",
            "url": "https://arxiv.org/html/2512.14313v1"
          },
          {
            "title": "Dynamic context selection using multi-stage reinforcement ...",
            "url": "https://arxiv.org/pdf/2512.14465"
          },
          {
            "title": "Context-Picker: Dynamic Context Selection Using Multi-stage Reinforcement Learning",
            "url": "https://arxiv.org/html/2512.14465"
          },
          {
            "title": "[2512.10787v1] Replace, Don't Expand: Mitigating Context Dilution in Multi-Hop RAG via Fixed-Budget Evidence Assembly",
            "url": "https://arxiv.org/abs/2512.10787v1"
          }
        ]
      },
      "I found the paper you were looking for! Here's what the search revealed:\n\n\"Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating Distractors and Positional Bias\" is arXiv paper 2512.14313, submitted on December 16, 2025, with authors Malika Iratni, Mohand Boughanem, and Taoufiq Dkaki.\n\nThe paper addresses two key challenges in RAG systems:\n\n1. **Distractors**: Standard RAG systems typically rely on a fixed top k retrieval strategy, which can either miss relevant information or introduce semantically irrelevant passages, known as distractors, that degrade output quality.\n\n2. **Positional Bias**: The positioning of retrieved passages within the input context can influence the model attention and generation outcomes. Context placed in the middle tends to be overlooked, which is an issue known as the \"lost in the middle\" phenomenon.\n\nThe work systematically analyzes the impact of distractors on generation quality, and quantifies their effects under varying conditions.\n\nYou can access the paper directly at https://arxiv.org/abs/2512.14313."
    ],
    "durationSeconds": 6.891313491000008,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ea5159a4-20e9-4170-b38a-0d9a83d29ffc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-30T07:15:14.624Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the research landscape. Let me synthesize my findings and evaluate this proposal.

Key observations from my research:

1. **AdaGReS** (Dec 2025): Provides ε-approximate submodularity for redundancy-penalized greedy context selection, but only handles monotone objectives. Evaluated on NQ and a biomedical corpus.

2. **The Distracting Effect** (ACL 2025): Provides per-passage distraction measurement DE_q(p), but no set-level optimization.

3. **AAMAS 2026 γ-weakly DR-submodular**: Provides approximation guarantees for non-monotone γ-weakly DR-submodular functions, but no NLP applications.
   
4. **CCBQP** (Apr 2026): Uses Frank-Wolfe optimization for diversity-aware retrieval with a relevance-diversity tradeoff, though it lacks a distraction component.

5. **LDAR** (ICLR 2026): Incorporates distraction awareness into retrieval but doesn't provide formal guarantees or handle post-retrieval composition.

6. **DynamicRAG** (NeurIPS 2025) and **Vendi-RAG** (Feb 2025): Both use heuristic approaches—reinforcement learning and diversity scoring respectively—without formal theoretical guarantees or explicit handling of redundancy and distraction together.

7. **Qian (2019)** and **Dynamic Context Selection** (Dec 2025): The former studies the theoretical problem of approximately submodular minus modular functions, while the latter analyzes distractor impact empirically but lacks a formal optimization framework.

Now I'm checking whether my proposal genuinely fills a gap. The key claim is that no existing method combines post-retrieval composition, formal theoretical grounding, and distraction-awareness simultaneously. Looking at the landscape, this gap appears real—each method handles one or two of these aspects but not all three together. The specific application of the submodular minus modular framework to RAG with distraction-aware objectives seems to be novel in this context.

However, I need to be honest about potential weaknesses. The core novelty might be viewed as primarily a combination of existing building blocks rather than a fundamentally new insight. While I do derive the γ-weak DR-submodularity parameter for this specific RAG objective, the overall framework—decomposing the objective into relevance, redundancy, and distraction components, then applying known optimization algorithms—is relatively straightforward. A reviewer could reasonably argue this is a clean but somewhat expected application of existing optimization theory to NLP.

There's also the modular distraction assumption to consider. I'm using per-passage distraction rather than set-conditional distraction, which is a significant simplification that makes the theory tractable. If set-conditional distraction turns out to be substantially better empirically, that would undermine the theoretical contribution.

The practical viability of the theoretical guarantees hinges on γ values being reasonable. If γ turns out to be small in practice—which seems likely when candidate pools contain near-duplicate passages—the formal guarantees could become vacuous, which is a real concern. And fundamentally, I should ask whether the redundancy-distraction decomposition itself is a deep insight or just a natural modeling choice extending existing relevance-diversity trade-offs.

The gap identification is solid and the two-camp analysis is accurate. The proposal thoughtfully addresses why a simple two-stage pipeline wouldn't work, and the theoretical contribution is genuinely non-trivial if γ values hold up in practice.

Now I'm considering how to sharpen the novelty claim—framing this as the first instantiation of a known problem class in NLP is valid but potentially weak. Could the real novelty lie in identifying structural properties of RAG that make this instantiation non-trivial? There's also potential to amplify significance by developing the broader context engineering angle across ICL and tool-use as a general framework. And rather than treating small γ as a weakness, I could reframe it as a diagnostic feature—the framework reveals when guarantees degrade and why, which itself is a valuable insight. Actually, looking at this proposal again more carefully, it's already quite mature. The research landscape analysis is thorough, the trivial alternative is addressed, the experimental design is comprehensive. Let me think about whether there are genuine discovery points.

**Key question: Is this proposal's novelty claim defensible against the "clean application" criticism?**

The reviewer argument would be: "You took AdaGReS's objective, subtracted a modular distraction term, and applied known non-monotone optimization algorithms. The theoretical contribution is deriving γ, but this is a relatively mechanical computation given the bounded-embedding conditions. What's the surprise?"

The defense would need to be: either (a) the γ derivation reveals something unexpected about when/why distraction-aware composition benefits from joint optimization, or (b) the empirical results show the framework works significantly better than the two-stage alternative, validating the necessity of joint optimization.

I think the real discovery point is sharpening why joint optimization actually matters at a conceptual level, not just claiming it's theoretically cleaner. There's also something worth investigating about how redundancy and distraction interact — the current objective treats them as independent additive penalties, but what if a passage is simultaneously redundant and distracting? Could there be amplification effects where distraction becomes more harmful when combined with other distracting passages? The objective function is deceptively simple, and this interaction might be a genuine theoretical insight. This distinction between capacity waste and active interference could be formalized as a core contribution with different scaling properties and mitigation strategies. I'm also noticing some related work gaps—conformal prediction approaches to context selection seem relevant but aren't discussed, and the proposal's handling of non-monotone approximately submodular functions might need more careful positioning relative to existing work on this problem class. ε-approximate submodularity doesn't guarantee monotonicity—it's about diminishing returns—but AdaGReS applies monotone greedy, which does require it. The objective might be non-monotone in highly redundant settings, though AdaGReS likely assumes conditions that ensure monotonicity. I should focus on the idea-level contributions rather than getting lost in these technical details. Overall, this proposal is quite mature with a clear gap, solid theoretical framing, and comprehensive experiments, though I'm starting to spot some potential limitations.

There are a few angles worth sharpening: the novelty could move beyond "first combination" to reveal what the empirically measured γ actually tells us about context composition in RAG; the distraction-redundancy decomposition might generalize as a broader principle for context engineering; there's a gap around conformal prediction methods that offer statistical rather than worst-case guarantees; and there's an interesting question about when formal optimization actually matters in practice versus simpler heuristics.

Reconsidering the conformal prediction connection — it's really addressing a different problem around coverage guarantees rather than composition optimization, so the relationship is probably weaker than I initially thought. The strongest angles are positioning γ itself as a diagnostic tool that characterizes optimization difficulty for a given query, and exploring how the framework generalizes beyond RAG to broader context engineering challenges. alization**: The broader motivation mentions ICL, tool-use, multi-document grounding. If the framework can be positioned as a general "non-monotone context composition" framework with RAG as the first instantiation, significance increases substantially.

3. **Related work gap**: One work I haven't seen discussed is the use of submodular optimization specifically for RAG diversity in the Jina blog context — this suggests industry interest in the approach. More importantly, the proposal should address how it relates to the "replace, don't expand" paradigm (arXiv 2512.10787) which takes a different approach to the same problem (fixed-budget evidence assembly for multi-hop RAG). This work replaces low-quality passages rather than expanding the context, which is a different paradigm but addresses the same concern about adding passages potentially hurting performance. The proposal should clarify how the non-monotone submodular framework relates to or potentially subsumes this approach.

Now I'm thinking more carefully about the trivial alternative argument. The proposal claims joint optimization is necessary because pre-filtering forfeits optimality guarantees, which is theoretically sound, but practically speaking, a passage with very high diversity and low relevance would likely be rejected by joint optimization anyway. The real question is how often the joint approach makes different decisions than a two-stage pipeline — if that happens rarely, the practical gains might be modest despite the theoretical advantage. The proposal plans an ablation to test this, which is good, but the core argument could be strengthened by identifying specific conditions where the two approaches diverge meaningfully.

I think I have enough to structure my assessment now. The proposal is mature and well-developed with genuine gap identification, and there are a few discovery points worth exploring to strengthen the core framing rather than the technical execution.

The first opportunity is to position γ not just as a technical parameter but as a diagnostic tool that reveals when formal non-monotone optimization becomes essential for context composition—shifting from "we applied theory to a domain" to "we've uncovered structural properties of the problem."

Second, the framework's decomposition principle could generalize beyond RAG to ICL, tool-use, and multi-document grounding, which would significantly amplify the contribution's significance if demonstrated.

Third, the redundancy-distraction decomposition itself could be elevated as a core contribution by framing it as a principled answer to why adding context hurts—showing these are two independent failure modes with distinct scaling behaviors and mitigation strategies. Though I'm wondering whether the additive penalty assumption actually supports the independence claim, or if there's interaction between redundancy and distraction that the model isn't capturing.

I should also check whether this specific decomposition or objective function has been proposed elsewhere.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86fc47b2-993c-4339-b957-8d9c0586fe1a",
  "isSidechain": false,
  "requestId": "req_011CbYLeNrFqcQogQEAZUVxz",
  "type": "assistant",
  "uuid": "a648b27c-90bc-47af-b94c-eff8334d2902",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PRUkJdwdtDR7J2xNDM4yUW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 686,
      "cache_read_input_tokens": 29538,
      "output_tokens": 3822,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 686,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3822,
          "cache_read_input_tokens": 29538,
          "cache_creation_input_tokens": 686,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 686
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

_source line 46 · 2026-05-30T07:15:14.626Z_

Let me do one more targeted search to check for any work that might have already proposed a similar redundancy-distraction decomposition or objective.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a648b27c-90bc-47af-b94c-eff8334d2902",
  "isSidechain": false,
  "requestId": "req_011CbYLeNrFqcQogQEAZUVxz",
  "type": "assistant",
  "uuid": "bd45d8e5-024e-4288-b44a-908e01f07e3d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PRUkJdwdtDR7J2xNDM4yUW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 686,
      "cache_read_input_tokens": 29538,
      "output_tokens": 3822,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 686,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3822,
          "cache_read_input_tokens": 29538,
          "cache_creation_input_tokens": 686,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 686
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

_source line 47 · 2026-05-30T07:15:14.628Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0134XMo6BZuxdTf4gkzALNp2`</summary>

```json
{
  "query": "redundancy distraction decomposition context selection RAG relevance diversity distraction penalty joint optimization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd45d8e5-024e-4288-b44a-908e01f07e3d",
  "isSidechain": false,
  "requestId": "req_011CbYLeNrFqcQogQEAZUVxz",
  "type": "assistant",
  "uuid": "65248431-d99f-4fe0-a99c-7fa04e7829b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PRUkJdwdtDR7J2xNDM4yUW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 686,
      "cache_read_input_tokens": 29538,
      "output_tokens": 3822,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 686,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3822,
          "cache_read_input_tokens": 29538,
          "cache_creation_input_tokens": 686,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 686
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

_source line 48_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition  ## Core Problem  How can post-retrieval context composition for RAG be formalized as a constrained non-monotone…",
  "leafUuid": "65248431-d99f-4fe0-a99c-7fa04e7829b0",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7"
}
```

---

### Runtime record

_source line 49_

```json
{
  "type": "ai-title",
  "aiTitle": "Non-monotone submodular context composition for RAG",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7"
}
```

---

### Tool result

_source line 50 · 2026-05-30T07:15:23.059Z_

<details><summary>↩ Tool result · `toolu_0134XMo6BZuxdTf4gkzALNp2`</summary>

```text
Web search results for query: "redundancy distraction decomposition context selection RAG relevance diversity distraction penalty joint optimization"

Links: [{"title":"AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG","url":"https://arxiv.org/pdf/2512.25052"},{"title":"Scaling DPPs for RAG: Density Meets Diversity","url":"https://arxiv.org/pdf/2604.03240"},{"title":"SMART-RAG: Selection using Determinantal Matrices for Augmented   Retrieval","url":"https://arxiv.org/pdf/2409.13992"},{"title":"Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating Distractors and Positional Bias","url":"https://arxiv.org/pdf/2512.14313"},{"title":"RAGSmith: A Framework for Finding the Optimal Composition of","url":"https://arxiv.org/pdf/2511.01386"},{"title":"Structure and Diversity Aware Context Bubble Construction for Enterprise Retrieval Augmented Systems","url":"https://arxiv.org/pdf/2601.10681"}]

I found several highly relevant research papers on context selection in RAG systems. Here's what the search returned:

**Key Research Papers:**

1. **AdaGReS** - A redundancy-aware context selection framework for token-budgeted RAG that optimizes a set-level objective combining query-chunk relevance and intra-set redundancy penalties. AdaGReS performs greedy selection under a token-budget constraint using marginal gains derived from the objective, and introduces a closed-form, instance-adaptive calibration of the relevance-redundancy trade-off parameter.

2. **Scaling DPPs for RAG** - This paper addresses how redundancy dilutes the effective token budget and constrains the generator to reason over a narrow semantic slice. It proposes using Determinantal Point Processes (DPPs) with a dynamic kernel construction mechanism for complementarity-aware chunk selection.

3. **SMART-RAG** - One of the key challenges in RAG is selecting contexts that are not only relevant but also diverse and free of contradictions. The key innovation of SMART lies in its use of Determinantal Point Processes (DPPs) to model relevance, diversity, and conflict relations among retrieved contexts.

4. **Dynamic Context Selection** - RAG systems often suffer from two critical challenges: (i) misleading irrelevant retrieved documents (distractors), that can distort the generation results, and (ii) the 'lost-in-the-middle' phenomenon.

5. **Context Bubble Construction** - A context bubble is constructed through constrained selection that balances query relevance, marginal coverage, and redundancy penalties.

These papers collectively address the core concepts in your search query: redundancy awareness, distraction mitigation, diversity optimization, and joint relevance-diversity objectives in RAG context selection.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65248431-d99f-4fe0-a99c-7fa04e7829b0",
  "isSidechain": false,
  "promptId": "5d3abe21-235c-45be-ad4b-bb4a82a5a4e1",
  "type": "user",
  "uuid": "4f2cee0f-3778-43e0-b798-ef8a1aee68c7",
  "toolUseResult": {
    "query": "redundancy distraction decomposition context selection RAG relevance diversity distraction penalty joint optimization",
    "results": [
      {
        "tool_use_id": "srvtoolu_01C61P4BvrQJ4fqAv5FpEGj7",
        "content": [
          {
            "title": "AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG",
            "url": "https://arxiv.org/pdf/2512.25052"
          },
          {
            "title": "Scaling DPPs for RAG: Density Meets Diversity",
            "url": "https://arxiv.org/pdf/2604.03240"
          },
          {
            "title": "SMART-RAG: Selection using Determinantal Matrices for Augmented   Retrieval",
            "url": "https://arxiv.org/pdf/2409.13992"
          },
          {
            "title": "Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating Distractors and Positional Bias",
            "url": "https://arxiv.org/pdf/2512.14313"
          },
          {
            "title": "RAGSmith: A Framework for Finding the Optimal Composition of",
            "url": "https://arxiv.org/pdf/2511.01386"
          },
          {
            "title": "Structure and Diversity Aware Context Bubble Construction for Enterprise Retrieval Augmented Systems",
            "url": "https://arxiv.org/pdf/2601.10681"
          }
        ]
      },
      "I found several highly relevant research papers on context selection in RAG systems. Here's what the search returned:\n\n**Key Research Papers:**\n\n1. **AdaGReS** - A redundancy-aware context selection framework for token-budgeted RAG that optimizes a set-level objective combining query-chunk relevance and intra-set redundancy penalties. AdaGReS performs greedy selection under a token-budget constraint using marginal gains derived from the objective, and introduces a closed-form, instance-adaptive calibration of the relevance-redundancy trade-off parameter.\n\n2. **Scaling DPPs for RAG** - This paper addresses how redundancy dilutes the effective token budget and constrains the generator to reason over a narrow semantic slice. It proposes using Determinantal Point Processes (DPPs) with a dynamic kernel construction mechanism for complementarity-aware chunk selection.\n\n3. **SMART-RAG** - One of the key challenges in RAG is selecting contexts that are not only relevant but also diverse and free of contradictions. The key innovation of SMART lies in its use of Determinantal Point Processes (DPPs) to model relevance, diversity, and conflict relations among retrieved contexts.\n\n4. **Dynamic Context Selection** - RAG systems often suffer from two critical challenges: (i) misleading irrelevant retrieved documents (distractors), that can distort the generation results, and (ii) the 'lost-in-the-middle' phenomenon.\n\n5. **Context Bubble Construction** - A context bubble is constructed through constrained selection that balances query relevance, marginal coverage, and redundancy penalties.\n\nThese papers collectively address the core concepts in your search query: redundancy awareness, distraction mitigation, diversity optimization, and joint relevance-diversity objectives in RAG context selection."
    ],
    "durationSeconds": 8.421899252000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "65248431-d99f-4fe0-a99c-7fa04e7829b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-30T07:15:25.573Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014irSC7c6utRRnjcUWtcqqa`</summary>

```json
{
  "query": "RAGSmith optimal composition RAG 2025 arXiv 2511.01386"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f2cee0f-3778-43e0-b798-ef8a1aee68c7",
  "isSidechain": false,
  "requestId": "req_011CbYLnEYAafAGbRiVWhQ3F",
  "type": "assistant",
  "uuid": "30c98888-02f2-44e3-8666-54ca94c2827b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LV3y4VUq5HQroQ9JkCJhAx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4539,
      "cache_read_input_tokens": 30224,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4539,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 30224,
          "cache_creation_input_tokens": 4539,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4539
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

_source line 52 · 2026-05-30T07:15:33.076Z_

<details><summary>↩ Tool result · `toolu_014irSC7c6utRRnjcUWtcqqa`</summary>

```text
Web search results for query: "RAGSmith optimal composition RAG 2025 arXiv 2511.01386"

Links: [{"title":"RAGSmith: RAG Pipeline with Genetic Algorithm Optimization","url":"https://github.com/yAquila/RAGSmith"},{"title":"[2511.01386] RAGSmith: A Framework for Finding the Optimal Composition of Retrieval-Augmented Generation Methods Across Datasets","url":"https://arxiv.org/abs/2511.01386"},{"title":"RAGSmith: A Framework for Finding the Optimal Composition of Retrieval-Augmented Generation Methods Across Datasets | Request PDF","url":"https://www.researchgate.net/publication/397231360_RAGSmith_A_Framework_for_Finding_the_Optimal_Composition_of_Retrieval-Augmented_Generation_Methods_Across_Datasets"},{"title":"RAGSmith: A Framework for Finding the Optimal Composition of","url":"https://arxiv.org/pdf/2511.01386"},{"title":"RAGSmith: A Framework for Finding the Optimal Composition of Retrieval-Augmented Generation Methods Across Datasets","url":"https://arxiv.org/html/2511.01386v1"}]

Based on the search results, here's information about RAGSmith and arXiv paper 2511.01386:

RAGSmith is a framework for finding the optimal composition of retrieval-augmented generation methods across datasets, authored by Muhammed Yusuf Kartal, Suha Kagan Kose, Korhan Sevinç, and Burak Aktas, published in November 2025.

## Overview

RAGSmith treats RAG design as an end-to-end architecture search over nine technique families and 46,080 feasible pipeline configurations. A genetic search optimizes a scalar objective that jointly aggregates retrieval metrics (recall@k, mAP, nDCG, MRR) and generation metrics (LLM-Judge and semantic similarity).

## Key Findings

The framework was evaluated on six Wikipedia-derived domains (Mathematics, Law, Finance, Medicine, Defense Industry, Computer Science), and RAGSmith found configurations that consistently outperform naive RAG baseline by +3.8% on average (range +1.2% to +6.9% across domains), with gains up to +12.5% in retrieval and +7.5% in generation.

The search typically explores approximately 0.2% of the space (~100 candidates) and discovers a robust backbone of vector retrieval plus post-generation reflection/revision, augmented by domain-dependent choices in expansion, reranking, augmentation, and prompt reordering; passage compression is never selected.

You can access the paper directly at https://arxiv.org/abs/2511.01386 and the code repository is available at https://github.com/yAquila/RAGSmith.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30c98888-02f2-44e3-8666-54ca94c2827b",
  "isSidechain": false,
  "promptId": "5d3abe21-235c-45be-ad4b-bb4a82a5a4e1",
  "type": "user",
  "uuid": "71cfbd45-ad73-46b5-aedf-bcc32698ea2e",
  "toolUseResult": {
    "query": "RAGSmith optimal composition RAG 2025 arXiv 2511.01386",
    "results": [
      {
        "tool_use_id": "srvtoolu_018HDkRNG9d4s9ohV3JJgvzL",
        "content": [
          {
            "title": "RAGSmith: RAG Pipeline with Genetic Algorithm Optimization",
            "url": "https://github.com/yAquila/RAGSmith"
          },
          {
            "title": "[2511.01386] RAGSmith: A Framework for Finding the Optimal Composition of Retrieval-Augmented Generation Methods Across Datasets",
            "url": "https://arxiv.org/abs/2511.01386"
          },
          {
            "title": "RAGSmith: A Framework for Finding the Optimal Composition of Retrieval-Augmented Generation Methods Across Datasets | Request PDF",
            "url": "https://www.researchgate.net/publication/397231360_RAGSmith_A_Framework_for_Finding_the_Optimal_Composition_of_Retrieval-Augmented_Generation_Methods_Across_Datasets"
          },
          {
            "title": "RAGSmith: A Framework for Finding the Optimal Composition of",
            "url": "https://arxiv.org/pdf/2511.01386"
          },
          {
            "title": "RAGSmith: A Framework for Finding the Optimal Composition of Retrieval-Augmented Generation Methods Across Datasets",
            "url": "https://arxiv.org/html/2511.01386v1"
          }
        ]
      },
      "Based on the search results, here's information about RAGSmith and arXiv paper 2511.01386:\n\nRAGSmith is a framework for finding the optimal composition of retrieval-augmented generation methods across datasets, authored by Muhammed Yusuf Kartal, Suha Kagan Kose, Korhan Sevinç, and Burak Aktas, published in November 2025.\n\n## Overview\n\nRAGSmith treats RAG design as an end-to-end architecture search over nine technique families and 46,080 feasible pipeline configurations. A genetic search optimizes a scalar objective that jointly aggregates retrieval metrics (recall@k, mAP, nDCG, MRR) and generation metrics (LLM-Judge and semantic similarity).\n\n## Key Findings\n\nThe framework was evaluated on six Wikipedia-derived domains (Mathematics, Law, Finance, Medicine, Defense Industry, Computer Science), and RAGSmith found configurations that consistently outperform naive RAG baseline by +3.8% on average (range +1.2% to +6.9% across domains), with gains up to +12.5% in retrieval and +7.5% in generation.\n\nThe search typically explores approximately 0.2% of the space (~100 candidates) and discovers a robust backbone of vector retrieval plus post-generation reflection/revision, augmented by domain-dependent choices in expansion, reranking, augmentation, and prompt reordering; passage compression is never selected.\n\nYou can access the paper directly at https://arxiv.org/abs/2511.01386 and the code repository is available at https://github.com/yAquila/RAGSmith."
    ],
    "durationSeconds": 7.494273661999963,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "30c98888-02f2-44e3-8666-54ca94c2827b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-30T07:16:04.140Z_

<details><summary>Logged reasoning block</summary>

```text
RAGSmith is about architecture search over RAG pipeline components, not specifically about the redundancy-distraction decomposition. It's tangentially related but not a direct threat to the novelty claim.

Now let me compile my analysis. Based on thorough research, I can confirm:

1. The gap claim (no method is simultaneously post-retrieval, formally grounded with approximation bounds, AND distraction-aware) is genuine.
2. No existing work has proposed the specific redundancy-distraction decomposition as a formal optimization objective.
3. The "approximately submodular minus modular" instantiation in RAG is indeed new.

However, there are several things I want to flag:


SMART-RAG addresses relevance, diversity, and conflict among passages, but its notion of conflict—contradictory information—differs from distraction as measured by answer-conditional interference, so the distinction holds. Context Bubble Construction balances relevance, coverage, and redundancy without incorporating a distraction term, leaving the proposed approach's focus on this dimension genuinely novel.

For the final output, I'm identifying three key contributions: γ as a diagnostic measure of context composition difficulty, the redundancy-distraction decomposition as a principled framework for understanding when context becomes harmful, and the independence assumption underlying the additive penalty structure. On that third point, I'm reconsidering whether independence is a limitation or a strength—if redundancy and distraction operate through fundamentally different mechanisms, with redundancy wasting tokens through duplication and distraction actively misleading through plausible irrelevant information, then treating them as independent failure modes becomes a feature rather than a constraint.

The proposal is solid overall with room for development, though I'm questioning whether formal guarantees alone sufficiently differentiate this from existing RL-based methods like DynamicRAG that already learn to avoid distraction implicitly through reward signals.

Looking at the core assumptions: the distraction measure DE_q(p) requires expensive LLM calls per pair, but the ACL 2025 work validates its robustness across models; the bounded-embedding conditions needed for the γ derivation will be verified empirically; and the additivity assumption across relevance, redundancy, and distraction is principled but would benefit from more explicit justification about why these failure modes decompose cleanly.

I'm confident in this analysis and ready to write up my findings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71cfbd45-ad73-46b5-aedf-bcc32698ea2e",
  "isSidechain": false,
  "requestId": "req_011CbYLnyK9yo6TYzH3byLwF",
  "type": "assistant",
  "uuid": "d9cdc18e-7c52-4aa4-b599-1953062d35f7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MumH8zoJdW4ChtneVK5ob2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 794,
      "cache_read_input_tokens": 34763,
      "output_tokens": 5175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 794,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5175,
          "cache_read_input_tokens": 34763,
          "cache_creation_input_tokens": 794,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 794
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

_source line 54 · 2026-05-30T07:17:36.220Z_

Now I have sufficient research context. Let me synthesize my findings and provide the analysis.

---

【状态】: 有发掘空间

【前置调研发现】
- [AdaGReS, arXiv:2512.25052](https://arxiv.org/abs/2512.25052) (Dec 2025): 提出 ε-approximate submodularity 用于 redundancy-penalized greedy context selection，但仅处理 monotone 情况。本 proposal 正确指出其不覆盖 distraction。其 adaptive β* calibration 是重要的技术细节——本 proposal 的 β 调节需要同样精细。
- [The Distracting Effect, ACL 2025](https://aclanthology.org/2025.acl-long.892/): 提出 per-passage DE_q(p) 连续度量，展示了 irrelevant passage 的 distraction 比 binary 分类更复杂。核心贡献在度量层面，无 set-level 优化。本 proposal 正确定位了其作为 modular penalty source 的角色。
- [AAMAS 2026 γ-weakly DR-submodular, arXiv:2601.00611](https://arxiv.org/abs/2601.00611) (Jan 2026): Jadav, Singh, Aggarwal。提供 non-monotone γ-weakly DR-submodular maximization 的 Φ_γ 保证。纯理论工作，无 NLP 实证。本 proposal 拟做首次 NLP instantiation。
- [CCBQP, arXiv:2604.02554](https://arxiv.org/abs/2604.02554) (Apr 2026): Frank-Wolfe + landscape analysis 做 relevance-diversity Pareto，dominate MMR/DPP。但明确处于 relevance-diversity paradigm，无 distraction term。这是本 proposal 最强的 formal-guarantee 竞争对手。
- [LDAR, ICLR 2026](https://arxiv.org/abs/2509.21865): Distraction-aware retriever，在 retrieval 阶段操作。无 post-retrieval composition 或 approximation bound。验证了 distraction-awareness 的经验重要性，但方法论不重叠。
- [DynamicRAG, NeurIPS 2025](https://arxiv.org/abs/2505.07233): RL + LLM feedback 做 dynamic reranking。跨 7 个 benchmark SOTA。但无 formal guarantees，distribution-dependent。
- [SMART-RAG, arXiv:2409.13992](https://arxiv.org/abs/2409.13992) (Sep 2024): DPP 联合建模 relevance/diversity/conflict。注意 "conflict" ≠ "distraction"：conflict 是 passage 间的矛盾信息，distraction 是 answer-conditional interference from irrelevant content。Proposal 已正确区分。
- [Qian, arXiv:1910.05492](https://arxiv.org/abs/1910.05492) (2019→Evolutionary Computation 2021): "Approximately submodular minus modular" 的 multi-objective EA 保证。理论框架存在，但无 NLP instantiation，且使用的是 evolutionary algorithm 而非 double-greedy。
- [Dynamic Context Selection, arXiv:2512.14313](https://arxiv.org/abs/2512.14313) (Dec 2025): 系统分析 distractor 对 RAG generation 的影响和 positional bias，但没有 formal optimization framework。
- 调研总结：当前该领域的研究者主要沿两条路线突破——(1) 用 formal optimization（submodular、DPP、BQP）保证 relevance-diversity trade-off 的理论性质；(2) 用 learned approach（RL、LLM-as-judge）隐式处理 distraction。本 proposal 试图弥合的 gap（formal + distraction-aware）确实存在，且未被近期工作覆盖。

---

【发掘点 1】
- 维度: novelty 锐化
- 内容: 当前 novelty claim 的主体是 "first instantiation of approximately-submodular-minus-modular in NLP/RAG"——这是一个**定位型 novelty**（"我们是第一个在领域 D 做 X 的"），容易被审稿人视为 incremental application。建议将 novelty 重心从"首次 instantiation"转移到 **γ 本身作为 context composition difficulty 的刻画量** 上。具体而言：γ 不仅是一个使算法运行的技术参数，它本身编码了一个有实际意义的结构性质——给定一组 candidate passages 和 query，γ 的大小刻画了"在此检索池上，简单贪心与 non-monotone 优化之间的性能差距有多大"。当 γ ≈ 1 时（candidate pool 语义多样、近似重复少），monotone greedy 足够好，formal non-monotone 优化的边际收益小；当 γ 显著小于 1 时（高冗余、高 distraction pool），non-monotone 优化变得必要。这将贡献从"应用了一个理论"升级为"**揭示了 RAG context composition 的一个结构性刻画**"。具体做法：在 empirically measured γ 的报告中，跨 benchmark 分析 γ 与 (a) candidate pool 的语义多样性、(b) 最终 accuracy gain over monotone greedy 的关系，验证 γ 是否确实是 composition difficulty 的可靠 predictor。
- 价值: 直接提升 Novelty 天花板。将 novelty 从 "application of known theory"（容易被视为 incremental）提升为 "structural insight about the problem domain"（更难被审稿人 dismiss）。同时为 significance 加分——γ 作为 diagnostic 工具本身对 practitioner 有实用价值（决定何时值得使用复杂算法）。
- 调研依据: CCBQP (arXiv:2604.02554) 通过 landscape analysis 揭示了 relevance-diversity Pareto 的结构性质，被认为是有价值的理论贡献。类似地，γ-as-diagnostic 也是揭示问题结构的贡献。AAMAS 2026 论文本身仅提供了抽象的 Φ_γ 保证，但没有讨论 γ 在特定领域中的语义——本 proposal 有机会填补这一空白。

【发掘点 2】
- 维度: 核心 claim 强化
- 内容: 当前 proposal 将 redundancy-distraction decomposition 作为一个建模选择来呈现（"我们定义 f(S) = rel − β·redundancy − λ·distraction"），但没有深入论证**为什么这两个 failure mode 应该被独立建模**。建议将 decomposition 本身升级为一个有因果论证的 first-class contribution。论证逻辑：redundancy 和 distraction 通过**不同的因果机制**损害 generation quality——redundancy 是一个**资源浪费问题**（重复信息占据 token budget，排挤其他有用 passage 的机会），其危害是间接的（opportunity cost）；distraction 是一个**主动干扰问题**（irrelevant-but-plausible content 直接误导 LLM 的 attention 和推理），其危害是直接的（interference cost）。这两种机制有不同的 scaling behavior：redundancy 的边际危害递减（第 n 个重复 passage 的边际信息损失越来越小），distraction 的边际危害可能递增（多个 distracting passages 可能产生 compounding interference）。正因为机制不同、scaling 不同，它们需要不同的 penalty 结构（pairwise sim vs. modular DE）和不同的超参数（β vs. λ）来独立控制。这个论证将 decomposition 从"一种建模方式"升级为"一种有原则的问题分析框架"。
- 价值: 强化 Novelty 和 Significance。如果 decomposition 仅是建模选择，审稿人会问 "why not a single penalty term that captures both?"；如果 decomposition 有因果论证支撑，它就成为一个 conceptual contribution，提升 idea 的理论深度。
- 调研依据: SMART-RAG 将 "conflict" 作为第三个维度加入 DPP kernel，但没有区分 conflict 和 distraction 的因果机制，也没有论证为什么它们应该被独立建模。LDAR 隐式处理 distraction 但不做 decomposition。当前领域没有任何工作从因果机制角度论证 redundancy vs. distraction 的独立性——这是一个空白。

【发掘点 3】
- 维度: significance 提升
- 内容: 当前的 broader motivation 部分提到了 "in-context learning, tool-use composition, multi-document grounding" 均展现 non-monotone returns to context size，但这只用了一段话作为背景铺垫，然后迅速聚焦到 RAG。建议**在 framing 层面将贡献定位为"non-monotone context composition 的通用分析框架的首个实例化"**，而不仅仅是"RAG 的一个新方法"。具体做法：(1) 在 introduction 中用 1-2 段明确指出 non-monotone context composition 是一个跨领域的共性问题，列出 3-4 个具体场景（RAG passage selection、ICL exemplar selection、tool-use context assembly、multi-agent communication），说明每个场景中 "adding more context hurts" 的具体表现；(2) 明确表述 "本文的 distraction-redundancy decomposition 框架是通用的，任何满足 relevance−redundancy−interference 结构的 context composition 问题都可以套用，RAG 是最清晰且最容易实证验证的 instantiation"；(3) 在 discussion 中简要展望如何将 DE_q(p) 推广到 tool-use 场景（如 "tool irrelevance score"）或 ICL 场景（如 "exemplar interference score"）。注意：不需要做额外实验，纯 framing 层面的提升。
- 价值: 直接提升 Significance。将 paper 从 "a RAG method paper" 升级为 "a framework paper with RAG as case study"。前者竞争对手众多（DynamicRAG、LDAR、Context-Picker 等），后者竞争对手极少。同时提高 AAAI 审稿人的兴趣——AAAI 重视 broad impact 和 cross-cutting contributions。
- 调研依据: Sub-CP (arXiv:2510.05130) 将 submodular optimization 用于 ICL exemplar partitioning，验证了 submodular 框架在 ICL 中的适用性。这为 "non-monotone context composition 是跨领域共性问题" 的论点提供了直接支撑。

【发掘点 4】
- 维度: related work 差异化
- 内容: 当前 proposal 的 related work 分析非常到位地覆盖了 formal-guarantee camp 和 distraction-aware camp，但遗漏了一类潜在的审稿人质疑：**CCBQP 的 diagonal loading 项 λ≥2 是否已经隐式处理了部分 distraction？** CCBQP 的 Frank-Wolfe formulation 中的 diagonal loading 增强了 relevance 的权重，可能在效果上减弱了低 relevance（即可能 distracting）passage 的选中概率。虽然这不等同于显式的 distraction modeling，但审稿人可能会问 "CCBQP 的 diagonal loading 已经足够好了，为什么还需要一个显式的 DE term？" 建议在 related work 中预防性地回应这一质疑：明确区分 "low relevance" ≠ "high distraction"。一个 passage 可以具有中等 relevance（与 query 有语义关联）但 high distraction（包含误导性信息导致 LLM 产生错误答案）。DE_q(p) 捕获的是后者，而 relevance score 无法区分这两种情况。引用 ACL 2025 Distracting Effect 论文的发现：高 DE 的 passage 并不总是 low relevance 的，它们可能是 topically related 但 answer-misleading 的——这正是 relevance-based filtering 无法处理的盲区。
- 价值: 提升 Related Work 差异化的鲁棒性。CCBQP 是本 proposal 在 formal-guarantee camp 中最强的竞争对手（Apr 2026，方法新且结果强），如果审稿人恰好熟悉 CCBQP 并提出上述质疑，缺乏预防性回应将显著降低 novelty 说服力。
- 调研依据: CCBQP (arXiv:2604.02554) 的 diagonal loading 分析（λ≥2 条件下的 landscape 性质）。ACL 2025 Distracting Effect 论文的核心发现——distraction 不是 irrelevance 的子集，而是一个正交维度。

Sources:
- [AdaGReS: Adaptive Greedy Context Selection](https://arxiv.org/abs/2512.25052)
- [The Distracting Effect: Understanding Irrelevant Passages in RAG (ACL 2025)](https://aclanthology.org/2025.acl-long.892/)
- [AAMAS 2026: γ-Weakly DR-Submodular Maximization](https://arxiv.org/abs/2601.00611)
- [CCBQP: Cardinality-Constrained Binary Quadratic Programming](https://arxiv.org/abs/2604.02554)
- [LDAR: Learning Distraction-Aware Retrieval (ICLR 2026)](https://arxiv.org/abs/2509.21865)
- [DynamicRAG (NeurIPS 2025)](https://arxiv.org/abs/2505.07233)
- [SMART-RAG: Selection using Determinantal Matrices](https://arxiv.org/abs/2409.13992)
- [Qian: Approximately Submodular Minus Modular](https://arxiv.org/abs/1910.05492)
- [Dynamic Context Selection for RAG](https://arxiv.org/abs/2512.14313)
- [Sub-CP: Submodular Context Partitioning for ICL](https://arxiv.org/abs/2510.05130)
- [Vendi-RAG: Diversity and Quality Trade-Off](https://arxiv.org/abs/2502.11228)
- [Jina: Submodular Optimization for Text Selection & Context Engineering](https://jina.ai/news/submodular-optimization-for-text-selection-passage-reranking-context-engineering/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9cdc18e-7c52-4aa4-b599-1953062d35f7",
  "isSidechain": false,
  "requestId": "req_011CbYLnyK9yo6TYzH3byLwF",
  "type": "assistant",
  "uuid": "a918da53-e749-474f-b789-36e2ba5b475d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MumH8zoJdW4ChtneVK5ob2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 794,
      "cache_read_input_tokens": 34763,
      "output_tokens": 5175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 794,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5175,
          "cache_read_input_tokens": 34763,
          "cache_creation_input_tokens": 794,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 794
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

_source line 55_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition  ## Core Problem  How can post-retrieval context composition for RAG be formalized as a constrained non-monotone…",
  "leafUuid": "a918da53-e749-474f-b789-36e2ba5b475d",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Non-monotone submodular context composition for RAG",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7"
}
```

---

### Runtime record

_source line 57_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition  ## Core Problem  How can post-retrieval context composition for RAG be formalized as a constrained non-monotone…",
  "leafUuid": "a918da53-e749-474f-b789-36e2ba5b475d",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7"
}
```

---

### Runtime record

_source line 58_

```json
{
  "type": "ai-title",
  "aiTitle": "Non-monotone submodular context composition for RAG",
  "sessionId": "f38fdf25-2bc6-4f3e-8501-0aa918175ef7"
}
```

---
