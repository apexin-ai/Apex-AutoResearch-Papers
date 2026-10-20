# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Conformal Abstention for RAG unde

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-2/aa5893a8-fa2a-43db-928c-9a8aa9b27f5b.jsonl`
- **Structured JSON:** [`07c9bd7a5d0094a9ea30.json`](../../sessions/07/07c9bd7a5d0094a9ea30.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T07:50:42.340Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T07:50:42.340Z",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Conformal Abstention for RAG under LP-Bounded Retrieval Shifts\n\n## Core Problem\n\nHow can a RAG system provide distribution-free, certified abstention guarantees on answer correctness when the retrieval corpus undergoes bounded distributional shifts — including adversarial corpus poisoning, organic corpus drift, and domain mismatch — where standard conformal prediction (TRAQ, C-RAG) breaks due to exchangeability violation, and existing certified defenses (RobustRAG, ReliabilityRAG) can only generate answers but cannot formally decide when to abstain?\n\n## Core Insight\n\nWe show that anchoring the nonconformity score at the retrieval-agreement level — rather than the answer-confidence level used by prior CP-for-RAG methods — is a necessary condition for LP-CP's score propagation theorem to yield non-vacuous guarantees in RAG.\n\n**Why retrieval-level anchoring is necessary, not merely convenient.** LP-CP's worst-case quantile shifts scale as L·ε, where L is the score function's Lipschitz constant and ε is the local perturbation bound. For answer-level scores (LLM output logits/probabilities), the composition of embedding lookup → attention layers → softmax produces Lipschitz constants that grow uncontrollably with context length and model depth, rendering LP-CP propagation vacuous (worst-case quantile collapses to trivial bounds). For retrieval-level pairwise cosine similarity on normalized embeddings, the Lipschitz constant is analytically bounded (O(2/k) for mean pairwise agreement over k passages w.r.t. single-document replacement), independent of LLM architecture. This analysis establishes that retrieval-level scoring is the natural — and effectively the only viable — anchor point for LP-CP in RAG systems.\n\nThis design simultaneously: (1) directly probes the attack surface (poisoning acts on retrieval, not generation), (2) makes the method LLM-agnostic and composable with any downstream generator, and (3) enables the first certified abstention guarantee for RAG under distributional shifts.\n\n## Research Opportunity\n\nThe intersection of {conformal prediction} ∩ {RAG} ∩ {adversarial robustness} is empty as of May 2026, verified across two RAG security surveys (arXiv:2603.21654, arXiv:2604.08304), the TACL CP-for-NLP survey, and 15+ targeted searches. Chen et al. (arXiv:2603.16817, Mar 2026) explicitly diagnosed that conformal factuality guarantees break under RAG distribution shift — including but not limited to adversarial shift — but proposed no solution. The LP-CP framework (NeurIPS 2025, arXiv:2502.14105) provides the exact (ρ, ε) decomposition that maps onto corpus poisoning parameters. No concurrent work addresses this gap.\n\n## Research Landscape\n\n**CP for benign RAG.** TRAQ (NAACL 2024) provides end-to-end coverage via calibrated retrieval and answer sets. C-RAG (ICML 2024) certifies conformal generation risk bounds. Conformal-RAG (SIGIR 2025) offers group-conditional coverage for sub-claims. Principled Context Engineering for RAG (arXiv:2511.17908) uses CP for context filtering, reducing retained context by 2–3×. PASC (arXiv:2605.18812) addresses pipeline-aware joint coverage for multi-stage NLP systems including RAG pipelines. None handle adversarial or shifted retrieval.\n\n**Certified RAG defenses (answer-only, no abstention).** RobustRAG (SaTML 2026) achieves 38% certified robust accuracy on RealtimeQA (71% clean) via isolate-then-aggregate. ReliabilityRAG (NeurIPS 2025) uses graph-theoretic MIS with reliability-weighted documents under k′ ≤ k/5 poisoning budget. Both must produce an answer even under high uncertainty; neither offers formal abstention.\n\n**Heuristic RAG defenses.** RAGDefender (ACSAC 2025) achieves 0.18 ASR at 10× poisoning ratio via cosine-similarity clustering, finding poisoned docs cluster tightly (0.976 vs 0.309 cosine similarity). TrustRAG (arXiv:2501.00879) uses K-means clustering + cosine similarity for plug-and-play detection. RAGPart & RAGMask (arXiv:2512.24268) use document partitioning and token masking at retrieval stage across four retrievers. These rely on heuristic thresholds with no coverage guarantees or formal abstention.\n\n**Relationship to RAGDefender's signal.** LP-RAG-Abstain uses the same underlying signal as RAGDefender — pairwise cosine similarity among retrieved passages. The contribution operates at a different level: (1) signal level: shared (pairwise cosine similarity) — we openly acknowledge this; (2) decision rule level: RAGDefender uses tuned thresholds on cluster membership, LP-RAG-Abstain uses LP-CP worst-case quantiles — methodological difference; (3) guarantee level: RAGDefender provides no finite-sample guarantee and its threshold has no parametric response to attack budget, LP-RAG-Abstain provides distribution-free coverage guarantee parameterized by (ρ, ε) — fundamental difference. The core question this paper answers: what theoretical framework converts the empirical observation that pairwise similarity distinguishes poisoned retrieval into a formal guarantee?\n\n**Poisoning-robust CP (non-RAG).** RPS (ICLR 2025 Spotlight) uses partition-and-vote for calibration-time data poisoning — a fundamentally different poisoning model than test-time retrieval corruption. In calibration poisoning, the attacker corrupts the static calibration set; in RAG poisoning, corruption occurs dynamically at test-time through retrieval. RPS's guarantees do not transfer to the RAG setting. LP-CP (NeurIPS 2025, arXiv:2502.14105) provides closed-form worst-case quantiles under LP distribution shifts but was not applied to RAG.\n\n**Conformal abstention (non-adversarial).** Learning Conformal Abstention Policies (arXiv:2502.06884) integrates RL with CP for adaptive abstention in LLMs/VLMs but relies on training and does not handle adversarial settings. Selective Conformal Risk Control (arXiv:2512.12844) integrates CP with selective classification but not in RAG or adversarial contexts.\n\n**Robust CP for LLMs.** Beyond Surface Statistics (arXiv:2604.16217) uses LLM internal representations for robust CP but does not analyze Lipschitz properties or address adversarial RAG. Efficient Robust CP via Lipschitz-Bounded Networks (arXiv:2506.05434) controls model Lipschitz constants to tighten robust CP sets — complementary to our approach of controlling the score function's Lipschitz constant.\n\n**Attack landscape.** PoisonedRAG (USENIX Security 2025) achieves 97% ASR via multi-document injection with distinct black-box (LLM-generated) and white-box (gradient-optimized) variants. CorruptRAG (arXiv:2504.03957) achieves high ASR with single-document injection (ρ→0). Benchmarking Poisoning Attacks against RAG (arXiv:2505.18543) provides a unified framework across 5 datasets, 13 attacks, and 7 defenses.\n\n## Proposed Approach\n\n**LP-RAG-Abstain** provides distribution-free certified abstention for RAG under LP-bounded retrieval shifts, with adversarial corpus poisoning as the primary and most challenging instantiation.\n\n**Threat model.** Attacker injects poisoned documents into the corpus. Defense assumes upper bounds (ρ₀, ε₀) on: ρ = fraction of poisoned documents in top-k retrieval, ε = maximum embedding perturbation per poisoned document. These are defense input parameters (analogous to RobustRAG's k′ ≤ k/5), not quantities to estimate. Guarantees are conditional: valid whenever the actual attack falls within (ρ₀, ε₀). The same (ρ, ε) parameterization naturally covers non-adversarial retrieval shifts (organic corpus drift, domain mismatch), making the framework broadly applicable.\n\n**Score design.** Define retrieval-agreement nonconformity score s(q) from pairwise cosine similarities among top-k retrieved passages for query q. For normalized embeddings on the unit sphere, the mean pairwise cosine similarity score has Lipschitz constant O(2/k) w.r.t. single-document replacement, enabling LP-CP's propagation theorem to yield closed-form worst-case quantiles that are non-vacuous for practical (ρ, ε) ranges.\n\n**Lipschitz tightness.** The practical viability depends on the Lipschitz constant being small enough. We will: (1) derive the analytic Lipschitz upper bound, (2) empirically estimate the constant on real embedding data, (3) report the gap between certified and empirical coverage to quantify conservatism, and (4) if needed, explore Lipschitz-regularized score designs (cf. arXiv:2506.05434).\n\n**Abstention rule.** Map (ρ₀, ε₀) to LP ambiguity set. Compute worst-case conformal quantile via LP-CP's closed-form expression. Abstain when prediction set is empty under worst-case quantile. Guarantee: P(correct ∈ set ∨ abstain) ≥ 1−α.\n\n**Adversary-budget monotonicity.** Certified coverage improves as attacker budget (ρ, ε) decreases, with the tightest guarantees at the most practical attack regime — single/few-document poisoning (CorruptRAG, arXiv:2504.03957). This contrasts with isolate-then-aggregate methods (RobustRAG) whose partitioning overhead is constant regardless of attack strength.\n\n**\"Safe Silence\" guarantee.** Unlike answer-only defenses that must produce output under high uncertainty, LP-RAG-Abstain formally guarantees: \"either I return a set containing the correct answer, or I explicitly abstain.\" In safety-critical RAG (medical, legal, financial), confidently wrong answers are far more harmful than acknowledged uncertainty. This addresses the \"robustness + usefulness\" desiderata of Chen et al. (arXiv:2603.16817).\n\n**Compositional extension.** LP-RAG-Abstain as a retrieval-stage gatekeeper can compose with downstream answer-level CP methods (TRAQ, C-RAG): if LP-RAG-Abstain does not abstain, retrieval is certified within LP tolerance, approximately restoring exchangeability so downstream CP guarantees re-activate. Via pipeline-aware CP techniques (PASC, arXiv:2605.18812), this enables end-to-end joint coverage guarantees — a direction we discuss as future work.\n\n## Experimental Design\n\n**Datasets.** NQ, HotpotQA, MS-MARCO.\n\n**Attacks.** PoisonedRAG black-box + white-box (USENIX Security 2025), CorruptRAG single-document (arXiv:2504.03957). White-box variant directly optimizes embeddings, providing the strongest test of ε-bounded guarantees.\n\n**Embedding models.** Qwen3-Embedding-8B (primary), BGE-large, Contriever. Report empirical Lipschitz constant for each.\n\n**Generator LLMs.** Llama-3.1-8B (open-source), GPT-4o (closed-source).\n\n**Baselines.**\n- No-defense vanilla RAG\n- TRAQ (NAACL 2024): CP without adversarial awareness\n- C-RAG (ICML 2024): conformal risk bounds without adversarial awareness\n- RobustRAG (SaTML 2026): certified answer-only defense\n- ReliabilityRAG (NeurIPS 2025): certified answer-only defense\n- RAGDefender (ACSAC 2025): heuristic detection (same signal, no guarantee)\n- TrustRAG (arXiv:2501.00879): heuristic detection\n- Naive selective prediction: LLM confidence threshold abstention\n\n**Evaluation metrics.**\n- Coverage (poisoned): P(correct ∈ set ∨ abstain) — core guarantee\n- Coverage (clean): P(correct ∈ set) without poisoning — should ≥ 1−α\n- Abstention rate (poisoned vs. clean)\n- Certified robust accuracy on non-abstained queries (EM and F1)\n- Overall ASR (abstain counted as attack failure) and conditional ASR (non-abstained only)\n- Prediction set size (mean/median)\n- Accuracy-abstention tradeoff AUC (varying α)\n- Wall-clock inference time and LLM call count per query\n\n**Ablation studies.**\n1. ρ sensitivity: fix ε, vary ρ ∈ {0, 0.05, 0.1, 0.2, 0.4}\n2. ε sensitivity: fix ρ, vary ε\n3. Score function: pairwise cosine agreement (proposed) vs. average retrieval score vs. answer entropy\n4. k sensitivity: k ∈ {5, 10, 20, 50}\n5. α sweep: α ∈ {0.01, 0.05, 0.10, 0.20}\n6. Calibration set size: {100, 300, 500, 1000, 2000}\n7. LP-CP vs. Bonferroni correction\n\n**(ρ, ε) heatmap.** Jointly vary (ρ, ε) and plot certified accuracy and abstention rate as 2D heatmaps.\n\n**Adaptive attack evaluation.** Adversary with full knowledge of the defense. Two PGD-based attack strategies within ε-ball: (a) maximize pairwise cosine agreement score (poisoned docs mimic clean retrieval pattern), (b) minimize it (force vacuous prediction sets). Report whichever is worse for the defense. Constraints: ‖e_poison − e_original‖₂ ≤ ε, ρk poisoned docs in top-k. Reference design: OPSA (arXiv:2506.07804) for CP-targeted attack methodology.\n\n**Cross-attack validation.** On NQ: calibrate (ρ₀, ε₀) under PoisonedRAG assumptions, test under CorruptRAG, and vice versa. Verify coverage guarantee holds across attack types (theoretically guaranteed by (ρ, ε) parameterization; experimentally validated).\n\n**Experiment organization.** Layered strategy: (1) Core: primary embedding model + Llama-3.1-8B + all datasets + all attacks + all baselines; (2) Generalization: NQ with all embedding model × LLM combinations; (3) Ablation: main configuration only; (4) GPT-4o limited to core and generalization experiments.\n\n**Targets.** Exceed RobustRAG's 38% certified robust accuracy on comparable datasets; maintain >90% clean coverage; achieve <15% clean abstention rate; overall ASR < 10% under standard PoisonedRAG attack.\n\n## Key References\n\n- TRAQ (NAACL 2024)\n- C-RAG: Certified Generation Risks for RAG (ICML 2024)\n- Conformal-RAG / Response Quality Assessment (SIGIR 2025)\n- RobustRAG: Certifiably Robust RAG against Retrieval Corruption (SaTML 2026)\n- ReliabilityRAG (NeurIPS 2025)\n- PoisonedRAG (USENIX Security 2025)\n- CorruptRAG: Practical Poisoning Attacks against RAG (arXiv:2504.03957)\n- LP-CP: Conformal Prediction under Lévy-Prokhorov Distribution Shifts (NeurIPS 2025, arXiv:2502.14105)\n- RPS: Provably Reliable CP Sets under Data Poisoning (ICLR 2025 Spotlight)\n- RAGDefender: Rescuing the Unpoisoned (ACSAC 2025)\n- TrustRAG (arXiv:2501.00879)\n- RAGPart & RAGMask (arXiv:2512.24268)\n- Chen et al.: Is Conformal Factuality for RAG-based LLMs Robust? (arXiv:2603.16817, 2026)\n- RAG security surveys (arXiv:2603.21654, arXiv:2604.08304)\n- TACL CP-for-NLP survey\n- Principled Context Engineering for RAG (arXiv:2511.17908)\n- Learning Conformal Abstention Policies (arXiv:2502.06884)\n- Selective Conformal Risk Control (arXiv:2512.12844)\n- Benchmarking Poisoning Attacks against RAG (arXiv:2505.18543)\n- PASC: Pipeline-Aware Conformal Prediction (arXiv:2605.18812)\n- OPSA: Enhancing Adversarial Robustness with CP (arXiv:2506.07804)\n- Efficient Robust CP via Lipschitz-Bounded Networks (arXiv:2506.05434)\n- Beyond Surface Statistics: Robust CP for LLMs (arXiv:2604.16217)"
}
```

---

### Runtime record

_source line 2 · 2026-05-30T07:50:42.348Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T07:50:42.348Z",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b"
}
```

---

## Round 1

41 recorded events

### User

_source line 3 · 2026-05-30T07:50:42.371Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Conformal Abstention for RAG under LP-Bounded Retrieval Shifts

## Core Problem

How can a RAG system provide distribution-free, certified abstention guarantees on answer correctness when the retrieval corpus undergoes bounded distributional shifts — including adversarial corpus poisoning, organic corpus drift, and domain mismatch — where standard conformal prediction (TRAQ, C-RAG) breaks due to exchangeability violation, and existing certified defenses (RobustRAG, ReliabilityRAG) can only generate answers but cannot formally decide when to abstain?

## Core Insight

We show that anchoring the nonconformity score at the retrieval-agreement level — rather than the answer-confidence level used by prior CP-for-RAG methods — is a necessary condition for LP-CP's score propagation theorem to yield non-vacuous guarantees in RAG.

**Why retrieval-level anchoring is necessary, not merely convenient.** LP-CP's worst-case quantile shifts scale as L·ε, where L is the score function's Lipschitz constant and ε is the local perturbation bound. For answer-level scores (LLM output logits/probabilities), the composition of embedding lookup → attention layers → softmax produces Lipschitz constants that grow uncontrollably with context length and model depth, rendering LP-CP propagation vacuous (worst-case quantile collapses to trivial bounds). For retrieval-level pairwise cosine similarity on normalized embeddings, the Lipschitz constant is analytically bounded (O(2/k) for mean pairwise agreement over k passages w.r.t. single-document replacement), independent of LLM architecture. This analysis establishes that retrieval-level scoring is the natural — and effectively the only viable — anchor point for LP-CP in RAG systems.

This design simultaneously: (1) directly probes the attack surface (poisoning acts on retrieval, not generation), (2) makes the method LLM-agnostic and composable with any downstream generator, and (3) enables the first certified abstention guarantee for RAG under distributional shifts.

## Research Opportunity

The intersection of {conformal prediction} ∩ {RAG} ∩ {adversarial robustness} is empty as of May 2026, verified across two RAG security surveys (arXiv:2603.21654, arXiv:2604.08304), the TACL CP-for-NLP survey, and 15+ targeted searches. Chen et al. (arXiv:2603.16817, Mar 2026) explicitly diagnosed that conformal factuality guarantees break under RAG distribution shift — including but not limited to adversarial shift — but proposed no solution. The LP-CP framework (NeurIPS 2025, arXiv:2502.14105) provides the exact (ρ, ε) decomposition that maps onto corpus poisoning parameters. No concurrent work addresses this gap.

## Research Landscape

**CP for benign RAG.** TRAQ (NAACL 2024) provides end-to-end coverage via calibrated retrieval and answer sets. C-RAG (ICML 2024) certifies conformal generation risk bounds. Conformal-RAG (SIGIR 2025) offers group-conditional coverage for sub-claims. Principled Context Engineering for RAG (arXiv:2511.17908) uses CP for context filtering, reducing retained context by 2–3×. PASC (arXiv:2605.18812) addresses pipeline-aware joint coverage for multi-stage NLP systems including RAG pipelines. None handle adversarial or shifted retrieval.

**Certified RAG defenses (answer-only, no abstention).** RobustRAG (SaTML 2026) achieves 38% certified robust accuracy on RealtimeQA (71% clean) via isolate-then-aggregate. ReliabilityRAG (NeurIPS 2025) uses graph-theoretic MIS with reliability-weighted documents under k′ ≤ k/5 poisoning budget. Both must produce an answer even under high uncertainty; neither offers formal abstention.

**Heuristic RAG defenses.** RAGDefender (ACSAC 2025) achieves 0.18 ASR at 10× poisoning ratio via cosine-similarity clustering, finding poisoned docs cluster tightly (0.976 vs 0.309 cosine similarity). TrustRAG (arXiv:2501.00879) uses K-means clustering + cosine similarity for plug-and-play detection. RAGPart & RAGMask (arXiv:2512.24268) use document partitioning and token masking at retrieval stage across four retrievers. These rely on heuristic thresholds with no coverage guarantees or formal abstention.

**Relationship to RAGDefender's signal.** LP-RAG-Abstain uses the same underlying signal as RAGDefender — pairwise cosine similarity among retrieved passages. The contribution operates at a different level: (1) signal level: shared (pairwise cosine similarity) — we openly acknowledge this; (2) decision rule level: RAGDefender uses tuned thresholds on cluster membership, LP-RAG-Abstain uses LP-CP worst-case quantiles — methodological difference; (3) guarantee level: RAGDefender provides no finite-sample guarantee and its threshold has no parametric response to attack budget, LP-RAG-Abstain provides distribution-free coverage guarantee parameterized by (ρ, ε) — fundamental difference. The core question this paper answers: what theoretical framework converts the empirical observation that pairwise similarity distinguishes poisoned retrieval into a formal guarantee?

**Poisoning-robust CP (non-RAG).** RPS (ICLR 2025 Spotlight) uses partition-and-vote for calibration-time data poisoning — a fundamentally different poisoning model than test-time retrieval corruption. In calibration poisoning, the attacker corrupts the static calibration set; in RAG poisoning, corruption occurs dynamically at test-time through retrieval. RPS's guarantees do not transfer to the RAG setting. LP-CP (NeurIPS 2025, arXiv:2502.14105) provides closed-form worst-case quantiles under LP distribution shifts but was not applied to RAG.

**Conformal abstention (non-adversarial).** Learning Conformal Abstention Policies (arXiv:2502.06884) integrates RL with CP for adaptive abstention in LLMs/VLMs but relies on training and does not handle adversarial settings. Selective Conformal Risk Control (arXiv:2512.12844) integrates CP with selective classification but not in RAG or adversarial contexts.

**Robust CP for LLMs.** Beyond Surface Statistics (arXiv:2604.16217) uses LLM internal representations for robust CP but does not analyze Lipschitz properties or address adversarial RAG. Efficient Robust CP via Lipschitz-Bounded Networks (arXiv:2506.05434) controls model Lipschitz constants to tighten robust CP sets — complementary to our approach of controlling the score function's Lipschitz constant.

**Attack landscape.** PoisonedRAG (USENIX Security 2025) achieves 97% ASR via multi-document injection with distinct black-box (LLM-generated) and white-box (gradient-optimized) variants. CorruptRAG (arXiv:2504.03957) achieves high ASR with single-document injection (ρ→0). Benchmarking Poisoning Attacks against RAG (arXiv:2505.18543) provides a unified framework across 5 datasets, 13 attacks, and 7 defenses.

## Proposed Approach

**LP-RAG-Abstain** provides distribution-free certified abstention for RAG under LP-bounded retrieval shifts, with adversarial corpus poisoning as the primary and most challenging instantiation.

**Threat model.** Attacker injects poisoned documents into the corpus. Defense assumes upper bounds (ρ₀, ε₀) on: ρ = fraction of poisoned documents in top-k retrieval, ε = maximum embedding perturbation per poisoned document. These are defense input parameters (analogous to RobustRAG's k′ ≤ k/5), not quantities to estimate. Guarantees are conditional: valid whenever the actual attack falls within (ρ₀, ε₀). The same (ρ, ε) parameterization naturally covers non-adversarial retrieval shifts (organic corpus drift, domain mismatch), making the framework broadly applicable.

**Score design.** Define retrieval-agreement nonconformity score s(q) from pairwise cosine similarities among top-k retrieved passages for query q. For normalized embeddings on the unit sphere, the mean pairwise cosine similarity score has Lipschitz constant O(2/k) w.r.t. single-document replacement, enabling LP-CP's propagation theorem to yield closed-form worst-case quantiles that are non-vacuous for practical (ρ, ε) ranges.

**Lipschitz tightness.** The practical viability depends on the Lipschitz constant being small enough. We will: (1) derive the analytic Lipschitz upper bound, (2) empirically estimate the constant on real embedding data, (3) report the gap between certified and empirical coverage to quantify conservatism, and (4) if needed, explore Lipschitz-regularized score designs (cf. arXiv:2506.05434).

**Abstention rule.** Map (ρ₀, ε₀) to LP ambiguity set. Compute worst-case conformal quantile via LP-CP's closed-form expression. Abstain when prediction set is empty under worst-case quantile. Guarantee: P(correct ∈ set ∨ abstain) ≥ 1−α.

**Adversary-budget monotonicity.** Certified coverage improves as attacker budget (ρ, ε) decreases, with the tightest guarantees at the most practical attack regime — single/few-document poisoning (CorruptRAG, arXiv:2504.03957). This contrasts with isolate-then-aggregate methods (RobustRAG) whose partitioning overhead is constant regardless of attack strength.

**"Safe Silence" guarantee.** Unlike answer-only defenses that must produce output under high uncertainty, LP-RAG-Abstain formally guarantees: "either I return a set containing the correct answer, or I explicitly abstain." In safety-critical RAG (medical, legal, financial), confidently wrong answers are far more harmful than acknowledged uncertainty. This addresses the "robustness + usefulness" desiderata of Chen et al. (arXiv:2603.16817).

**Compositional extension.** LP-RAG-Abstain as a retrieval-stage gatekeeper can compose with downstream answer-level CP methods (TRAQ, C-RAG): if LP-RAG-Abstain does not abstain, retrieval is certified within LP tolerance, approximately restoring exchangeability so downstream CP guarantees re-activate. Via pipeline-aware CP techniques (PASC, arXiv:2605.18812), this enables end-to-end joint coverage guarantees — a direction we discuss as future work.

## Experimental Design

**Datasets.** NQ, HotpotQA, MS-MARCO.

**Attacks.** PoisonedRAG black-box + white-box (USENIX Security 2025), CorruptRAG single-document (arXiv:2504.03957). White-box variant directly optimizes embeddings, providing the strongest test of ε-bounded guarantees.

**Embedding models.** Qwen3-Embedding-8B (primary), BGE-large, Contriever. Report empirical Lipschitz constant for each.

**Generator LLMs.** Llama-3.1-8B (open-source), GPT-4o (closed-source).

**Baselines.**
- No-defense vanilla RAG
- TRAQ (NAACL 2024): CP without adversarial awareness
- C-RAG (ICML 2024): conformal risk bounds without adversarial awareness
- RobustRAG (SaTML 2026): certified answer-only defense
- ReliabilityRAG (NeurIPS 2025): certified answer-only defense
- RAGDefender (ACSAC 2025): heuristic detection (same signal, no guarantee)
- TrustRAG (arXiv:2501.00879): heuristic detection
- Naive selective prediction: LLM confidence threshold abstention

**Evaluation metrics.**
- Coverage (poisoned): P(correct ∈ set ∨ abstain) — core guarantee
- Coverage (clean): P(correct ∈ set) without poisoning — should ≥ 1−α
- Abstention rate (poisoned vs. clean)
- Certified robust accuracy on non-abstained queries (EM and F1)
- Overall ASR (abstain counted as attack failure) and conditional ASR (non-abstained only)
- Prediction set size (mean/median)
- Accuracy-abstention tradeoff AUC (varying α)
- Wall-clock inference time and LLM call count per query

**Ablation studies.**
1. ρ sensitivity: fix ε, vary ρ ∈ {0, 0.05, 0.1, 0.2, 0.4}
2. ε sensitivity: fix ρ, vary ε
3. Score function: pairwise cosine agreement (proposed) vs. average retrieval score vs. answer entropy
4. k sensitivity: k ∈ {5, 10, 20, 50}
5. α sweep: α ∈ {0.01, 0.05, 0.10, 0.20}
6. Calibration set size: {100, 300, 500, 1000, 2000}
7. LP-CP vs. Bonferroni correction

**(ρ, ε) heatmap.** Jointly vary (ρ, ε) and plot certified accuracy and abstention rate as 2D heatmaps.

**Adaptive attack evaluation.** Adversary with full knowledge of the defense. Two PGD-based attack strategies within ε-ball: (a) maximize pairwise cosine agreement score (poisoned docs mimic clean retrieval pattern), (b) minimize it (force vacuous prediction sets). Report whichever is worse for the defense. Constraints: ‖e_poison − e_original‖₂ ≤ ε, ρk poisoned docs in top-k. Reference design: OPSA (arXiv:2506.07804) for CP-targeted attack methodology.

**Cross-attack validation.** On NQ: calibrate (ρ₀, ε₀) under PoisonedRAG assumptions, test under CorruptRAG, and vice versa. Verify coverage guarantee holds across attack types (theoretically guaranteed by (ρ, ε) parameterization; experimentally validated).

**Experiment organization.** Layered strategy: (1) Core: primary embedding model + Llama-3.1-8B + all datasets + all attacks + all baselines; (2) Generalization: NQ with all embedding model × LLM combinations; (3) Ablation: main configuration only; (4) GPT-4o limited to core and generalization experiments.

**Targets.** Exceed RobustRAG's 38% certified robust accuracy on comparable datasets; maintain >90% clean coverage; achieve <15% clean abstention rate; overall ASR < 10% under standard PoisonedRAG attack.

## Key References

- TRAQ (NAACL 2024)
- C-RAG: Certified Generation Risks for RAG (ICML 2024)
- Conformal-RAG / Response Quality Assessment (SIGIR 2025)
- RobustRAG: Certifiably Robust RAG against Retrieval Corruption (SaTML 2026)
- ReliabilityRAG (NeurIPS 2025)
- PoisonedRAG (USENIX Security 2025)
- CorruptRAG: Practical Poisoning Attacks against RAG (arXiv:2504.03957)
- LP-CP: Conformal Prediction under Lévy-Prokhorov Distribution Shifts (NeurIPS 2025, arXiv:2502.14105)
- RPS: Provably Reliable CP Sets under Data Poisoning (ICLR 2025 Spotlight)
- RAGDefender: Rescuing the Unpoisoned (ACSAC 2025)
- TrustRAG (arXiv:2501.00879)
- RAGPart & RAGMask (arXiv:2512.24268)
- Chen et al.: Is Conformal Factuality for RAG-based LLMs Robust? (arXiv:2603.16817, 2026)
- RAG security surveys (arXiv:2603.21654, arXiv:2604.08304)
- TACL CP-for-NLP survey
- Principled Context Engineering for RAG (arXiv:2511.17908)
- Learning Conformal Abstention Policies (arXiv:2502.06884)
- Selective Conformal Risk Control (arXiv:2512.12844)
- Benchmarking Poisoning Attacks against RAG (arXiv:2505.18543)
- PASC: Pipeline-Aware Conformal Prediction (arXiv:2605.18812)
- OPSA: Enhancing Adversarial Robustness with CP (arXiv:2506.07804)
- Efficient Robust CP via Lipschitz-Bounded Networks (arXiv:2506.05434)
- Beyond Surface Statistics: Robust CP for LLMs (arXiv:2604.16217)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "bf7c039c-9c46-4596-82cc-fdd9084f898b",
  "type": "user",
  "uuid": "d31fac94-1f18-4c1f-9b33-a95bafc0ba44",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T07:50:42.369Z_

```json
{
  "parentUuid": "d31fac94-1f18-4c1f-9b33-a95bafc0ba44",
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
  "uuid": "45441e37-aa48-49af-9c6b-24f683607fe1",
  "timestamp": "2026-05-30T07:50:42.369Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T07:50:42.370Z_

```json
{
  "parentUuid": "45441e37-aa48-49af-9c6b-24f683607fe1",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5ef039b8-20b7-4ea8-af2c-cff2ddd6ee00",
  "timestamp": "2026-05-30T07:50:42.370Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Conformal Abstention for RAG under LP-Bounded Retrieval Shifts  ## Core Problem  How can a RAG system provide di…",
  "leafUuid": "5ef039b8-20b7-4ea8-af2c-cff2ddd6ee00",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Certified RAG abstention under retrieval poisoning",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b"
}
```

---

### Assistant

_source line 8 · 2026-05-30T07:50:48.884Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for AAAI 2026. Before I can give a proper assessment, I need to do thorough literature research on the topic. Let me first load the WebSearch tool, then conduct several searches to understand the current landscape.

The proposal is about "Conformal Abstention for RAG under LP-Bounded Retrieval Shifts" - combining conformal prediction, RAG systems, and adversarial robustness.

Let me start by loading WebSearch and conducting research.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ef039b8-20b7-4ea8-af2c-cff2ddd6ee00",
  "isSidechain": false,
  "requestId": "req_011CbYPUTf3ZCx3hsqdhmpV4",
  "type": "assistant",
  "uuid": "5c7d4ce1-495f-49c3-a1d6-3e06f979c566",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CRt6wbmASoimuyPqc245bg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8219,
      "cache_read_input_tokens": 11014,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8219,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 8219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8219
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

_source line 9 · 2026-05-30T07:50:49.113Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018p6RG3G2u3L7fvA9N4p2Fa`</summary>

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
  "parentUuid": "5c7d4ce1-495f-49c3-a1d6-3e06f979c566",
  "isSidechain": false,
  "requestId": "req_011CbYPUTf3ZCx3hsqdhmpV4",
  "type": "assistant",
  "uuid": "57427447-8873-4c32-9936-0db9870ef2dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CRt6wbmASoimuyPqc245bg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8219,
      "cache_read_input_tokens": 11014,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8219,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 204,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 8219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8219
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

_source line 10 · 2026-05-30T07:50:49.122Z_

<details><summary>↩ Tool result · `toolu_018p6RG3G2u3L7fvA9N4p2Fa`</summary>

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
  "parentUuid": "57427447-8873-4c32-9936-0db9870ef2dd",
  "isSidechain": false,
  "promptId": "bf7c039c-9c46-4596-82cc-fdd9084f898b",
  "type": "user",
  "uuid": "a6888e77-fd87-4f63-938c-a8bdab7e1fe1",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "57427447-8873-4c32-9936-0db9870ef2dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-30T07:50:54.481Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me conduct several targeted searches to understand the current landscape before evaluating this proposal. I'll search for:

1. LP-CP (Conformal Prediction under Lévy-Prokhorov shifts) and its applications
2. Conformal prediction for RAG systems (TRAQ, C-RAG, etc.)
3. Certified defenses for RAG poisoning (RobustRAG, ReliabilityRAG)
4. Recent work on conformal prediction + adversarial robustness
5. RAG poisoning attacks and defenses landscape


6. Running these searches now...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6888e77-fd87-4f63-938c-a8bdab7e1fe1",
  "isSidechain": false,
  "requestId": "req_011CbYPUxb6QfeNix3DoDW8D",
  "type": "assistant",
  "uuid": "228fb148-c6b7-4969-b820-8095f2f292b3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D7yvPX1FWWhAWqeAJ8pKKa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 19233,
      "output_tokens": 357,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 732,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 357,
          "cache_read_input_tokens": 19233,
          "cache_creation_input_tokens": 732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 732
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

_source line 12 · 2026-05-30T07:50:55.529Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013fk8YbgYFG7B7Ez17qrNns`</summary>

```json
{
  "query": "LP-CP conformal prediction Lévy-Prokhorov distribution shift NeurIPS 2025 arXiv:2502.14105"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "228fb148-c6b7-4969-b820-8095f2f292b3",
  "isSidechain": false,
  "requestId": "req_011CbYPUxb6QfeNix3DoDW8D",
  "type": "assistant",
  "uuid": "a19b2cbc-a2fe-440d-9b7e-d9d1780eb51a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D7yvPX1FWWhAWqeAJ8pKKa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 19233,
      "output_tokens": 357,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 732,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 357,
          "cache_read_input_tokens": 19233,
          "cache_creation_input_tokens": 732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 732
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

_source line 13 · 2026-05-30T07:50:56.067Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0195NEjuuVbvChN49qPsJ8kG`</summary>

```json
{
  "query": "conformal prediction RAG retrieval augmented generation TRAQ C-RAG 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a19b2cbc-a2fe-440d-9b7e-d9d1780eb51a",
  "isSidechain": false,
  "requestId": "req_011CbYPUxb6QfeNix3DoDW8D",
  "type": "assistant",
  "uuid": "fc2328ad-e34e-4ab1-ad86-9e54d7c4ed33",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D7yvPX1FWWhAWqeAJ8pKKa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 19233,
      "output_tokens": 357,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 732,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 357,
          "cache_read_input_tokens": 19233,
          "cache_creation_input_tokens": 732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 732
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

_source line 14 · 2026-05-30T07:50:56.565Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011QFz8cxMeXbZsYNdpPihyz`</summary>

```json
{
  "query": "RobustRAG certified defense RAG poisoning SaTML 2026 ReliabilityRAG NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc2328ad-e34e-4ab1-ad86-9e54d7c4ed33",
  "isSidechain": false,
  "requestId": "req_011CbYPUxb6QfeNix3DoDW8D",
  "type": "assistant",
  "uuid": "b5adaf37-c2d6-4a51-be1a-2333a782e0a0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D7yvPX1FWWhAWqeAJ8pKKa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 19233,
      "output_tokens": 357,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 732,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 357,
          "cache_read_input_tokens": 19233,
          "cache_creation_input_tokens": 732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 732
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

_source line 15 · 2026-05-30T07:51:00.667Z_

<details><summary>↩ Tool result · `toolu_013fk8YbgYFG7B7Ez17qrNns`</summary>

```text
Web search results for query: "LP-CP conformal prediction Lévy-Prokhorov distribution shift NeurIPS 2025 arXiv:2502.14105"

Links: [{"title":"[2502.14105] Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/abs/2502.14105"},{"title":"Conformal Prediction under Lévy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations | OpenReview","url":"https://openreview.net/forum?id=1ULQvdbZ3X"},{"title":"(PDF) Conformal Prediction under L\\'evy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://www.researchgate.net/publication/389176501_Conformal_Prediction_under_L'evy-Prokhorov_Distribution_Shifts_Robustness_to_Local_and_Global_Perturbations"},{"title":"NeurIPS Poster Conformal Prediction under Lévy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/120230"},{"title":"Conformal Prediction under Lévy-Prokhorov Distribution ...","url":"https://arxiv.org/pdf/2502.14105"},{"title":"Coverage Guarantees for Pseudo-Calibrated Conformal Prediction under Distribution Shift","url":"https://arxiv.org/html/2602.14913v1"},{"title":"Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/html/2502.14105v2"}]

I found the paper you're looking for. Here's what the search revealed:

The paper addresses conformal prediction's robustness under distribution shifts by modeling distribution shifts using Lévy-Prokhorov (LP) ambiguity sets, which capture both local and global perturbations.

The authors provide an overview of LP ambiguity sets and their connections to popular metrics such as Wasserstein and Total Variation. The key contribution is showing that by propagating the LP ambiguity set through the scoring function, complex high-dimensional distribution shifts can be reduced to manageable one-dimensional distribution shifts, enabling exact quantification of worst-case quantiles and coverage.

The paper was presented as a NeurIPS 2025 poster. The arxiv paper (arXiv:2502.14105) was submitted on February 19, 2025, with the latest revision on May 19, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a19b2cbc-a2fe-440d-9b7e-d9d1780eb51a",
  "isSidechain": false,
  "promptId": "bf7c039c-9c46-4596-82cc-fdd9084f898b",
  "type": "user",
  "uuid": "0c800c5d-4f6f-421a-9410-37691b1f2b87",
  "toolUseResult": {
    "query": "LP-CP conformal prediction Lévy-Prokhorov distribution shift NeurIPS 2025 arXiv:2502.14105",
    "results": [
      {
        "tool_use_id": "srvtoolu_011EmNyLzhVqyWEM6EpCUz6i",
        "content": [
          {
            "title": "[2502.14105] Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/abs/2502.14105"
          },
          {
            "title": "Conformal Prediction under Lévy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations | OpenReview",
            "url": "https://openreview.net/forum?id=1ULQvdbZ3X"
          },
          {
            "title": "(PDF) Conformal Prediction under L\\'evy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://www.researchgate.net/publication/389176501_Conformal_Prediction_under_L'evy-Prokhorov_Distribution_Shifts_Robustness_to_Local_and_Global_Perturbations"
          },
          {
            "title": "NeurIPS Poster Conformal Prediction under Lévy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://neurips.cc/virtual/2025/loc/san-diego/poster/120230"
          },
          {
            "title": "Conformal Prediction under Lévy-Prokhorov Distribution ...",
            "url": "https://arxiv.org/pdf/2502.14105"
          },
          {
            "title": "Coverage Guarantees for Pseudo-Calibrated Conformal Prediction under Distribution Shift",
            "url": "https://arxiv.org/html/2602.14913v1"
          },
          {
            "title": "Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/html/2502.14105v2"
          }
        ]
      },
      "I found the paper you're looking for. Here's what the search revealed:\n\nThe paper addresses conformal prediction's robustness under distribution shifts by modeling distribution shifts using Lévy-Prokhorov (LP) ambiguity sets, which capture both local and global perturbations.\n\nThe authors provide an overview of LP ambiguity sets and their connections to popular metrics such as Wasserstein and Total Variation. The key contribution is showing that by propagating the LP ambiguity set through the scoring function, complex high-dimensional distribution shifts can be reduced to manageable one-dimensional distribution shifts, enabling exact quantification of worst-case quantiles and coverage.\n\nThe paper was presented as a NeurIPS 2025 poster. The arxiv paper (arXiv:2502.14105) was submitted on February 19, 2025, with the latest revision on May 19, 2025."
    ],
    "durationSeconds": 5.131423684,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a19b2cbc-a2fe-440d-9b7e-d9d1780eb51a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-30T07:51:02.843Z_

<details><summary>↩ Tool result · `toolu_0195NEjuuVbvChN49qPsJ8kG`</summary>

```text
Web search results for query: "conformal prediction RAG retrieval augmented generation TRAQ C-RAG 2024 2025"

Links: [{"title":"GitHub - Arstanley/Awesome-Trustworthy-RAG · GitHub","url":"https://github.com/Arstanley/Awesome-Trustworthy-RAG"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal   Prediction","url":"https://arxiv.org/pdf/2307.04642"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.210/"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction","url":"https://arxiv.org/html/2307.04642v2"},{"title":"Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-21300-6_45"},{"title":"Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/html/2506.20978"}]

Based on the web search results, I found relevant information about conformal prediction applied to RAG systems. Here are the key findings:

## TRAQ: Trustworthy Retrieval Augmented Question Answering

TRAQ provides the first end-to-end statistical correctness guarantee for RAG. TRAQ uses conformal prediction, a statistical technique for constructing prediction sets that are guaranteed to contain the semantically correct response with high probability.

While retrieval augmented generation (RAG) is a promising strategy to avoid hallucinations, it does not provide guarantees on its correctness, and TRAQ addresses this challenge. The framework introduces a novel nonconformity measure that estimates the uncertainty for each semantically distinct meaning and obtains a coverage guarantee at the semantic level.

## C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models

C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models was published in ICML in 2024.02

## Related Work (2024-2025)

CONFLARE: CONFormal LArge language model REtrieval was published in April 2024. Additionally, conformal prediction provides a stronger theoretical foundation for ensuring soundness of evaluations through statistical guarantees compared to traditional auto-evaluation methods for RAG systems.

The search results show active research in combining conformal prediction with RAG systems in 2024-2025, with multiple approaches emerging to provide statistical guarantees for RAG reliability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc2328ad-e34e-4ab1-ad86-9e54d7c4ed33",
  "isSidechain": false,
  "promptId": "bf7c039c-9c46-4596-82cc-fdd9084f898b",
  "type": "user",
  "uuid": "6d387c61-7150-4b77-9911-285e5b8f1489",
  "toolUseResult": {
    "query": "conformal prediction RAG retrieval augmented generation TRAQ C-RAG 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_013CQvkyEhUauNHpWnJ61AoB",
        "content": [
          {
            "title": "GitHub - Arstanley/Awesome-Trustworthy-RAG · GitHub",
            "url": "https://github.com/Arstanley/Awesome-Trustworthy-RAG"
          },
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal   Prediction",
            "url": "https://arxiv.org/pdf/2307.04642"
          },
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction - ACL Anthology",
            "url": "https://aclanthology.org/2024.naacl-long.210/"
          },
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction",
            "url": "https://arxiv.org/html/2307.04642v2"
          },
          {
            "title": "Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-3-032-21300-6_45"
          },
          {
            "title": "Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality",
            "url": "https://arxiv.org/html/2506.20978"
          }
        ]
      },
      "Based on the web search results, I found relevant information about conformal prediction applied to RAG systems. Here are the key findings:\n\n## TRAQ: Trustworthy Retrieval Augmented Question Answering\n\nTRAQ provides the first end-to-end statistical correctness guarantee for RAG. TRAQ uses conformal prediction, a statistical technique for constructing prediction sets that are guaranteed to contain the semantically correct response with high probability.\n\nWhile retrieval augmented generation (RAG) is a promising strategy to avoid hallucinations, it does not provide guarantees on its correctness, and TRAQ addresses this challenge. The framework introduces a novel nonconformity measure that estimates the uncertainty for each semantically distinct meaning and obtains a coverage guarantee at the semantic level.\n\n## C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models\n\nC-RAG: Certified Generation Risks for Retrieval-Augmented Language Models was published in ICML in 2024.02\n\n## Related Work (2024-2025)\n\nCONFLARE: CONFormal LArge language model REtrieval was published in April 2024. Additionally, conformal prediction provides a stronger theoretical foundation for ensuring soundness of evaluations through statistical guarantees compared to traditional auto-evaluation methods for RAG systems.\n\nThe search results show active research in combining conformal prediction with RAG systems in 2024-2025, with multiple approaches emerging to provide statistical guarantees for RAG reliability."
    ],
    "durationSeconds": 6.772738919000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fc2328ad-e34e-4ab1-ad86-9e54d7c4ed33",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-30T07:51:06.404Z_

<details><summary>↩ Tool result · `toolu_011QFz8cxMeXbZsYNdpPihyz`</summary>

```text
Web search results for query: "RobustRAG certified defense RAG poisoning SaTML 2026 ReliabilityRAG NeurIPS 2025"

Links: [{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/pdf/2405.15556"},{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"Certified Defenses for RAG Systems","url":"https://www.emergentmind.com/topics/certified-defenses-for-rag-systems"},{"title":"ICML Certifiably Robust RAG against Retrieval Corruption","url":"https://icml.cc/virtual/2024/37487"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://openreview.net/pdf?id=qsEeACAJjD"},{"title":"Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems","url":"https://arxiv.org/html/2511.01268v1"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/html/2405.15556v2"},{"title":"Certifiably Robust RAG against Retrieval Corruption Attacks | OpenReview","url":"https://openreview.net/forum?id=cU6ZdN87p3"},{"title":"[2405.15556] Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/abs/2405.15556"},{"title":"RAG Poisoning: Threats and Defenses","url":"https://www.emergentmind.com/topics/retrieval-augmented-generation-rag-poisoning"}]

Links: [{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/pdf/2509.23519"},{"title":"NeurIPS Poster ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://neurips.cc/virtual/2025/poster/119236"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://neurips.cc/media/neurips-2025/Slides/119236.pdf"},{"title":"Retrieval-Augmented Generation with Estimation of Source Reliability","url":"https://arxiv.org/pdf/2410.22954"},{"title":"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/pdf/2603.16817"},{"title":"Quantifying Document Impact in RAG-LLMs","url":"https://arxiv.org/pdf/2601.05260"}]

Based on the search results, here's what I found about your query:

## RobustRAG

RobustRAG is the first defense framework with certifiable robustness against retrieval corruption attacks. The key insight of RobustRAG is an isolate-then-aggregate strategy: it isolates passages into disjoint groups, generates LLM responses based on the concatenated passages from each isolated group, and then securely aggregates these responses for a robust output.

RobustRAG achieves substantial certifiable robustness while maintaining high clean performance, e.g., 71% clean accuracy and 38% certifiable robust accuracy on the RealtimeQA dataset, compared to 69% clean accuracy and no certifiable accuracy for vanilla RAG.

## ReliabilityRAG

ReliabilityRAG was presented at the 39th Conference on Neural Information Processing Systems (NeurIPS 2025). ReliabilityRAG is a framework for adversarial robustness that explicitly leverages reliability information of retrieved documents.

ReliabilityRAG introduces a novel algorithm based on finding a Maximum Independent Set (MIS) on a document graph where edges encode contradiction, with a MIS variant that explicitly prioritizes higher-reliability documents and provides provable robustness guarantees.

ReliabilityRAG provides superior robustness against adversarial attacks compared to prior methods, maintains high benign accuracy, and excels in long-form generation tasks where prior robustness-focused methods struggled.

I did not find specific information about SaTML 2026 in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5adaf37-c2d6-4a51-be1a-2333a782e0a0",
  "isSidechain": false,
  "promptId": "bf7c039c-9c46-4596-82cc-fdd9084f898b",
  "type": "user",
  "uuid": "5818638f-5a27-4712-afd1-4ba2457e425c",
  "toolUseResult": {
    "query": "RobustRAG certified defense RAG poisoning SaTML 2026 ReliabilityRAG NeurIPS 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CoWFsLjKQ8xLLHrr99bD8P",
        "content": [
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://arxiv.org/pdf/2405.15556"
          },
          {
            "title": "RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2512.24268"
          },
          {
            "title": "Certified Defenses for RAG Systems",
            "url": "https://www.emergentmind.com/topics/certified-defenses-for-rag-systems"
          },
          {
            "title": "ICML Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://icml.cc/virtual/2024/37487"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://openreview.net/pdf?id=qsEeACAJjD"
          },
          {
            "title": "Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems",
            "url": "https://arxiv.org/html/2511.01268v1"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://arxiv.org/html/2405.15556v2"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption Attacks | OpenReview",
            "url": "https://openreview.net/forum?id=cU6ZdN87p3"
          },
          {
            "title": "[2405.15556] Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://arxiv.org/abs/2405.15556"
          },
          {
            "title": "RAG Poisoning: Threats and Defenses",
            "url": "https://www.emergentmind.com/topics/retrieval-augmented-generation-rag-poisoning"
          }
        ]
      },
      {
        "tool_use_id": "srvtoolu_01VwC5njecxL2d1ZPaw3AjC8",
        "content": [
          {
            "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://arxiv.org/pdf/2509.23519"
          },
          {
            "title": "NeurIPS Poster ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://neurips.cc/virtual/2025/poster/119236"
          },
          {
            "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://neurips.cc/media/neurips-2025/Slides/119236.pdf"
          },
          {
            "title": "Retrieval-Augmented Generation with Estimation of Source Reliability",
            "url": "https://arxiv.org/pdf/2410.22954"
          },
          {
            "title": "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights",
            "url": "https://arxiv.org/pdf/2603.16817"
          },
          {
            "title": "Quantifying Document Impact in RAG-LLMs",
            "url": "https://arxiv.org/pdf/2601.05260"
          }
        ]
      },
      "Based on the search results, here's what I found about your query:\n\n## RobustRAG\n\nRobustRAG is the first defense framework with certifiable robustness against retrieval corruption attacks. The key insight of RobustRAG is an isolate-then-aggregate strategy: it isolates passages into disjoint groups, generates LLM responses based on the concatenated passages from each isolated group, and then securely aggregates these responses for a robust output.\n\nRobustRAG achieves substantial certifiable robustness while maintaining high clean performance, e.g., 71% clean accuracy and 38% certifiable robust accuracy on the RealtimeQA dataset, compared to 69% clean accuracy and no certifiable accuracy for vanilla RAG.\n\n## ReliabilityRAG\n\nReliabilityRAG was presented at the 39th Conference on Neural Information Processing Systems (NeurIPS 2025). ReliabilityRAG is a framework for adversarial robustness that explicitly leverages reliability information of retrieved documents.\n\nReliabilityRAG introduces a novel algorithm based on finding a Maximum Independent Set (MIS) on a document graph where edges encode contradiction, with a MIS variant that explicitly prioritizes higher-reliability documents and provides provable robustness guarantees.\n\nReliabilityRAG provides superior robustness against adversarial attacks compared to prior methods, maintains high benign accuracy, and excels in long-form generation tasks where prior robustness-focused methods struggled.\n\nI did not find specific information about SaTML 2026 in the search results."
    ],
    "durationSeconds": 9.832307065,
    "searchCount": 2
  },
  "sourceToolAssistantUUID": "b5adaf37-c2d6-4a51-be1a-2333a782e0a0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-30T07:51:10.773Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I've gathered initial information. Let me now search for more specific topics:
1. RAG poisoning attacks (PoisonedRAG, CorruptRAG)
2. Conformal prediction + adversarial robustness intersection
3. Any concurrent work that might overlap with this proposal
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5818638f-5a27-4712-afd1-4ba2457e425c",
  "isSidechain": false,
  "requestId": "req_011CbYPWEFTF9kwVzmEFXtUt",
  "type": "assistant",
  "uuid": "57845d7b-af54-4403-bb59-51dde19363fe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018YR2rLpDEihfXnotro3WAc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2925,
      "cache_read_input_tokens": 19965,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2925,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 218,
          "cache_read_input_tokens": 19965,
          "cache_creation_input_tokens": 2925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2925
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

_source line 19 · 2026-05-30T07:51:11.734Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WGxMC9HJviTvSSMyL8mt7v`</summary>

```json
{
  "query": "PoisonedRAG corpus poisoning attack CorruptRAG 2025 2026 RAG adversarial defense landscape"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57845d7b-af54-4403-bb59-51dde19363fe",
  "isSidechain": false,
  "requestId": "req_011CbYPWEFTF9kwVzmEFXtUt",
  "type": "assistant",
  "uuid": "4c0da06f-f9df-438e-a245-99c71dbe10f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018YR2rLpDEihfXnotro3WAc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2925,
      "cache_read_input_tokens": 19965,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2925,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 218,
          "cache_read_input_tokens": 19965,
          "cache_creation_input_tokens": 2925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2925
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

_source line 20 · 2026-05-30T07:51:11.903Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012FwFZG3np7jNysvNdfjpQL`</summary>

```json
{
  "query": "conformal prediction adversarial robustness certified abstention 2025 2026 RAG distribution shift"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c0da06f-f9df-438e-a245-99c71dbe10f5",
  "isSidechain": false,
  "requestId": "req_011CbYPWEFTF9kwVzmEFXtUt",
  "type": "assistant",
  "uuid": "b8df1293-fd48-40ea-8cfe-290e4950ff6c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018YR2rLpDEihfXnotro3WAc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2925,
      "cache_read_input_tokens": 19965,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2925,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 218,
          "cache_read_input_tokens": 19965,
          "cache_creation_input_tokens": 2925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2925
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

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Conformal Abstention for RAG under LP-Bounded Retrieval Shifts  ## Core Problem  How can a RAG system provide di…",
  "leafUuid": "b8df1293-fd48-40ea-8cfe-290e4950ff6c",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Certified RAG abstention under retrieval poisoning",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b"
}
```

---

### Tool result

_source line 23 · 2026-05-30T07:51:21.808Z_

<details><summary>↩ Tool result · `toolu_012FwFZG3np7jNysvNdfjpQL`</summary>

```text
Web search results for query: "conformal prediction adversarial robustness certified abstention 2025 2026 RAG distribution shift"

Links: [{"title":"Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks - King's College London","url":"https://kclpure.kcl.ac.uk/portal/en/publications/verifiably-robust-conformal-prediction-for-probabilistic-guarante"},{"title":"Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability | OpenReview","url":"https://openreview.net/forum?id=Oty1LQrnFc"},{"title":"[2502.07255] Beyond Confidence: Adaptive Abstention in Dual-Threshold Conformal Prediction for Autonomous System Perception","url":"https://arxiv.org/abs/2502.07255"},{"title":"Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0031320325007113"},{"title":"Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://arxiv.org/html/2506.07804v1"},{"title":"(PDF) Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks","url":"https://www.researchgate.net/publication/397934771_Ensuring_Calibration_Robustness_in_Split_Conformal_Prediction_Under_Adversarial_Attacks"},{"title":"Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://arxiv.org/pdf/2506.07804"},{"title":"Paraphrase-Robust Conformal Prediction for Reliable LLM Uncertainty Quantification | OpenReview","url":"https://openreview.net/forum?id=Uf04r8gDn7"}]

Links: [{"title":"Adaptive Conformal Inference Under Distribution Shift","url":"https://arxiv.org/pdf/2106.00170"},{"title":"Conformal Prediction: A Data Perspective | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3736575"},{"title":"Online Conformal Inference with Retrospective Adjustment for Faster Adaptation to Distribution Shift","url":"https://arxiv.org/pdf/2511.04275"},{"title":"Conformal Prediction: A Data Perspective","url":"https://arxiv.org/pdf/2410.06494"},{"title":"Estimating Test Performance for AI Medical Devices under Distribution   Shift with Conformal Prediction","url":"https://arxiv.org/pdf/2207.05796"},{"title":"Robust Conformal Prediction under Distribution Shift via   Physics-Informed Structural Causal Model","url":"https://arxiv.org/pdf/2403.15025"},{"title":"Conformal Inference for Online Prediction with Arbitrary Distribution   Shifts","url":"https://arxiv.org/pdf/2208.08401"},{"title":"Not all distributional shifts are equal: Fine-grained robust conformal inference","url":"https://arxiv.org/pdf/2402.13042"},{"title":"Wasserstein-Regularized Conformal Prediction under General Distribution Shift | OpenReview","url":"https://openreview.net/forum?id=aJ3tiX1Tu4"}]

I've completed the web search for your query on conformal prediction, adversarial robustness, certified abstention, and distribution shift. Here are the key findings:

## Recent Research (2025-2026)

**Adversarial Robustness and Certified Guarantees:**

Conformal Prediction is a popular uncertainty quantification method that provides distribution-free, statistically valid prediction sets, with prediction sets guaranteed to cover the true test output with a user-specified probability; however, this guarantee is violated when data is subjected to adversarial attacks, which often result in a significant loss of coverage. 

A recent method called Verifiably Robust Conformal Prediction (VRCP) combines CP with neural network verification to recover conformal prediction's probabilistic guarantees under adversarial attacks.

**Certified Abstention:**

A framework for autonomous system perception demonstrates robust coverage (>84.5%) while appropriately abstaining from unreliable predictions, with detection performance (AUC: 0.995 +/- 0.001) significantly outperforming existing methods across all modalities.

**Distribution Shift and RAG:**

Research shows that applying conformal risk control with RAG demonstrates that using RAG can lead to lower risk than normal LLM with or without covariate shift.

Online conformal inference has emerged as a framework for constructing distribution-free prediction sets; however, existing approaches slowly adapt to distribution shifts because they update predictions only in a forward manner, and a novel method with retrospective adjustment has been proposed to achieve faster adaptation to distributional shifts.

For Large Language Models, a new framework for paraphrase-robust uncertainty quantification builds on conformal prediction to ensure valid coverage and introduces a paraphrase-aware nonconformity score derived by generating independent semantic paraphrases and aggregating variability across them.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8df1293-fd48-40ea-8cfe-290e4950ff6c",
  "isSidechain": false,
  "promptId": "bf7c039c-9c46-4596-82cc-fdd9084f898b",
  "type": "user",
  "uuid": "d5beb182-f1b1-43a6-ab7d-042b1bc3e205",
  "toolUseResult": {
    "query": "conformal prediction adversarial robustness certified abstention 2025 2026 RAG distribution shift",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HHisws89M3tyXJ3GRMGBEC",
        "content": [
          {
            "title": "Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks - King's College London",
            "url": "https://kclpure.kcl.ac.uk/portal/en/publications/verifiably-robust-conformal-prediction-for-probabilistic-guarante"
          },
          {
            "title": "Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability | OpenReview",
            "url": "https://openreview.net/forum?id=Oty1LQrnFc"
          },
          {
            "title": "[2502.07255] Beyond Confidence: Adaptive Abstention in Dual-Threshold Conformal Prediction for Autonomous System Perception",
            "url": "https://arxiv.org/abs/2502.07255"
          },
          {
            "title": "Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S0031320325007113"
          },
          {
            "title": "Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability",
            "url": "https://arxiv.org/html/2506.07804v1"
          },
          {
            "title": "(PDF) Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks",
            "url": "https://www.researchgate.net/publication/397934771_Ensuring_Calibration_Robustness_in_Split_Conformal_Prediction_Under_Adversarial_Attacks"
          },
          {
            "title": "Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability",
            "url": "https://arxiv.org/pdf/2506.07804"
          },
          {
            "title": "Paraphrase-Robust Conformal Prediction for Reliable LLM Uncertainty Quantification | OpenReview",
            "url": "https://openreview.net/forum?id=Uf04r8gDn7"
          }
        ]
      },
      {
        "tool_use_id": "srvtoolu_01AWXpNrNTSMUeT3HnyrP9Rj",
        "content": [
          {
            "title": "Adaptive Conformal Inference Under Distribution Shift",
            "url": "https://arxiv.org/pdf/2106.00170"
          },
          {
            "title": "Conformal Prediction: A Data Perspective | ACM Computing Surveys",
            "url": "https://dl.acm.org/doi/10.1145/3736575"
          },
          {
            "title": "Online Conformal Inference with Retrospective Adjustment for Faster Adaptation to Distribution Shift",
            "url": "https://arxiv.org/pdf/2511.04275"
          },
          {
            "title": "Conformal Prediction: A Data Perspective",
            "url": "https://arxiv.org/pdf/2410.06494"
          },
          {
            "title": "Estimating Test Performance for AI Medical Devices under Distribution   Shift with Conformal Prediction",
            "url": "https://arxiv.org/pdf/2207.05796"
          },
          {
            "title": "Robust Conformal Prediction under Distribution Shift via   Physics-Informed Structural Causal Model",
            "url": "https://arxiv.org/pdf/2403.15025"
          },
          {
            "title": "Conformal Inference for Online Prediction with Arbitrary Distribution   Shifts",
            "url": "https://arxiv.org/pdf/2208.08401"
          },
          {
            "title": "Not all distributional shifts are equal: Fine-grained robust conformal inference",
            "url": "https://arxiv.org/pdf/2402.13042"
          },
          {
            "title": "Wasserstein-Regularized Conformal Prediction under General Distribution Shift | OpenReview",
            "url": "https://openreview.net/forum?id=aJ3tiX1Tu4"
          }
        ]
      },
      "I've completed the web search for your query on conformal prediction, adversarial robustness, certified abstention, and distribution shift. Here are the key findings:\n\n## Recent Research (2025-2026)\n\n**Adversarial Robustness and Certified Guarantees:**\n\nConformal Prediction is a popular uncertainty quantification method that provides distribution-free, statistically valid prediction sets, with prediction sets guaranteed to cover the true test output with a user-specified probability; however, this guarantee is violated when data is subjected to adversarial attacks, which often result in a significant loss of coverage. \n\nA recent method called Verifiably Robust Conformal Prediction (VRCP) combines CP with neural network verification to recover conformal prediction's probabilistic guarantees under adversarial attacks.\n\n**Certified Abstention:**\n\nA framework for autonomous system perception demonstrates robust coverage (>84.5%) while appropriately abstaining from unreliable predictions, with detection performance (AUC: 0.995 +/- 0.001) significantly outperforming existing methods across all modalities.\n\n**Distribution Shift and RAG:**\n\nResearch shows that applying conformal risk control with RAG demonstrates that using RAG can lead to lower risk than normal LLM with or without covariate shift.\n\nOnline conformal inference has emerged as a framework for constructing distribution-free prediction sets; however, existing approaches slowly adapt to distribution shifts because they update predictions only in a forward manner, and a novel method with retrospective adjustment has been proposed to achieve faster adaptation to distributional shifts.\n\nFor Large Language Models, a new framework for paraphrase-robust uncertainty quantification builds on conformal prediction to ensure valid coverage and introduces a paraphrase-aware nonconformity score derived by generating independent semantic paraphrases and aggregating variability across them."
    ],
    "durationSeconds": 9.898813858,
    "searchCount": 2
  },
  "sourceToolAssistantUUID": "b8df1293-fd48-40ea-8cfe-290e4950ff6c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-30T07:51:22.897Z_

<details><summary>↩ Tool result · `toolu_01WGxMC9HJviTvSSMyL8mt7v`</summary>

```text
Web search results for query: "PoisonedRAG corpus poisoning attack CorruptRAG 2025 2026 RAG adversarial defense landscape"

Links: [{"title":"RAG Poisoning: Contaminating the AI's \"Source of Truth\"","url":"https://instatunnel.substack.com/p/rag-poisoning-contaminating-the-ais"},{"title":"RAG Poisoning: Contaminating the AI’s “Source of Truth” | by InstaTunnel | Medium","url":"https://medium.com/@instatunnel/rag-poisoning-contaminating-the-ais-source-of-truth-082dcbdeea7c"},{"title":"RAG Poisoning: Threats and Defenses","url":"https://www.emergentmind.com/topics/retrieval-augmented-generation-rag-poisoning"},{"title":"Practical Poisoning Attacks against Retrieval-Augmented Generation Baolei Zhang","url":"https://arxiv.org/pdf/2504.03957"},{"title":"Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems","url":"https://arxiv.org/html/2603.18034v1"},{"title":"Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems","url":"https://arxiv.org/pdf/2603.18034"},{"title":"Addressing Corpus Knowledge Poisoning Attacks on RAG Using Sparse Attention","url":"https://arxiv.org/pdf/2602.04711"}]

Based on the search results, here's an overview of the RAG corpus poisoning attack landscape in 2025-2026:

## Key Attack Methods

Recent 2025–2026 research covers sophisticated attacks like "PoisonedRAG," "CorruptRAG," "PoisonedEye," and "Phantom".

PoisonedRAG (Zou et al., 2025) formulates knowledge corruption as an optimization problem with retrieval and generation conditions, achieving 90 % attack success on standard QA benchmarks.

Research published in January 2026 introduces CorruptRAG, a practical poisoning attack requiring only a single poisoned text injection, significantly enhancing both feasibility and stealth compared to earlier methods.

## Attack Severity

Recent research demonstrates that injecting just five malicious texts into a knowledge database containing millions of documents can achieve a 90% attack success rate, while poisoning merely 0.04% of a corpus can lead to a 98.2% attack success rate and 74.6% system failure.

## Advanced Attack Variants

Recent methodologies such as CorruptRAG and AuthChain achieve high attack success with a single adversarial document per query, while CPA-RAG, CorruptRAG, and POISONCRAFT demonstrate attack transferability across a variety of retrievers and LLMs.

Confundo fine-tunes a poison generator to maximize attack success rate even when queries are paraphrased and ingestion pipelines chunk or reformat content, substantially closing the gap between controlled-benchmark and real-world attack success.

## Defense Landscape

RAG Security Bench (Wang et al., 2025) provides comprehensive evaluation, testing 13 poisoning methods across 5 datasets with 7 defense mechanisms and finding that hybrid defenses outperform single-mechanism approaches but still leave residual risk.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c0da06f-f9df-438e-a245-99c71dbe10f5",
  "isSidechain": false,
  "promptId": "bf7c039c-9c46-4596-82cc-fdd9084f898b",
  "type": "user",
  "uuid": "6cdee689-33e2-4d1d-8bfd-4e0d2ee2ed63",
  "toolUseResult": {
    "query": "PoisonedRAG corpus poisoning attack CorruptRAG 2025 2026 RAG adversarial defense landscape",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MybmQBCvchQsMiiNNA2SfS",
        "content": [
          {
            "title": "RAG Poisoning: Contaminating the AI's \"Source of Truth\"",
            "url": "https://instatunnel.substack.com/p/rag-poisoning-contaminating-the-ais"
          },
          {
            "title": "RAG Poisoning: Contaminating the AI’s “Source of Truth” | by InstaTunnel | Medium",
            "url": "https://medium.com/@instatunnel/rag-poisoning-contaminating-the-ais-source-of-truth-082dcbdeea7c"
          },
          {
            "title": "RAG Poisoning: Threats and Defenses",
            "url": "https://www.emergentmind.com/topics/retrieval-augmented-generation-rag-poisoning"
          },
          {
            "title": "Practical Poisoning Attacks against Retrieval-Augmented Generation Baolei Zhang",
            "url": "https://arxiv.org/pdf/2504.03957"
          },
          {
            "title": "Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems",
            "url": "https://arxiv.org/html/2603.18034v1"
          },
          {
            "title": "Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems",
            "url": "https://arxiv.org/pdf/2603.18034"
          },
          {
            "title": "Addressing Corpus Knowledge Poisoning Attacks on RAG Using Sparse Attention",
            "url": "https://arxiv.org/pdf/2602.04711"
          }
        ]
      },
      "Based on the search results, here's an overview of the RAG corpus poisoning attack landscape in 2025-2026:\n\n## Key Attack Methods\n\nRecent 2025–2026 research covers sophisticated attacks like \"PoisonedRAG,\" \"CorruptRAG,\" \"PoisonedEye,\" and \"Phantom\".\n\nPoisonedRAG (Zou et al., 2025) formulates knowledge corruption as an optimization problem with retrieval and generation conditions, achieving 90 % attack success on standard QA benchmarks.\n\nResearch published in January 2026 introduces CorruptRAG, a practical poisoning attack requiring only a single poisoned text injection, significantly enhancing both feasibility and stealth compared to earlier methods.\n\n## Attack Severity\n\nRecent research demonstrates that injecting just five malicious texts into a knowledge database containing millions of documents can achieve a 90% attack success rate, while poisoning merely 0.04% of a corpus can lead to a 98.2% attack success rate and 74.6% system failure.\n\n## Advanced Attack Variants\n\nRecent methodologies such as CorruptRAG and AuthChain achieve high attack success with a single adversarial document per query, while CPA-RAG, CorruptRAG, and POISONCRAFT demonstrate attack transferability across a variety of retrievers and LLMs.\n\nConfundo fine-tunes a poison generator to maximize attack success rate even when queries are paraphrased and ingestion pipelines chunk or reformat content, substantially closing the gap between controlled-benchmark and real-world attack success.\n\n## Defense Landscape\n\nRAG Security Bench (Wang et al., 2025) provides comprehensive evaluation, testing 13 poisoning methods across 5 datasets with 7 defense mechanisms and finding that hybrid defenses outperform single-mechanism approaches but still leave residual risk."
    ],
    "durationSeconds": 11.156944345,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4c0da06f-f9df-438e-a245-99c71dbe10f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-30T07:51:28.897Z_

<details><summary>Logged reasoning block</summary>

```text
Let me do a couple more targeted searches to check for:
1. Any concurrent work specifically at the intersection of conformal prediction + RAG + adversarial robustness
2. The specific Chen et al. paper about conformal factuality robustness for RAG
3. RAGDefender and its cosine similarity approach
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6cdee689-33e2-4d1d-8bfd-4e0d2ee2ed63",
  "isSidechain": false,
  "requestId": "req_011CbYPXSvjGGB5WfgNajD7Y",
  "type": "assistant",
  "uuid": "a7aea022-9dd6-4eb2-8f76-1d316b739284",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JhbAjwGxMH8v7isXH7Fcgz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1322,
      "cache_creation_input_tokens": 1066,
      "cache_read_input_tokens": 22890,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1066,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1322,
          "output_tokens": 219,
          "cache_read_input_tokens": 22890,
          "cache_creation_input_tokens": 1066,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1066
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

_source line 26 · 2026-05-30T07:51:29.939Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FkqwQ1Uj71Bh7bhJJB3fta`</summary>

```json
{
  "query": "\"conformal prediction\" \"RAG\" \"adversarial\" OR \"poisoning\" certified abstention 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7aea022-9dd6-4eb2-8f76-1d316b739284",
  "isSidechain": false,
  "requestId": "req_011CbYPXSvjGGB5WfgNajD7Y",
  "type": "assistant",
  "uuid": "af4a6172-972e-4819-80ab-6b5b4582c4d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JhbAjwGxMH8v7isXH7Fcgz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1322,
      "cache_creation_input_tokens": 1066,
      "cache_read_input_tokens": 22890,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1066,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1322,
          "output_tokens": 219,
          "cache_read_input_tokens": 22890,
          "cache_creation_input_tokens": 1066,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1066
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

_source line 27 · 2026-05-30T07:51:30.591Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019vbghRYoW22g5sqvXgUuJm`</summary>

```json
{
  "query": "RAGDefender cosine similarity clustering defense poisoning ACSAC 2025 TrustRAG"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af4a6172-972e-4819-80ab-6b5b4582c4d1",
  "isSidechain": false,
  "requestId": "req_011CbYPXSvjGGB5WfgNajD7Y",
  "type": "assistant",
  "uuid": "705e7b8f-fcc1-4c22-b4fc-e647ce39e3dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JhbAjwGxMH8v7isXH7Fcgz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1322,
      "cache_creation_input_tokens": 1066,
      "cache_read_input_tokens": 22890,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1066,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1322,
          "output_tokens": 219,
          "cache_read_input_tokens": 22890,
          "cache_creation_input_tokens": 1066,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1066
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

_source line 28 · 2026-05-30T07:51:37.699Z_

<details><summary>↩ Tool result · `toolu_019vbghRYoW22g5sqvXgUuJm`</summary>

```text
Web search results for query: "RAGDefender cosine similarity clustering defense poisoning ACSAC 2025 TrustRAG"

Links: [{"title":"TrustRAG: Enhancing Robustness and Trustworthiness in RAG","url":"https://arxiv.org/html/2501.00879v1"},{"title":"TrustRAG: RAG Defense framework to counter attacks from malicious injected docs | by SACHIN KUMAR | Medium","url":"https://medium.com/@techsachin/trustrag-rag-defense-framework-to-counter-attacks-from-malicious-injected-docs-996f5cd4af21"},{"title":"GitHub - SecAI-Lab/RAGDefender: Artifacts for paper \"Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems\" · GitHub","url":"https://github.com/SecAI-Lab/RAGDefender"},{"title":"Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems","url":"https://arxiv.org/html/2511.01268v1"},{"title":"Secure Retrieval-Augmented Generation against Poisoning Attacks","url":"https://arxiv.org/html/2510.25025v1"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://openreview.net/pdf?id=D9JeNTs5Bu"},{"title":"TrustRAG: Enhancing Robustness and Trustworthiness in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2501.00879"},{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"}]

Based on the search results, I found information about both RAGDefender and TrustRAG, which are two distinct defense mechanisms against corpus poisoning attacks in RAG systems:

## TrustRAG

TrustRAG is a robust framework that systematically filters compromised and irrelevant content before it reaches the language model. It implements a two-stage defense mechanism: first, it employs K-means clustering to identify potential attack patterns in retrieved documents based on their semantic embeddings, and second, it leverages cosine similarity and ROUGE metrics to detect malicious documents while resolving discrepancies between the model's internal knowledge and external information through a self-assessment process. TrustRAG functions as a plug-and-play, training-free module that integrates seamlessly with any language model, whether open or closed-source.

## RAGDefender

RAGDefender is a resource-efficient defense mechanism against knowledge corruption (data poisoning) attacks in practical RAG deployments by filtering out potentially adversarial documents. It devises two novel strategies (clustering-based and concentration-based grouping) to rescue legitimate (unpoisoned) passages at the first stage. RAGDefender is presented in the paper "Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems" at the Annual Computer Security Applications Conference (ACSAC) 2025.

Both approaches focus on defending RAG systems against corpus poisoning attacks, with clustering and similarity metrics playing key roles in identifying malicious content.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "705e7b8f-fcc1-4c22-b4fc-e647ce39e3dd",
  "isSidechain": false,
  "promptId": "bf7c039c-9c46-4596-82cc-fdd9084f898b",
  "type": "user",
  "uuid": "d95d3f8c-d7a0-4f2a-af6e-5187d3f623ff",
  "toolUseResult": {
    "query": "RAGDefender cosine similarity clustering defense poisoning ACSAC 2025 TrustRAG",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LDGY5jnkeLAzgPMj3EpA6L",
        "content": [
          {
            "title": "TrustRAG: Enhancing Robustness and Trustworthiness in RAG",
            "url": "https://arxiv.org/html/2501.00879v1"
          },
          {
            "title": "TrustRAG: RAG Defense framework to counter attacks from malicious injected docs | by SACHIN KUMAR | Medium",
            "url": "https://medium.com/@techsachin/trustrag-rag-defense-framework-to-counter-attacks-from-malicious-injected-docs-996f5cd4af21"
          },
          {
            "title": "GitHub - SecAI-Lab/RAGDefender: Artifacts for paper \"Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems\" · GitHub",
            "url": "https://github.com/SecAI-Lab/RAGDefender"
          },
          {
            "title": "Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems",
            "url": "https://arxiv.org/html/2511.01268v1"
          },
          {
            "title": "Secure Retrieval-Augmented Generation against Poisoning Attacks",
            "url": "https://arxiv.org/html/2510.25025v1"
          },
          {
            "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://openreview.net/pdf?id=D9JeNTs5Bu"
          },
          {
            "title": "TrustRAG: Enhancing Robustness and Trustworthiness in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2501.00879"
          },
          {
            "title": "RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2512.24268"
          }
        ]
      },
      "Based on the search results, I found information about both RAGDefender and TrustRAG, which are two distinct defense mechanisms against corpus poisoning attacks in RAG systems:\n\n## TrustRAG\n\nTrustRAG is a robust framework that systematically filters compromised and irrelevant content before it reaches the language model. It implements a two-stage defense mechanism: first, it employs K-means clustering to identify potential attack patterns in retrieved documents based on their semantic embeddings, and second, it leverages cosine similarity and ROUGE metrics to detect malicious documents while resolving discrepancies between the model's internal knowledge and external information through a self-assessment process. TrustRAG functions as a plug-and-play, training-free module that integrates seamlessly with any language model, whether open or closed-source.\n\n## RAGDefender\n\nRAGDefender is a resource-efficient defense mechanism against knowledge corruption (data poisoning) attacks in practical RAG deployments by filtering out potentially adversarial documents. It devises two novel strategies (clustering-based and concentration-based grouping) to rescue legitimate (unpoisoned) passages at the first stage. RAGDefender is presented in the paper \"Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems\" at the Annual Computer Security Applications Conference (ACSAC) 2025.\n\nBoth approaches focus on defending RAG systems against corpus poisoning attacks, with clustering and similarity metrics playing key roles in identifying malicious content."
    ],
    "durationSeconds": 7.098898015999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "705e7b8f-fcc1-4c22-b4fc-e647ce39e3dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-30T07:51:37.985Z_

<details><summary>↩ Tool result · `toolu_01FkqwQ1Uj71Bh7bhJJB3fta`</summary>

```text
Web search results for query: ""conformal prediction" "RAG" "adversarial" OR "poisoning" certified abstention 2026"

Links: [{"title":"Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks - King's College London","url":"https://kclpure.kcl.ac.uk/portal/en/publications/verifiably-robust-conformal-prediction-for-probabilistic-guarante"},{"title":"Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://arxiv.org/html/2506.07804v1"},{"title":"provably reliable conformal prediction sets","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4d21a4b33361c40c2142db9511c126-Paper-Conference.pdf"},{"title":"Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning","url":"https://arxiv.org/pdf/2410.09878"},{"title":"Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks","url":"https://arxiv.org/pdf/2412.16708"},{"title":"Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0031320325007113"}]

I found relevant research on conformal prediction with adversarial robustness and poisoning attacks. Here are the key findings:

## Conformal Prediction with Adversarial and Poisoning Robustness

**Recent frameworks for certified robustness:**

1. **VRCP (Verifiably Robust Conformal Prediction)**: This framework leverages recent neural network verification methods to recover coverage guarantees under adversarial attacks, and can be used to mitigate poisoning attacks. VRCP is the first to support perturbations bounded by arbitrary norms including ℓ1, ℓ2, and ℓ∞, as well as regression tasks.

2. **Reliable Prediction Sets (RPS)**: This is the first efficient method for constructing conformal prediction sets with provable reliability guarantees under poisoning. RPS is the first scalable and efficient method for making conformal prediction more reliable under training and calibration poisoning.

3. **RAG Adversarial Robustness**: RAG systems are vulnerable to various adversarial poisoning attacks where attackers can inject adversarial data into the underlying RAG database to manipulate the retriever and reduce model accuracy.

The research indicates active development in 2025-2026 of certified approaches combining conformal prediction with defenses against both adversarial and poisoning attacks, though I did not find specific results on certified abstention mechanisms in RAG systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af4a6172-972e-4819-80ab-6b5b4582c4d1",
  "isSidechain": false,
  "promptId": "bf7c039c-9c46-4596-82cc-fdd9084f898b",
  "type": "user",
  "uuid": "3f2df7f9-6e1b-4494-8683-0320586a8939",
  "toolUseResult": {
    "query": "\"conformal prediction\" \"RAG\" \"adversarial\" OR \"poisoning\" certified abstention 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EkpiRxh4K4as6QGWojwvae",
        "content": [
          {
            "title": "Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks - King's College London",
            "url": "https://kclpure.kcl.ac.uk/portal/en/publications/verifiably-robust-conformal-prediction-for-probabilistic-guarante"
          },
          {
            "title": "Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability",
            "url": "https://arxiv.org/html/2506.07804v1"
          },
          {
            "title": "provably reliable conformal prediction sets",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4d21a4b33361c40c2142db9511c126-Paper-Conference.pdf"
          },
          {
            "title": "Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning",
            "url": "https://arxiv.org/pdf/2410.09878"
          },
          {
            "title": "Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks",
            "url": "https://arxiv.org/pdf/2412.16708"
          },
          {
            "title": "Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S0031320325007113"
          }
        ]
      },
      "I found relevant research on conformal prediction with adversarial robustness and poisoning attacks. Here are the key findings:\n\n## Conformal Prediction with Adversarial and Poisoning Robustness\n\n**Recent frameworks for certified robustness:**\n\n1. **VRCP (Verifiably Robust Conformal Prediction)**: This framework leverages recent neural network verification methods to recover coverage guarantees under adversarial attacks, and can be used to mitigate poisoning attacks. VRCP is the first to support perturbations bounded by arbitrary norms including ℓ1, ℓ2, and ℓ∞, as well as regression tasks.\n\n2. **Reliable Prediction Sets (RPS)**: This is the first efficient method for constructing conformal prediction sets with provable reliability guarantees under poisoning. RPS is the first scalable and efficient method for making conformal prediction more reliable under training and calibration poisoning.\n\n3. **RAG Adversarial Robustness**: RAG systems are vulnerable to various adversarial poisoning attacks where attackers can inject adversarial data into the underlying RAG database to manipulate the retriever and reduce model accuracy.\n\nThe research indicates active development in 2025-2026 of certified approaches combining conformal prediction with defenses against both adversarial and poisoning attacks, though I did not find specific results on certified abstention mechanisms in RAG systems."
    ],
    "durationSeconds": 8.040639508,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "af4a6172-972e-4819-80ab-6b5b4582c4d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Conformal Abstention for RAG under LP-Bounded Retrieval Shifts  ## Core Problem  How can a RAG system provide di…",
  "leafUuid": "3f2df7f9-6e1b-4494-8683-0320586a8939",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Certified RAG abstention under retrieval poisoning",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b"
}
```

---

### Assistant

_source line 32 · 2026-05-30T07:51:41.686Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a solid understanding of the landscape. Let me do one more search specifically for the Chen et al. paper about conformal factuality robustness and also check for any very recent work that might be concurrent.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f2df7f9-6e1b-4494-8683-0320586a8939",
  "isSidechain": false,
  "requestId": "req_011CbYPYZF1e3o3nV3xgMHke",
  "type": "assistant",
  "uuid": "84aba84d-80d5-4eb0-b85d-89995ab5fc5f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T95sf9oLvK6dNirDWnC62F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 851,
      "cache_creation_input_tokens": 2276,
      "cache_read_input_tokens": 23956,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2276,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 851,
          "output_tokens": 190,
          "cache_read_input_tokens": 23956,
          "cache_creation_input_tokens": 2276,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2276
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

_source line 33 · 2026-05-30T07:51:42.657Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019KZojRqeMcRi5zn7WrFk6R`</summary>

```json
{
  "query": "Chen \"conformal factuality\" RAG robust arXiv 2603.16817 2026 distribution shift breaks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84aba84d-80d5-4eb0-b85d-89995ab5fc5f",
  "isSidechain": false,
  "requestId": "req_011CbYPYZF1e3o3nV3xgMHke",
  "type": "assistant",
  "uuid": "1bd075ed-6687-4b59-a9ea-ea597148e4fa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T95sf9oLvK6dNirDWnC62F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 851,
      "cache_creation_input_tokens": 2276,
      "cache_read_input_tokens": 23956,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2276,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 851,
          "output_tokens": 190,
          "cache_read_input_tokens": 23956,
          "cache_creation_input_tokens": 2276,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2276
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

_source line 34 · 2026-05-30T07:51:43.343Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BaBfxXaUTZ2Sjd47GCSYtF`</summary>

```json
{
  "query": "Lipschitz conformal prediction score function robust retrieval agreement 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bd075ed-6687-4b59-a9ea-ea597148e4fa",
  "isSidechain": false,
  "requestId": "req_011CbYPYZF1e3o3nV3xgMHke",
  "type": "assistant",
  "uuid": "aef21283-37a9-4f81-a4b1-4906c47db597",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T95sf9oLvK6dNirDWnC62F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 851,
      "cache_creation_input_tokens": 2276,
      "cache_read_input_tokens": 23956,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2276,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 851,
          "output_tokens": 190,
          "cache_read_input_tokens": 23956,
          "cache_creation_input_tokens": 2276,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2276
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

_source line 35 · 2026-05-30T07:51:49.463Z_

<details><summary>↩ Tool result · `toolu_019KZojRqeMcRi5zn7WrFk6R`</summary>

```text
Web search results for query: "Chen "conformal factuality" RAG robust arXiv 2603.16817 2026 distribution shift breaks"

Links: [{"title":"[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/abs/2603.16817"},{"title":"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/pdf/2603.16817"},{"title":"[2506.20978v1] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/abs/2506.20978v1"},{"title":"[2506.20978] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/abs/2506.20978"},{"title":"Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/html/2506.20978v1"}]

I found the paper you were looking for! Here are the key findings:

The paper "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights" (arXiv:2603.16817) was submitted on March 17, 2026 by Yi Chen, Daiwei Chen, Sukrut Madhav Chikodikar, Caitlyn Heqi Yin, and Ramya Korlakai Vinayak.

The research examines the robustness of conformal factuality approaches for RAG-based language models. The study finds that conformal factuality guarantees are not robust to distribution shifts and distractors, highlighting the limitation that calibration data must closely match deployment conditions.

Additionally, the research shows that conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, and lightweight entailment-based verifiers match or outperform LLM-based model confidence scorers while requiring over 100× fewer FLOPs.

The paper appears to expose critical limitations in applying conformal prediction methods to RAG systems when facing distribution shifts in real-world deployment scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1bd075ed-6687-4b59-a9ea-ea597148e4fa",
  "isSidechain": false,
  "promptId": "bf7c039c-9c46-4596-82cc-fdd9084f898b",
  "type": "user",
  "uuid": "7de80774-73a6-45e9-9b61-9579b665c033",
  "toolUseResult": {
    "query": "Chen \"conformal factuality\" RAG robust arXiv 2603.16817 2026 distribution shift breaks",
    "results": [
      {
        "tool_use_id": "srvtoolu_01F2eup7gdPxPPStWqUNzzEo",
        "content": [
          {
            "title": "[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights",
            "url": "https://arxiv.org/abs/2603.16817"
          },
          {
            "title": "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights",
            "url": "https://arxiv.org/pdf/2603.16817"
          },
          {
            "title": "[2506.20978v1] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality",
            "url": "https://arxiv.org/abs/2506.20978v1"
          },
          {
            "title": "[2506.20978] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality",
            "url": "https://arxiv.org/abs/2506.20978"
          },
          {
            "title": "Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality",
            "url": "https://arxiv.org/html/2506.20978v1"
          }
        ]
      },
      "I found the paper you were looking for! Here are the key findings:\n\nThe paper \"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights\" (arXiv:2603.16817) was submitted on March 17, 2026 by Yi Chen, Daiwei Chen, Sukrut Madhav Chikodikar, Caitlyn Heqi Yin, and Ramya Korlakai Vinayak.\n\nThe research examines the robustness of conformal factuality approaches for RAG-based language models. The study finds that conformal factuality guarantees are not robust to distribution shifts and distractors, highlighting the limitation that calibration data must closely match deployment conditions.\n\nAdditionally, the research shows that conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, and lightweight entailment-based verifiers match or outperform LLM-based model confidence scorers while requiring over 100× fewer FLOPs.\n\nThe paper appears to expose critical limitations in applying conformal prediction methods to RAG systems when facing distribution shifts in real-world deployment scenarios."
    ],
    "durationSeconds": 6.801388320000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1bd075ed-6687-4b59-a9ea-ea597148e4fa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-30T07:51:49.889Z_

<details><summary>↩ Tool result · `toolu_01BaBfxXaUTZ2Sjd47GCSYtF`</summary>

```text
Web search results for query: "Lipschitz conformal prediction score function robust retrieval agreement 2025 2026"

Links: [{"title":"One Sample is Enough to Make Conformal Prediction Robust","url":"https://openreview.net/pdf?id=h5NsMrUK4g"},{"title":"[2506.05434] Efficient Robust Conformal Prediction via Lipschitz-Bounded Networks","url":"https://arxiv.org/abs/2506.05434"},{"title":"Efficient Robust Conformal Prediction via Lipschitz-Bounded Networks","url":"https://proceedings.mlr.press/v267/massena25a.html"},{"title":"Efficient Robust Conformal Prediction via Lipschitz-Bounded Networks - Archive ouverte HAL","url":"https://hal.science/hal-04936823v3"},{"title":"Efficient Robust Conformal Prediction via Lipschitz-Bounded Networks","url":"https://arxiv.org/pdf/2506.05434"},{"title":"Extending Prediction-Powered Inference through Conformal Prediction","url":"https://arxiv.org/html/2510.16166v1"},{"title":"Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/html/2502.14105v2"},{"title":"Efficient Robust Conformal Prediction via Lipschitz-Bounded Networks | OpenReview","url":"https://openreview.net/forum?id=w6Ds32QkQd"}]

Based on the search results, I found relevant research on Lipschitz-based conformal prediction. Here are the key findings:

## Efficient Robust Conformal Prediction via Lipschitz-Bounded Networks

Conformal Prediction (CP) has proven to be an effective post-hoc method for improving the trustworthiness of neural networks by providing prediction sets with finite-sample guarantees, though under adversarial attacks, classical conformal guarantees do not hold anymore.

A new method leverages Lipschitz-bounded networks to precisely and efficiently estimate robust CP sets, and when combined with a 1-Lipschitz robust network, the lip-rcp method outperforms state-of-the-art results in both the size of the robust CP sets and computational efficiency in medium and large-scale scenarios such as ImageNet.

This work was presented at the 42nd International Conference on Machine Learning (ICML 2025) in July 2025 in Vancouver, Canada.

## Related Research

There's also research on how data-space perturbations translate into score-space perturbations under smooth scoring functions, with conformal prediction under distribution shift derived by modeling shift directly over nonconformity scores to accommodate complex, potentially non-Lipschitz score functions such as deep neural networks.

Additionally, Lipschitz continuity of networks is used to bound the score function in robust conformal prediction approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aef21283-37a9-4f81-a4b1-4906c47db597",
  "isSidechain": false,
  "promptId": "bf7c039c-9c46-4596-82cc-fdd9084f898b",
  "type": "user",
  "uuid": "bc140001-d09e-49ee-af5c-c83c7f51064b",
  "toolUseResult": {
    "query": "Lipschitz conformal prediction score function robust retrieval agreement 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Tn6ZwD332KAwX43JDXJpa7",
        "content": [
          {
            "title": "One Sample is Enough to Make Conformal Prediction Robust",
            "url": "https://openreview.net/pdf?id=h5NsMrUK4g"
          },
          {
            "title": "[2506.05434] Efficient Robust Conformal Prediction via Lipschitz-Bounded Networks",
            "url": "https://arxiv.org/abs/2506.05434"
          },
          {
            "title": "Efficient Robust Conformal Prediction via Lipschitz-Bounded Networks",
            "url": "https://proceedings.mlr.press/v267/massena25a.html"
          },
          {
            "title": "Efficient Robust Conformal Prediction via Lipschitz-Bounded Networks - Archive ouverte HAL",
            "url": "https://hal.science/hal-04936823v3"
          },
          {
            "title": "Efficient Robust Conformal Prediction via Lipschitz-Bounded Networks",
            "url": "https://arxiv.org/pdf/2506.05434"
          },
          {
            "title": "Extending Prediction-Powered Inference through Conformal Prediction",
            "url": "https://arxiv.org/html/2510.16166v1"
          },
          {
            "title": "Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/html/2502.14105v2"
          },
          {
            "title": "Efficient Robust Conformal Prediction via Lipschitz-Bounded Networks | OpenReview",
            "url": "https://openreview.net/forum?id=w6Ds32QkQd"
          }
        ]
      },
      "Based on the search results, I found relevant research on Lipschitz-based conformal prediction. Here are the key findings:\n\n## Efficient Robust Conformal Prediction via Lipschitz-Bounded Networks\n\nConformal Prediction (CP) has proven to be an effective post-hoc method for improving the trustworthiness of neural networks by providing prediction sets with finite-sample guarantees, though under adversarial attacks, classical conformal guarantees do not hold anymore.\n\nA new method leverages Lipschitz-bounded networks to precisely and efficiently estimate robust CP sets, and when combined with a 1-Lipschitz robust network, the lip-rcp method outperforms state-of-the-art results in both the size of the robust CP sets and computational efficiency in medium and large-scale scenarios such as ImageNet.\n\nThis work was presented at the 42nd International Conference on Machine Learning (ICML 2025) in July 2025 in Vancouver, Canada.\n\n## Related Research\n\nThere's also research on how data-space perturbations translate into score-space perturbations under smooth scoring functions, with conformal prediction under distribution shift derived by modeling shift directly over nonconformity scores to accommodate complex, potentially non-Lipschitz score functions such as deep neural networks.\n\nAdditionally, Lipschitz continuity of networks is used to bound the score function in robust conformal prediction approaches."
    ],
    "durationSeconds": 6.543168960000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "aef21283-37a9-4f81-a4b1-4906c47db597",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 37 · 2026-05-30T07:51:49.894Z_

```json
{
  "parentUuid": "bc140001-d09e-49ee-af5c-c83c7f51064b",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "06596a93-6442-45eb-877f-4e063f46b1a5",
  "timestamp": "2026-05-30T07:51:49.894Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 38 · 2026-05-30T07:52:45.932Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive research to evaluate this proposal. Let me synthesize everything and write the evaluation.

Let me summarize my findings:

**Research landscape:**

1. **LP-CP (NeurIPS 2025)**: Real paper, provides framework for conformal prediction under Lévy-Prokhorov distribution shifts. Key idea: propagate LP ambiguity set through scoring function to get worst-case quantiles. The (ρ, ε) decomposition is real.

2. **Conformal prediction for RAG (benign)**:
   - TRAQ (NAACL 2024): end-to-end coverage guarantees for RAG
   - C-RAG (ICML 2024): certified generation risks
   - Conformal-RAG (SIGIR 2025): group-conditional coverage
   - All assume exchangeability / benign retrieval

3. **Certified RAG defenses**:
   - RobustRAG: isolate-then-aggregate approach achieving 38% certified robust accuracy on RealtimeQA (71% clean accuracy). The proposal claims SaTML 2026, but search results suggest ICML 2024 instead—there's some ambiguity here I need to clarify.
   - ReliabilityRAG (NeurIPS 2025): uses MIS-based defense
   - Neither offers formal abstention mechanisms

4. **Heuristic defenses**:
   - RAGDefender (ACSAC 2025): cosine similarity clustering
   - TrustRAG: K-means + cosine similarity

5. **Chen et al. (arXiv:2603.16817, Mar 2026)**: Directly shows that conformal factuality guarantees fail under RAG distribution shift—this is the key motivation for the proposal.

6. **Attacks**: PoisonedRAG, CorruptRAG, and many others—the field is very active.

7. My searches confirm the intersection of conformal prediction, RAG, and adversarial robustness appears completely unexplored—no existing work addresses all three together.

8. **Lipschitz-based robust CP**: There's a real paper on Lipschitz-bounded networks for robust conformal prediction at ICML 2025.

Now evaluating the proposal itself: it correctly identifies a genuine gap at the intersection of these three areas. The Lipschitz argument is elegant—LLM logits have uncontrollable Lipschitz constants due to deep composition, while normalized embedding cosine similarity has analytically bounded constants, which motivates why retrieval-level scores are necessary for propagating conformal guarantees. The proposal clearly differentiates itself from prior work like RobustRAG.

answer-only approaches, ReliabilityRAG, RAGDefender, and others that lack either adversarial robustness or formal guarantees. The experimental design is comprehensive with eight baselines, three datasets, three attack types, multiple embedding models and LLMs, plus extensive ablations and adaptive attack validation. The "Safe Silence" framing—guaranteeing either correct answers or explicit abstention—is well-motivated for safety-critical applications, and the compositional design where LP-RAG-Abstain acts as a retrieval gatekeeper to restore exchangeability is a clever architectural choice.

The main concerns are whether the Lipschitz constant is tight enough in practice to avoid overly conservative abstention rates, and whether the required knowledge of upper bounds on perturbation magnitude and embedding shift is realistic to obtain. There's also potential signal overlap with RAGDefender's use of pairwise cosine similarity, though the proposal addresses this distinction.

The worst-case guarantees might be overly conservative compared to empirical coverage, and the computational cost of pairwise similarity comparisons scales quadratically with retrieval set size. Most significantly, the compositional extension for end-to-end coverage is deferred to future work, which limits the immediate impact of the contribution.

Overall, this is a well-executed proposal with a genuine research gap and a novel theoretical insight about retrieval-level anchoring as a necessary condition for conformal prediction in RAG systems.

The experimental validation is thorough and the positioning against related work is honest. The main vulnerabilities are whether the Lipschitz bounds prove tight enough for practical use, whether reviewers perceive the cosine similarity signal as too derivative of RAGDefender, and whether the theoretical contribution feels like a straightforward application of existing conformal prediction techniques to a new domain. For AAAI 2026, the timing is favorable given the current interest in RAG security, the rigor of the theoretical framework, and the comprehensiveness of the experimental plan. The research problem is strong with clear motivation, though the method sits at medium-to-strong innovation since the core theoretical machinery and signal both draw from existing work.

The real novelty lies in connecting these pieces and using Lipschitz analysis to justify why retrieval-level scoring is necessary. Given the genuinely empty intersection with prior work, the clean theoretical insight, the exhaustive experimental design, practical applicability, and thorough positioning against all related work, I'd estimate the acceptance probability at 35-50%, with a median around 42%. This is a solid contribution with genuine merit, but the main risk is reviewers categorizing it as an application paper rather than a fundamental advance—though the Lipschitz analysis does push it beyond that. The fact that it addresses a gap Chen et al. explicitly identified in their March 2026 work strengthens the case considerably.

One thing I should verify: the proposal lists RobustRAG as "SaTML 2026," but my search results show ICML 2024 references. This could be a venue discrepancy that affects credibility if reviewers catch it, though it's relatively minor. The proposal itself is quite mature and well-executed.

I'm settling on an estimate of 35-48%, with a median around 40%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06596a93-6442-45eb-877f-4e063f46b1a5",
  "isSidechain": false,
  "requestId": "req_011CbYPZSCdMHnjKiDBNxHfX",
  "type": "assistant",
  "uuid": "9675c712-182d-4d4e-bf2b-d1c760614d6a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5gWR3xauudNwm241oSd1Q",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2490,
      "cache_read_input_tokens": 26232,
      "output_tokens": 7483,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2490,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7483,
          "cache_read_input_tokens": 26232,
          "cache_creation_input_tokens": 2490,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2490
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

_source line 39 · 2026-05-30T07:54:38.446Z_

Now I have sufficient research to provide a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:
- [LP-CP: Conformal Prediction under Lévy-Prokhorov Distribution Shifts](https://arxiv.org/abs/2502.14105) (NeurIPS 2025): 本 proposal 的核心理论工具。提供了 (ρ, ε) 分解和通过 scoring function 传播 LP ambiguity set 得到 worst-case quantile 的闭式表达。该框架未被应用于 RAG 场景，proposal 正是填补此空白。
- [TRAQ](https://aclanthology.org/2024.naacl-long.210/) (NAACL 2024): 首个为 RAG 提供端到端 conformal coverage 保证的方法。假设 exchangeability，不处理对抗性检索。
- [C-RAG](https://arxiv.org/abs/2401.13059) (ICML 2024): RAG 的 conformal 生成风险界。同样假设良性检索。
- [Conformal-RAG](https://arxiv.org/abs/2506.20978) (SIGIR 2025): 子声明级条件 coverage。良性设定。
- [RobustRAG](https://arxiv.org/abs/2405.15556) (published ~2024-2025): 首个可认证鲁棒 RAG 防御，isolate-then-aggregate 策略。RealtimeQA 上 71% clean / 38% certified robust accuracy。**只生成答案，不提供 abstention 机制**。注意：proposal 标注为 SaTML 2026，但搜索结果显示可能更早发表于 ICML 2024，需作者核实。
- [ReliabilityRAG](https://neurips.cc/virtual/2025/poster/119236) (NeurIPS 2025): 基于图论 MIS 的可靠性加权防御。同样只产生答案，无正式 abstention。
- [RAGDefender](https://github.com/SecAI-Lab/RAGDefender) (ACSAC 2025): 使用 cosine similarity clustering 进行启发式毒文档检测（0.18 ASR at 10× poisoning ratio）。**与本 proposal 使用相同的底层信号**，但无统计保证。
- [TrustRAG](https://arxiv.org/abs/2501.00879) (arXiv 2025): K-means + cosine similarity 的即插即用检测模块。启发式方法，无 coverage 保证。
- [Chen et al.: Is Conformal Factuality for RAG-based LLMs Robust?](https://arxiv.org/abs/2603.16817) (arXiv, Mar 2026): **直接诊断了 conformal factuality 保证在 RAG distribution shift 下失效的问题**，但未提出解决方案。这为本 proposal 提供了极好的问题动机。
- [RPS: Provably Reliable CP Sets under Data Poisoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4d21a4b33361c40c2142db9511c126-Paper-Conference.pdf) (ICLR 2025 Spotlight): 处理 calibration-time 数据投毒。与 RAG 的 test-time retrieval corruption 是根本不同的投毒模型。
- [Efficient Robust CP via Lipschitz-Bounded Networks](https://arxiv.org/abs/2506.05434) (ICML 2025): 通过控制网络 Lipschitz 常数来收紧 robust CP sets。与本 proposal 控制 score function 的 Lipschitz 常数互补。
- [PoisonedRAG](https://arxiv.org/abs/2402.07867) (USENIX Security 2025): 多文档注入攻击，97% ASR。
- [CorruptRAG](https://arxiv.org/abs/2504.03957) (arXiv 2025): 单文档注入实用攻击。
- [OPSA](https://arxiv.org/abs/2506.07804) (arXiv 2025): CP-targeted 攻击方法论。
- 调研总结: **{conformal prediction} ∩ {RAG} ∩ {adversarial robustness} 的交集经多轮搜索确认为空**。Chen et al. (2026) 明确诊断了问题但未给出解决方案。本 proposal 处于一个真实存在的、被明确识别但尚未填补的研究空白中，时效性极强。

【整体印象】:
作为审稿人，我的第一反应是 **lean accept / borderline accept**。这是一份成熟度极高的 proposal，具备以下令人印象深刻的特质：(1) 研究空白是真实的且经过严格验证；(2) 核心理论 insight（retrieval-level anchoring 是 LP-CP 在 RAG 中产生 non-vacuous 保证的必要条件，而非仅仅是方便选择）优雅且有深度；(3) 实验设计的完备程度远超同领域平均水平（8 个 baselines、adaptive attack、cross-attack validation、7 项 ablation + heatmap）；(4) 与所有相关工作的定位极其精准且诚实（特别是对 RAGDefender 信号重叠的坦诚讨论）。主要顾虑在于：(a) 核心方法是否会被视为 LP-CP 到新领域的"应用"而非根本性贡献；(b) Lipschitz bound 的实际紧致度是否足以产生非平凡的保证。

【核心贡献】:
1. **理论贡献**：证明 retrieval-agreement level 的 nonconformity score 是 LP-CP 在 RAG 中产生 non-vacuous 保证的**必要条件**（通过 Lipschitz 常数分析：answer-level scores 的 Lipschitz 常数随模型深度和上下文长度不可控增长，而 retrieval-level pairwise cosine similarity 的 Lipschitz 常数为 O(2/k)，解析可界）。
2. **方法贡献**：LP-RAG-Abstain — 首个为 RAG 在分布漂移（含对抗性投毒）下提供 distribution-free certified abstention 保证的框架。
3. **实践贡献**："Safe Silence" 保证 — "要么返回包含正确答案的集合，要么明确弃权"，填补了 RobustRAG/ReliabilityRAG 只能强制输出答案的空白。

这些贡献的领域价值**较高**。RAG 安全是 2025-2026 的热门方向，而 conformal prediction 社区也在积极探索 distribution shift 下的扩展。本工作恰好处于两个活跃社区的交叉点，且解决了一个被 Chen et al. (2026) 明确指出的开放问题。

【方法合理性】:
方法逻辑链条清晰且合理：
- LP-CP 提供了现成的 (ρ, ε) 框架 → 自然映射到 corpus poisoning 参数
- Lipschitz 分析排除了 answer-level scoring 的可行性 → 理论驱动的设计选择，非随意
- Pairwise cosine similarity 作为 score function → 已被 RAGDefender 实证验证有效，现在获得理论提升
- Abstention rule 通过 worst-case conformal quantile 实现 → 是 LP-CP 框架的自然推论

**潜在的更简单替代方案**：
1. 直接在 RAGDefender 的 cosine similarity 上设阈值做 abstention — 但这正是 proposal 要超越的（无统计保证）。
2. 用 answer-level confidence + 简单阈值 — 但无 certified coverage 保证，且 Chen et al. 已证明此类方法在分布漂移下失效。
3. 用 RPS (ICLR 2025) 的 partition-and-vote 方案 — 但 RPS 处理的是 calibration-time 投毒，不适用于 RAG 的 test-time 检索腐蚀。

因此，没有更简单的替代方案能同时实现 certified abstention + distribution-free guarantee + adversarial robustness。方法设计是必要复杂度下的最简方案。

【5 维度打分】:

1. 研究问题: 【强】 — 问题真实存在且被 Chen et al. (2026) 明确诊断。RAG 安全是 2025-2026 最热门的 AI 安全子方向之一（PoisonedRAG、CorruptRAG、RAGDefender、ReliabilityRAG 等密集发表）。现有 certified 防御（RobustRAG、ReliabilityRAG）只能强制输出答案，无法在高不确定性时弃权，在医疗/法律/金融等安全关键场景中有明显不足。Conformal prediction 在 RAG 中的应用（TRAQ、C-RAG）又假设良性检索。这个三方交叉的空白是真实的、重要的、及时的。

2. 方法与创新: 【中偏强】 — 核心理论工具（LP-CP）和底层信号（pairwise cosine similarity）均非原创，创新在于：(a) Lipschitz 必要性分析证明 retrieval-level anchoring 是唯一可行选择，这是一个非平凡的理论 insight；(b) 将 LP-CP 的 (ρ, ε) 分解与 corpus poisoning threat model 的自然对应关系识别出来。但审稿人可能认为这更偏向"应用 LP-CP 到新领域"而非"提出新的理论框架"。与 RAGDefender 的信号重叠（proposal 已诚实讨论）可能被部分审稿人视为 incremental。与 Efficient Robust CP via Lipschitz-Bounded Networks (ICML 2025) 的技术关联也需要更清晰地阐明差异。

3. 实验设计: 【强】 — 这是 proposal 最大的亮点之一。8 个 baselines 覆盖了所有相关类别（benign CP、certified defense、heuristic defense、naive baseline）；3 个数据集（NQ、HotpotQA、MS-MARCO）；多种攻击（PoisonedRAG black/white-box、CorruptRAG）；7 项 ablation + (ρ,ε) heatmap；**adaptive attack evaluation**（PGD-based，攻击者完全了解防御机制）；**cross-attack validation**（在一种攻击下校准，另一种攻击下测试）。特别是 adaptive attack 的设计（两种策略取最差）和 cross-attack validation 体现了安全论文的高标准。分层实验组织也很务实。这一实验设计达到了顶会安全论文的标准。

4. 可行性: 【强】 — (a) 无需训练任何模型，仅需 embedding 计算 + calibration；(b) 计算开销主要来自 embedding 和 LLM inference（与 baseline 一致）；(c) 理论部分（Lipschitz 分析、LP-CP 传播）已有成熟框架支撑；(d) 数据集和攻击实现均有开源代码；(e) 分层实验策略合理控制了 GPT-4o API 成本。唯一风险：如果 Lipschitz bound 过于松弛导致 certified coverage 与 empirical coverage 差距过大，方法可能需要 Lipschitz-regularized score design 的额外探索，但 proposal 已预见到这一点。

5. 写作与呈现: 【强】 — Proposal 结构极其清晰：问题 → insight → 为什么 insight 是必要的 → 机会 → landscape → approach → experiments。对相关工作的定位精准到每一篇论文的具体限制（如 RPS 的 calibration-time vs. test-time 投毒区别、RAGDefender 的信号 vs. 保证层面差异）。Threat model 的描述明确，参数的含义和类比（"analogous to RobustRAG's k′ ≤ k/5"）帮助读者快速理解。实验设计的目标量化且具体（"exceed RobustRAG's 38% certified robust accuracy"、"clean abstention rate <15%"）。这份 proposal 本身的写作水平接近可投稿论文。

【概率估计】: [33% - 48%] 中位 40%

【估计理由】:
上调因素：
- 真实且被验证的研究空白（Chen et al. 2026 明确诊断了问题但未解决），时效性极强
- 理论 insight（Lipschitz 必要性分析）将方法从"应用"提升为有深度的贡献
- 实验设计的完备程度（特别是 adaptive attack + cross-attack validation）在安全方向论文中属上乘
- "Safe Silence" 的实际意义在安全关键应用中有说服力
- 写作和 positioning 的成熟度降低了因表述不清被误判的风险
- 方法 LLM-agnostic 且无需训练，实用性强

下压因素：
- 核心可能被视为 LP-CP 的 straightforward application（虽然 Lipschitz 分析增加了深度，但理论贡献主要是"识别正确的 score function"而非"提出新的 CP 框架"）
- Pairwise cosine similarity 信号与 RAGDefender 共享，创新感打折扣
- Lipschitz bound 的实际紧致度是未验证的关键假设 — 如果 certified coverage 过于保守（如 clean abstention rate 远超 15%），实用价值将大打折扣，论文将变成"负面结果 + 分析"
- AAAI 审稿人多样性大，可能遇到不熟悉 LP-CP 框架的审稿人，导致理论贡献被低估
- 竞争时间窗口风险 — 该空白已被公开识别（Chen et al. 2026），可能有并发工作

综合来看，这是一篇 solid 的 borderline paper。如果 Lipschitz tightness 实验结果良好（certified vs. empirical gap 合理），且论文能有效论证理论贡献的非平凡性（不仅仅是 apply LP-CP），中稿概率偏向上界。

【主要风险】:
1. **Lipschitz bound 过松导致方法实际不可用**：如果 O(2/k) 的 worst-case bound 在实际数据上与 empirical Lipschitz constant 差距过大，worst-case conformal quantile 将过于保守，导致要么 prediction set trivially large，要么 clean abstention rate 过高（远超 15%目标），从而使 "certified guarantee" 沦为纯理论贡献。这是**最大的技术风险**。
2. **被审稿人判定为 "application paper" 缺乏足够 novelty**：尽管 Lipschitz 必要性分析增加了理论深度，但核心框架（LP-CP）和核心信号（pairwise cosine similarity）均来自已有工作，部分审稿人可能认为贡献不足以达到顶会标准，尤其在理论创新维度上。与 RAGDefender 的信号重叠加剧了这一风险。

【实施评估】:
  - 计算资源: 中等。主要开销在 embedding 计算（Qwen3-Embedding-8B 是最大模型）和 LLM inference（Llama-3.1-8B 本地 + GPT-4o API）。无模型训练。估计需要 2-4 张 A100 GPU 用于本地推理，GPT-4o 费用可通过分层实验策略控制。
  - 数据需求: 低。NQ、HotpotQA、MS-MARCO 均为公开标准数据集。PoisonedRAG 和 CorruptRAG 的攻击实现开源。
  - 人工介入: 低。理论推导 + 实验管线搭建，无需人工标注。
  - 训练需求: 无。方法完全基于 test-time calibration + inference，无需 fine-tuning 任何模型。
  - 新 Benchmark: 无需构建。使用现有标准数据集和攻击方法。
  - 预估周期: 8-12 周。理论推导（2-3 周）→ 核心实验管线搭建（2-3 周）→ 完整实验运行（3-4 周）→ 论文写作（2-3 周，可部分并行）。AAAI 2026 投稿 deadline 前可完成。
```

Sources:
- [LP-CP: Conformal Prediction under Lévy-Prokhorov Distribution Shifts](https://arxiv.org/abs/2502.14105)
- [TRAQ: Trustworthy Retrieval Augmented Question Answering](https://aclanthology.org/2024.naacl-long.210/)
- [RobustRAG: Certifiably Robust RAG against Retrieval Corruption](https://arxiv.org/abs/2405.15556)
- [ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search](https://neurips.cc/virtual/2025/poster/119236)
- [Chen et al.: Is Conformal Factuality for RAG-based LLMs Robust?](https://arxiv.org/abs/2603.16817)
- [RAGDefender: Rescuing the Unpoisoned](https://github.com/SecAI-Lab/RAGDefender)
- [TrustRAG: Enhancing Robustness and Trustworthiness in RAG](https://arxiv.org/abs/2501.00879)
- [CorruptRAG: Practical Poisoning Attacks against RAG](https://arxiv.org/abs/2504.03957)
- [Efficient Robust CP via Lipschitz-Bounded Networks](https://arxiv.org/abs/2506.05434)
- [OPSA: Enhancing Adversarial Robustness with Conformal Prediction](https://arxiv.org/abs/2506.07804)
- [RPS: Provably Reliable CP Sets under Data Poisoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4d21a4b33361c40c2142db9511c126-Paper-Conference.pdf)
- [RAG Poisoning: Threats and Defenses (Emergent Mind)](https://www.emergentmind.com/topics/retrieval-augmented-generation-rag-poisoning)
- [Certified Defenses for RAG Systems (Emergent Mind)](https://www.emergentmind.com/topics/certified-defenses-for-rag-systems)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9675c712-182d-4d4e-bf2b-d1c760614d6a",
  "isSidechain": false,
  "requestId": "req_011CbYPZSCdMHnjKiDBNxHfX",
  "type": "assistant",
  "uuid": "aa021227-3347-4d05-ba12-9ecd1032fd6d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5gWR3xauudNwm241oSd1Q",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2490,
      "cache_read_input_tokens": 26232,
      "output_tokens": 7483,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2490,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7483,
          "cache_read_input_tokens": 26232,
          "cache_creation_input_tokens": 2490,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2490
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

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Conformal Abstention for RAG under LP-Bounded Retrieval Shifts  ## Core Problem  How can a RAG system provide di…",
  "leafUuid": "aa021227-3347-4d05-ba12-9ecd1032fd6d",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Certified RAG abstention under retrieval poisoning",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Conformal Abstention for RAG under LP-Bounded Retrieval Shifts  ## Core Problem  How can a RAG system provide di…",
  "leafUuid": "aa021227-3347-4d05-ba12-9ecd1032fd6d",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Certified RAG abstention under retrieval poisoning",
  "sessionId": "aa5893a8-fa2a-43db-928c-9a8aa9b27f5b"
}
```

---
