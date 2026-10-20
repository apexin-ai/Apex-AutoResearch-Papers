# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Conformal Abstention for RAG unde

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/e33840bd-e0ef-41a3-8869-05f690526764.jsonl`
- **Structured JSON:** [`3b7b85a801ee12430ca7.json`](../../sessions/3b/3b7b85a801ee12430ca7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T07:50:42.349Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T07:50:42.349Z",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Conformal Abstention for RAG under LP-Bounded Retrieval Shifts\n\n## Core Problem\n\nHow can a RAG system provide distribution-free, certified abstention guarantees on answer correctness when the retrieval corpus undergoes bounded distributional shifts — including adversarial corpus poisoning, organic corpus drift, and domain mismatch — where standard conformal prediction (TRAQ, C-RAG) breaks due to exchangeability violation, and existing certified defenses (RobustRAG, ReliabilityRAG) can only generate answers but cannot formally decide when to abstain?\n\n## Core Insight\n\nWe show that anchoring the nonconformity score at the retrieval-agreement level — rather than the answer-confidence level used by prior CP-for-RAG methods — is a necessary condition for LP-CP's score propagation theorem to yield non-vacuous guarantees in RAG.\n\n**Why retrieval-level anchoring is necessary, not merely convenient.** LP-CP's worst-case quantile shifts scale as L·ε, where L is the score function's Lipschitz constant and ε is the local perturbation bound. For answer-level scores (LLM output logits/probabilities), the composition of embedding lookup → attention layers → softmax produces Lipschitz constants that grow uncontrollably with context length and model depth, rendering LP-CP propagation vacuous (worst-case quantile collapses to trivial bounds). For retrieval-level pairwise cosine similarity on normalized embeddings, the Lipschitz constant is analytically bounded (O(2/k) for mean pairwise agreement over k passages w.r.t. single-document replacement), independent of LLM architecture. This analysis establishes that retrieval-level scoring is the natural — and effectively the only viable — anchor point for LP-CP in RAG systems.\n\nThis design simultaneously: (1) directly probes the attack surface (poisoning acts on retrieval, not generation), (2) makes the method LLM-agnostic and composable with any downstream generator, and (3) enables the first certified abstention guarantee for RAG under distributional shifts.\n\n## Research Opportunity\n\nThe intersection of {conformal prediction} ∩ {RAG} ∩ {adversarial robustness} is empty as of May 2026, verified across two RAG security surveys (arXiv:2603.21654, arXiv:2604.08304), the TACL CP-for-NLP survey, and 15+ targeted searches. Chen et al. (arXiv:2603.16817, Mar 2026) explicitly diagnosed that conformal factuality guarantees break under RAG distribution shift — including but not limited to adversarial shift — but proposed no solution. The LP-CP framework (NeurIPS 2025, arXiv:2502.14105) provides the exact (ρ, ε) decomposition that maps onto corpus poisoning parameters. No concurrent work addresses this gap.\n\n## Research Landscape\n\n**CP for benign RAG.** TRAQ (NAACL 2024) provides end-to-end coverage via calibrated retrieval and answer sets. C-RAG (ICML 2024) certifies conformal generation risk bounds. Conformal-RAG (SIGIR 2025) offers group-conditional coverage for sub-claims. Principled Context Engineering for RAG (arXiv:2511.17908) uses CP for context filtering, reducing retained context by 2–3×. PASC (arXiv:2605.18812) addresses pipeline-aware joint coverage for multi-stage NLP systems including RAG pipelines. None handle adversarial or shifted retrieval.\n\n**Certified RAG defenses (answer-only, no abstention).** RobustRAG (SaTML 2026) achieves 38% certified robust accuracy on RealtimeQA (71% clean) via isolate-then-aggregate. ReliabilityRAG (NeurIPS 2025) uses graph-theoretic MIS with reliability-weighted documents under k′ ≤ k/5 poisoning budget. Both must produce an answer even under high uncertainty; neither offers formal abstention.\n\n**Heuristic RAG defenses.** RAGDefender (ACSAC 2025) achieves 0.18 ASR at 10× poisoning ratio via cosine-similarity clustering, finding poisoned docs cluster tightly (0.976 vs 0.309 cosine similarity). TrustRAG (arXiv:2501.00879) uses K-means clustering + cosine similarity for plug-and-play detection. RAGPart & RAGMask (arXiv:2512.24268) use document partitioning and token masking at retrieval stage across four retrievers. These rely on heuristic thresholds with no coverage guarantees or formal abstention.\n\n**Relationship to RAGDefender's signal.** LP-RAG-Abstain uses the same underlying signal as RAGDefender — pairwise cosine similarity among retrieved passages. The contribution operates at a different level: (1) signal level: shared (pairwise cosine similarity) — we openly acknowledge this; (2) decision rule level: RAGDefender uses tuned thresholds on cluster membership, LP-RAG-Abstain uses LP-CP worst-case quantiles — methodological difference; (3) guarantee level: RAGDefender provides no finite-sample guarantee and its threshold has no parametric response to attack budget, LP-RAG-Abstain provides distribution-free coverage guarantee parameterized by (ρ, ε) — fundamental difference. The core question this paper answers: what theoretical framework converts the empirical observation that pairwise similarity distinguishes poisoned retrieval into a formal guarantee?\n\n**Poisoning-robust CP (non-RAG).** RPS (ICLR 2025 Spotlight) uses partition-and-vote for calibration-time data poisoning — a fundamentally different poisoning model than test-time retrieval corruption. In calibration poisoning, the attacker corrupts the static calibration set; in RAG poisoning, corruption occurs dynamically at test-time through retrieval. RPS's guarantees do not transfer to the RAG setting. LP-CP (NeurIPS 2025, arXiv:2502.14105) provides closed-form worst-case quantiles under LP distribution shifts but was not applied to RAG.\n\n**Conformal abstention (non-adversarial).** Learning Conformal Abstention Policies (arXiv:2502.06884) integrates RL with CP for adaptive abstention in LLMs/VLMs but relies on training and does not handle adversarial settings. Selective Conformal Risk Control (arXiv:2512.12844) integrates CP with selective classification but not in RAG or adversarial contexts.\n\n**Robust CP for LLMs.** Beyond Surface Statistics (arXiv:2604.16217) uses LLM internal representations for robust CP but does not analyze Lipschitz properties or address adversarial RAG. Efficient Robust CP via Lipschitz-Bounded Networks (arXiv:2506.05434) controls model Lipschitz constants to tighten robust CP sets — complementary to our approach of controlling the score function's Lipschitz constant.\n\n**Attack landscape.** PoisonedRAG (USENIX Security 2025) achieves 97% ASR via multi-document injection with distinct black-box (LLM-generated) and white-box (gradient-optimized) variants. CorruptRAG (arXiv:2504.03957) achieves high ASR with single-document injection (ρ→0). Benchmarking Poisoning Attacks against RAG (arXiv:2505.18543) provides a unified framework across 5 datasets, 13 attacks, and 7 defenses.\n\n## Proposed Approach\n\n**LP-RAG-Abstain** provides distribution-free certified abstention for RAG under LP-bounded retrieval shifts, with adversarial corpus poisoning as the primary and most challenging instantiation.\n\n**Threat model.** Attacker injects poisoned documents into the corpus. Defense assumes upper bounds (ρ₀, ε₀) on: ρ = fraction of poisoned documents in top-k retrieval, ε = maximum embedding perturbation per poisoned document. These are defense input parameters (analogous to RobustRAG's k′ ≤ k/5), not quantities to estimate. Guarantees are conditional: valid whenever the actual attack falls within (ρ₀, ε₀). The same (ρ, ε) parameterization naturally covers non-adversarial retrieval shifts (organic corpus drift, domain mismatch), making the framework broadly applicable.\n\n**Score design.** Define retrieval-agreement nonconformity score s(q) from pairwise cosine similarities among top-k retrieved passages for query q. For normalized embeddings on the unit sphere, the mean pairwise cosine similarity score has Lipschitz constant O(2/k) w.r.t. single-document replacement, enabling LP-CP's propagation theorem to yield closed-form worst-case quantiles that are non-vacuous for practical (ρ, ε) ranges.\n\n**Lipschitz tightness.** The practical viability depends on the Lipschitz constant being small enough. We will: (1) derive the analytic Lipschitz upper bound, (2) empirically estimate the constant on real embedding data, (3) report the gap between certified and empirical coverage to quantify conservatism, and (4) if needed, explore Lipschitz-regularized score designs (cf. arXiv:2506.05434).\n\n**Abstention rule.** Map (ρ₀, ε₀) to LP ambiguity set. Compute worst-case conformal quantile via LP-CP's closed-form expression. Abstain when prediction set is empty under worst-case quantile. Guarantee: P(correct ∈ set ∨ abstain) ≥ 1−α.\n\n**Adversary-budget monotonicity.** Certified coverage improves as attacker budget (ρ, ε) decreases, with the tightest guarantees at the most practical attack regime — single/few-document poisoning (CorruptRAG, arXiv:2504.03957). This contrasts with isolate-then-aggregate methods (RobustRAG) whose partitioning overhead is constant regardless of attack strength.\n\n**\"Safe Silence\" guarantee.** Unlike answer-only defenses that must produce output under high uncertainty, LP-RAG-Abstain formally guarantees: \"either I return a set containing the correct answer, or I explicitly abstain.\" In safety-critical RAG (medical, legal, financial), confidently wrong answers are far more harmful than acknowledged uncertainty. This addresses the \"robustness + usefulness\" desiderata of Chen et al. (arXiv:2603.16817).\n\n**Compositional extension.** LP-RAG-Abstain as a retrieval-stage gatekeeper can compose with downstream answer-level CP methods (TRAQ, C-RAG): if LP-RAG-Abstain does not abstain, retrieval is certified within LP tolerance, approximately restoring exchangeability so downstream CP guarantees re-activate. Via pipeline-aware CP techniques (PASC, arXiv:2605.18812), this enables end-to-end joint coverage guarantees — a direction we discuss as future work.\n\n## Experimental Design\n\n**Datasets.** NQ, HotpotQA, MS-MARCO.\n\n**Attacks.** PoisonedRAG black-box + white-box (USENIX Security 2025), CorruptRAG single-document (arXiv:2504.03957). White-box variant directly optimizes embeddings, providing the strongest test of ε-bounded guarantees.\n\n**Embedding models.** Qwen3-Embedding-8B (primary), BGE-large, Contriever. Report empirical Lipschitz constant for each.\n\n**Generator LLMs.** Llama-3.1-8B (open-source), GPT-4o (closed-source).\n\n**Baselines.**\n- No-defense vanilla RAG\n- TRAQ (NAACL 2024): CP without adversarial awareness\n- C-RAG (ICML 2024): conformal risk bounds without adversarial awareness\n- RobustRAG (SaTML 2026): certified answer-only defense\n- ReliabilityRAG (NeurIPS 2025): certified answer-only defense\n- RAGDefender (ACSAC 2025): heuristic detection (same signal, no guarantee)\n- TrustRAG (arXiv:2501.00879): heuristic detection\n- Naive selective prediction: LLM confidence threshold abstention\n\n**Evaluation metrics.**\n- Coverage (poisoned): P(correct ∈ set ∨ abstain) — core guarantee\n- Coverage (clean): P(correct ∈ set) without poisoning — should ≥ 1−α\n- Abstention rate (poisoned vs. clean)\n- Certified robust accuracy on non-abstained queries (EM and F1)\n- Overall ASR (abstain counted as attack failure) and conditional ASR (non-abstained only)\n- Prediction set size (mean/median)\n- Accuracy-abstention tradeoff AUC (varying α)\n- Wall-clock inference time and LLM call count per query\n\n**Ablation studies.**\n1. ρ sensitivity: fix ε, vary ρ ∈ {0, 0.05, 0.1, 0.2, 0.4}\n2. ε sensitivity: fix ρ, vary ε\n3. Score function: pairwise cosine agreement (proposed) vs. average retrieval score vs. answer entropy\n4. k sensitivity: k ∈ {5, 10, 20, 50}\n5. α sweep: α ∈ {0.01, 0.05, 0.10, 0.20}\n6. Calibration set size: {100, 300, 500, 1000, 2000}\n7. LP-CP vs. Bonferroni correction\n\n**(ρ, ε) heatmap.** Jointly vary (ρ, ε) and plot certified accuracy and abstention rate as 2D heatmaps.\n\n**Adaptive attack evaluation.** Adversary with full knowledge of the defense. Two PGD-based attack strategies within ε-ball: (a) maximize pairwise cosine agreement score (poisoned docs mimic clean retrieval pattern), (b) minimize it (force vacuous prediction sets). Report whichever is worse for the defense. Constraints: ‖e_poison − e_original‖₂ ≤ ε, ρk poisoned docs in top-k. Reference design: OPSA (arXiv:2506.07804) for CP-targeted attack methodology.\n\n**Cross-attack validation.** On NQ: calibrate (ρ₀, ε₀) under PoisonedRAG assumptions, test under CorruptRAG, and vice versa. Verify coverage guarantee holds across attack types (theoretically guaranteed by (ρ, ε) parameterization; experimentally validated).\n\n**Experiment organization.** Layered strategy: (1) Core: primary embedding model + Llama-3.1-8B + all datasets + all attacks + all baselines; (2) Generalization: NQ with all embedding model × LLM combinations; (3) Ablation: main configuration only; (4) GPT-4o limited to core and generalization experiments.\n\n**Targets.** Exceed RobustRAG's 38% certified robust accuracy on comparable datasets; maintain >90% clean coverage; achieve <15% clean abstention rate; overall ASR < 10% under standard PoisonedRAG attack.\n\n## Key References\n\n- TRAQ (NAACL 2024)\n- C-RAG: Certified Generation Risks for RAG (ICML 2024)\n- Conformal-RAG / Response Quality Assessment (SIGIR 2025)\n- RobustRAG: Certifiably Robust RAG against Retrieval Corruption (SaTML 2026)\n- ReliabilityRAG (NeurIPS 2025)\n- PoisonedRAG (USENIX Security 2025)\n- CorruptRAG: Practical Poisoning Attacks against RAG (arXiv:2504.03957)\n- LP-CP: Conformal Prediction under Lévy-Prokhorov Distribution Shifts (NeurIPS 2025, arXiv:2502.14105)\n- RPS: Provably Reliable CP Sets under Data Poisoning (ICLR 2025 Spotlight)\n- RAGDefender: Rescuing the Unpoisoned (ACSAC 2025)\n- TrustRAG (arXiv:2501.00879)\n- RAGPart & RAGMask (arXiv:2512.24268)\n- Chen et al.: Is Conformal Factuality for RAG-based LLMs Robust? (arXiv:2603.16817, 2026)\n- RAG security surveys (arXiv:2603.21654, arXiv:2604.08304)\n- TACL CP-for-NLP survey\n- Principled Context Engineering for RAG (arXiv:2511.17908)\n- Learning Conformal Abstention Policies (arXiv:2502.06884)\n- Selective Conformal Risk Control (arXiv:2512.12844)\n- Benchmarking Poisoning Attacks against RAG (arXiv:2505.18543)\n- PASC: Pipeline-Aware Conformal Prediction (arXiv:2605.18812)\n- OPSA: Enhancing Adversarial Robustness with CP (arXiv:2506.07804)\n- Efficient Robust CP via Lipschitz-Bounded Networks (arXiv:2506.05434)\n- Beyond Surface Statistics: Robust CP for LLMs (arXiv:2604.16217)"
}
```

---

### Runtime record

_source line 2 · 2026-05-30T07:50:42.355Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T07:50:42.355Z",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764"
}
```

---

## Round 1

35 recorded events

### User

_source line 3 · 2026-05-30T07:50:42.379Z_

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
  "promptId": "121afd3a-f968-4ef5-8969-c92e4fdf9808",
  "type": "user",
  "uuid": "5893ea1b-2066-46fa-810f-5f4a40548c53",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T07:50:42.377Z_

```json
{
  "parentUuid": "5893ea1b-2066-46fa-810f-5f4a40548c53",
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
  "uuid": "552d2463-ecc1-4cb0-b316-05a12dec3170",
  "timestamp": "2026-05-30T07:50:42.377Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T07:50:42.377Z_

```json
{
  "parentUuid": "552d2463-ecc1-4cb0-b316-05a12dec3170",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4828a596-744a-4dbb-806b-6466976bbec3",
  "timestamp": "2026-05-30T07:50:42.377Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
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
  "leafUuid": "4828a596-744a-4dbb-806b-6466976bbec3",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal abstention for RAG under adversarial retrieval shifts",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764"
}
```

---

### Assistant

_source line 8 · 2026-05-30T07:50:49.126Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for AAAI 2026 submission. I need to first conduct thorough literature research, then provide a comprehensive evaluation following the specified format.

Let me start by searching for the key topics in this proposal:
1. Conformal prediction for RAG systems
2. LP-CP (Lévy-Prokhorov Conformal Prediction)
3. RAG adversarial robustness / corpus poisoning defenses
4. Certified abstention in NLP/RAG

Let me do the web searches first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4828a596-744a-4dbb-806b-6466976bbec3",
  "isSidechain": false,
  "requestId": "req_011CbYPUTimCtf64jirtkp26",
  "type": "assistant",
  "uuid": "3ac66b4d-2e53-4361-8785-774084b0883d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4ygxiq5JpKswgukkrYrpT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8219,
      "cache_read_input_tokens": 11014,
      "output_tokens": 266,
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
          "output_tokens": 266,
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

### Assistant

_source line 9 · 2026-05-30T07:50:50.380Z_

I'll start by conducting thorough literature research on the key topics of this proposal before making any evaluation. Let me search for the current state of conformal prediction for RAG, adversarial RAG defenses, and LP-CP.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ac66b4d-2e53-4361-8785-774084b0883d",
  "isSidechain": false,
  "requestId": "req_011CbYPUTimCtf64jirtkp26",
  "type": "assistant",
  "uuid": "5e0fa474-3dbe-4198-b67f-5604ddd44785",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4ygxiq5JpKswgukkrYrpT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8219,
      "cache_read_input_tokens": 11014,
      "output_tokens": 266,
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
          "output_tokens": 266,
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

_source line 10 · 2026-05-30T07:50:50.887Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EX8DiQMZ2M4y1dC1AWxob8`</summary>

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
  "parentUuid": "5e0fa474-3dbe-4198-b67f-5604ddd44785",
  "isSidechain": false,
  "requestId": "req_011CbYPUTimCtf64jirtkp26",
  "type": "assistant",
  "uuid": "c2c4bb00-a596-40c7-95e2-5226ce5c155f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4ygxiq5JpKswgukkrYrpT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8219,
      "cache_read_input_tokens": 11014,
      "output_tokens": 266,
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
          "output_tokens": 266,
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

_source line 11 · 2026-05-30T07:50:50.917Z_

<details><summary>↩ Tool result · `toolu_01EX8DiQMZ2M4y1dC1AWxob8`</summary>

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
  "parentUuid": "c2c4bb00-a596-40c7-95e2-5226ce5c155f",
  "isSidechain": false,
  "promptId": "121afd3a-f968-4ef5-8969-c92e4fdf9808",
  "type": "user",
  "uuid": "74300449-fec2-4013-aa2c-993660f53681",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "c2c4bb00-a596-40c7-95e2-5226ce5c155f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-30T07:50:53.784Z_

Now let me conduct the required literature searches. I'll run multiple searches in parallel to cover the key areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "74300449-fec2-4013-aa2c-993660f53681",
  "isSidechain": false,
  "requestId": "req_011CbYPV6CzC2RFvndcBh8dx",
  "type": "assistant",
  "uuid": "755c60ed-34be-4a8b-8c5d-15a3919d73b7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bjg6jKCaM5KzAAxUJ8bJux",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 794,
      "cache_read_input_tokens": 19233,
      "output_tokens": 95,
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
          "input_tokens": 3,
          "output_tokens": 95,
          "cache_read_input_tokens": 19233,
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

### Tool call

_source line 13 · 2026-05-30T07:50:53.943Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F5pq7RDrQvcR1ZJaT2v1oH`</summary>

```json
{
  "query": "conformal prediction RAG retrieval-augmented generation 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "755c60ed-34be-4a8b-8c5d-15a3919d73b7",
  "isSidechain": false,
  "requestId": "req_011CbYPV6CzC2RFvndcBh8dx",
  "type": "assistant",
  "uuid": "4805f59b-a7d8-4901-9b71-3eb1db7911c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bjg6jKCaM5KzAAxUJ8bJux",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 794,
      "cache_read_input_tokens": 19233,
      "output_tokens": 95,
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
          "input_tokens": 3,
          "output_tokens": 95,
          "cache_read_input_tokens": 19233,
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

### Tool result

_source line 14 · 2026-05-30T07:51:00.841Z_

<details><summary>↩ Tool result · `toolu_01F5pq7RDrQvcR1ZJaT2v1oH`</summary>

```text
Web search results for query: "conformal prediction RAG retrieval-augmented generation 2024 2025 2026"

Links: [{"title":"GitHub - Arstanley/Awesome-Trustworthy-RAG · GitHub","url":"https://github.com/Arstanley/Awesome-Trustworthy-RAG"},{"title":"Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/html/2506.20978"},{"title":"RAG is DEAD!. Retrieval-Augmented Generation ruled… | by Reliable Data Engineering | Medium","url":"https://medium.com/@reliabledataengineering/rag-is-dead-and-why-thats-the-best-news-you-ll-hear-all-year-0f3de8c44604"},{"title":"Towards Dependable Retrieval-Augmented Generation Using Factual Confidence Prediction","url":"https://arxiv.org/html/2605.05244v1"},{"title":"Retrieval-Augmented Generation (RAG)","url":"https://www.emergentmind.com/topics/retrieval-augmented-generation-rag-b2f527f9-ed5b-4d55-bf40-48c4e873c676"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal   Prediction","url":"https://arxiv.org/pdf/2307.04642"}]

Based on the web search results, here's what I found about conformal prediction and retrieval-augmented generation (RAG) research in 2024-2026:

## Recent Developments

Conformal prediction provides a stronger theoretical foundation for ensuring soundness of evaluations through statistical guarantees in RAG systems. Conformal prediction (CP) is a distribution-free uncertainty quantification method based on the assumption of the exchangeability of data.

## Key Research Works

Several notable approaches have emerged combining these techniques:

1. **TRAQ Framework**: TRAQ leverages conformal prediction to ensure that the retrieved set includes the relevant passage with a high probability and that the LLM set contains a semantically correct answer with a high probability.

2. **Conformal-RAG (2025)**: Conformal-RAG incorporates similarity information from the RAG mechanism and uses automatic annotation to provide ground truth on sub-claim factuality.

3. **Conformal Answer Set Prediction (2024)**: Conformalized Answer Set Prediction for Knowledge Graph Embedding was published in August 2024.

4. **Broader RAG Trustworthiness**: Recent work presents a comprehensive workflow to quantify factual confidence in RAG systems with separate metrics for the stages of context retrieval and LLM-based answer generation.

These developments reflect growing focus on making RAG systems more trustworthy and reliable through uncertainty quantification methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4805f59b-a7d8-4901-9b71-3eb1db7911c7",
  "isSidechain": false,
  "promptId": "121afd3a-f968-4ef5-8969-c92e4fdf9808",
  "type": "user",
  "uuid": "8fc6a213-6c69-49db-a9b8-f4ff08c6a769",
  "toolUseResult": {
    "query": "conformal prediction RAG retrieval-augmented generation 2024 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Hi9sERrLNJtJTX8UXvU1Yf",
        "content": [
          {
            "title": "GitHub - Arstanley/Awesome-Trustworthy-RAG · GitHub",
            "url": "https://github.com/Arstanley/Awesome-Trustworthy-RAG"
          },
          {
            "title": "Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality",
            "url": "https://arxiv.org/html/2506.20978"
          },
          {
            "title": "RAG is DEAD!. Retrieval-Augmented Generation ruled… | by Reliable Data Engineering | Medium",
            "url": "https://medium.com/@reliabledataengineering/rag-is-dead-and-why-thats-the-best-news-you-ll-hear-all-year-0f3de8c44604"
          },
          {
            "title": "Towards Dependable Retrieval-Augmented Generation Using Factual Confidence Prediction",
            "url": "https://arxiv.org/html/2605.05244v1"
          },
          {
            "title": "Retrieval-Augmented Generation (RAG)",
            "url": "https://www.emergentmind.com/topics/retrieval-augmented-generation-rag-b2f527f9-ed5b-4d55-bf40-48c4e873c676"
          },
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal   Prediction",
            "url": "https://arxiv.org/pdf/2307.04642"
          }
        ]
      },
      "Based on the web search results, here's what I found about conformal prediction and retrieval-augmented generation (RAG) research in 2024-2026:\n\n## Recent Developments\n\nConformal prediction provides a stronger theoretical foundation for ensuring soundness of evaluations through statistical guarantees in RAG systems. Conformal prediction (CP) is a distribution-free uncertainty quantification method based on the assumption of the exchangeability of data.\n\n## Key Research Works\n\nSeveral notable approaches have emerged combining these techniques:\n\n1. **TRAQ Framework**: TRAQ leverages conformal prediction to ensure that the retrieved set includes the relevant passage with a high probability and that the LLM set contains a semantically correct answer with a high probability.\n\n2. **Conformal-RAG (2025)**: Conformal-RAG incorporates similarity information from the RAG mechanism and uses automatic annotation to provide ground truth on sub-claim factuality.\n\n3. **Conformal Answer Set Prediction (2024)**: Conformalized Answer Set Prediction for Knowledge Graph Embedding was published in August 2024.\n\n4. **Broader RAG Trustworthiness**: Recent work presents a comprehensive workflow to quantify factual confidence in RAG systems with separate metrics for the stages of context retrieval and LLM-based answer generation.\n\nThese developments reflect growing focus on making RAG systems more trustworthy and reliable through uncertainty quantification methods."
    ],
    "durationSeconds": 6.891471726,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4805f59b-a7d8-4901-9b71-3eb1db7911c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-30T07:51:03.382Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DgYNtP8ULXDct9H8wX1xRR`</summary>

```json
{
  "query": "LP-CP Lévy-Prokhorov conformal prediction distribution shift NeurIPS 2025 arXiv 2502.14105"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fc6a213-6c69-49db-a9b8-f4ff08c6a769",
  "isSidechain": false,
  "requestId": "req_011CbYPVpRz6WcnZ4gFekTtr",
  "type": "assistant",
  "uuid": "0f76a402-0d6a-434e-bc6b-00b3ad120939",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Ga6RjLG4p1HgxUEtJjpiQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 20027,
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
          "cache_read_input_tokens": 20027,
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

_source line 16 · 2026-05-30T07:51:09.001Z_

<details><summary>↩ Tool result · `toolu_01DgYNtP8ULXDct9H8wX1xRR`</summary>

```text
Web search results for query: "LP-CP Lévy-Prokhorov conformal prediction distribution shift NeurIPS 2025 arXiv 2502.14105"

Links: [{"title":"[2502.14105] Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/abs/2502.14105"},{"title":"Conformal Prediction under Lévy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations | OpenReview","url":"https://openreview.net/forum?id=1ULQvdbZ3X"},{"title":"NeurIPS Poster Conformal Prediction under Lévy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/120230"},{"title":"Conformal Prediction under Lévy-Prokhorov Distribution ...","url":"https://openreview.net/pdf/860efa6f37cc6b64df19821bba75d83edb3b9603.pdf"},{"title":"(PDF) Conformal Prediction under L\\'evy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://www.researchgate.net/publication/389176501_Conformal_Prediction_under_L'evy-Prokhorov_Distribution_Shifts_Robustness_to_Local_and_Global_Perturbations"},{"title":"Conformal Prediction under Lévy-Prokhorov Distribution ...","url":"https://arxiv.org/pdf/2502.14105"},{"title":"Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/html/2502.14105v2"}]

I found the paper! Here are the key details about arXiv 2502.14105:

## Paper Summary

Conformal prediction provides a powerful framework for constructing prediction intervals with finite-sample guarantees, yet its robustness under distribution shifts remains a significant challenge. The paper addresses this limitation by modeling distribution shifts using Levy-Prokhorov (LP) ambiguity sets, which capture both local and global perturbations.

## Main Contributions

The authors provide a self-contained overview of LP ambiguity sets and their connections to popular metrics such as Wasserstein and Total Variation. 

The link between conformal prediction and LP ambiguity sets is a natural one: by propagating the LP ambiguity set through the scoring function, they reduce complex high-dimensional distribution shifts to manageable one-dimensional distribution shifts, enabling exact quantification of worst-case quantiles and coverage.

## Publication Details

- **arXiv ID:** 2502.14105
- **Submitted:** February 19, 2025 (v1), last revised May 19, 2025 (v2)
- **Venue:** NeurIPS 2025 poster
- **Authors:** Liviu Aolaritei, Zheyu Oliver Wang, Julie Zhu, Michael I. Jordan, and Youssef Marzouk


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f76a402-0d6a-434e-bc6b-00b3ad120939",
  "isSidechain": false,
  "promptId": "121afd3a-f968-4ef5-8969-c92e4fdf9808",
  "type": "user",
  "uuid": "db75d074-05a3-43a6-a5bd-1e80d4144236",
  "toolUseResult": {
    "query": "LP-CP Lévy-Prokhorov conformal prediction distribution shift NeurIPS 2025 arXiv 2502.14105",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Sb13xaMSHE84XfuYFMTuNT",
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
            "title": "NeurIPS Poster Conformal Prediction under Lévy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://neurips.cc/virtual/2025/loc/san-diego/poster/120230"
          },
          {
            "title": "Conformal Prediction under Lévy-Prokhorov Distribution ...",
            "url": "https://openreview.net/pdf/860efa6f37cc6b64df19821bba75d83edb3b9603.pdf"
          },
          {
            "title": "(PDF) Conformal Prediction under L\\'evy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://www.researchgate.net/publication/389176501_Conformal_Prediction_under_L'evy-Prokhorov_Distribution_Shifts_Robustness_to_Local_and_Global_Perturbations"
          },
          {
            "title": "Conformal Prediction under Lévy-Prokhorov Distribution ...",
            "url": "https://arxiv.org/pdf/2502.14105"
          },
          {
            "title": "Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/html/2502.14105v2"
          }
        ]
      },
      "I found the paper! Here are the key details about arXiv 2502.14105:\n\n## Paper Summary\n\nConformal prediction provides a powerful framework for constructing prediction intervals with finite-sample guarantees, yet its robustness under distribution shifts remains a significant challenge. The paper addresses this limitation by modeling distribution shifts using Levy-Prokhorov (LP) ambiguity sets, which capture both local and global perturbations.\n\n## Main Contributions\n\nThe authors provide a self-contained overview of LP ambiguity sets and their connections to popular metrics such as Wasserstein and Total Variation. \n\nThe link between conformal prediction and LP ambiguity sets is a natural one: by propagating the LP ambiguity set through the scoring function, they reduce complex high-dimensional distribution shifts to manageable one-dimensional distribution shifts, enabling exact quantification of worst-case quantiles and coverage.\n\n## Publication Details\n\n- **arXiv ID:** 2502.14105\n- **Submitted:** February 19, 2025 (v1), last revised May 19, 2025 (v2)\n- **Venue:** NeurIPS 2025 poster\n- **Authors:** Liviu Aolaritei, Zheyu Oliver Wang, Julie Zhu, Michael I. Jordan, and Youssef Marzouk"
    ],
    "durationSeconds": 5.614521929999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0f76a402-0d6a-434e-bc6b-00b3ad120939",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-30T07:51:11.387Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MQMfNgQ2zKKJsKK9f3aSUV`</summary>

```json
{
  "query": "RobustRAG certified defense corpus poisoning SaTML 2026 ReliabilityRAG NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db75d074-05a3-43a6-a5bd-1e80d4144236",
  "isSidechain": false,
  "requestId": "req_011CbYPWRHj8CFEmbnTHmiTV",
  "type": "assistant",
  "uuid": "bf2f9776-033d-4b31-a28d-a39e34bb311e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AKbhB9iHaJCttpQGLcrfTn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 895,
      "cache_read_input_tokens": 20835,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 895,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 20835,
          "cache_creation_input_tokens": 895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 895
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

_source line 18 · 2026-05-30T07:51:21.550Z_

<details><summary>↩ Tool result · `toolu_01MQMfNgQ2zKKJsKK9f3aSUV`</summary>

```text
Web search results for query: "RobustRAG certified defense corpus poisoning SaTML 2026 ReliabilityRAG NeurIPS 2025"

Links: [{"title":"Addressing Corpus Knowledge Poisoning Attacks on RAG Using Sparse Attention","url":"https://www.arxiv.org/pdf/2602.04711"},{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/pdf/2509.23519"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search | OpenReview","url":"https://openreview.net/forum?id=D9JeNTs5Bu"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/pdf/2405.15556"},{"title":"Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems","url":"https://arxiv.org/pdf/2603.18034"},{"title":"IEEE SaTML 2026 · Program","url":"https://satml.org/program/"},{"title":"IEEE SaTML 2026 · Accepted Papers","url":"https://satml.org/accepted-papers/"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://openreview.net/pdf?id=D9JeNTs5Bu"}]

Based on the search results, here's what I found about these research topics:

## RobustRAG and Certified Defense

RobustRAG is a defense framework with certifiable robustness against retrieval corruption attacks, where malicious passages injected into retrieval results can lead to inaccurate model responses. The key insight of RobustRAG is an isolate-then-aggregate strategy: it isolates passages into disjoint groups, generates LLM responses based on the concatenated passages from each isolated group, and then securely aggregates these responses for a robust output. RobustRAG was accepted at IEEE SaTML 2026.

## ReliabilityRAG at NeurIPS 2025

ReliabilityRAG uses a MIS (Maximal Independent Set) variant that prioritizes higher-reliability documents and provides provable robustness guarantees against bounded adversarial corruption, along with a scalable weighted sample and aggregate framework that utilizes reliability information while efficiently handling many documents. ReliabilityRAG is a framework for adversarial robustness that explicitly leverages reliability information of retrieved documents. ReliabilityRAG was published at NeurIPS 2025 as a poster presentation.

## Comparison

ReliabilityRAG addresses limitations of RobustRAG, a major existing RAG framework aimed at providing adversarial robustness, which suffers from limited performance in benign (no-attack) scenarios and struggles in complex generation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf2f9776-033d-4b31-a28d-a39e34bb311e",
  "isSidechain": false,
  "promptId": "121afd3a-f968-4ef5-8969-c92e4fdf9808",
  "type": "user",
  "uuid": "70ad191b-9157-431f-83f8-ca5886151a0b",
  "toolUseResult": {
    "query": "RobustRAG certified defense corpus poisoning SaTML 2026 ReliabilityRAG NeurIPS 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_0134kv5u7JXkbvxXXkDsCptu",
        "content": [
          {
            "title": "Addressing Corpus Knowledge Poisoning Attacks on RAG Using Sparse Attention",
            "url": "https://www.arxiv.org/pdf/2602.04711"
          },
          {
            "title": "RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2512.24268"
          },
          {
            "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://arxiv.org/pdf/2509.23519"
          },
          {
            "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search | OpenReview",
            "url": "https://openreview.net/forum?id=D9JeNTs5Bu"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://arxiv.org/pdf/2405.15556"
          },
          {
            "title": "Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems",
            "url": "https://arxiv.org/pdf/2603.18034"
          },
          {
            "title": "IEEE SaTML 2026 · Program",
            "url": "https://satml.org/program/"
          },
          {
            "title": "IEEE SaTML 2026 · Accepted Papers",
            "url": "https://satml.org/accepted-papers/"
          },
          {
            "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://openreview.net/pdf?id=D9JeNTs5Bu"
          }
        ]
      },
      "Based on the search results, here's what I found about these research topics:\n\n## RobustRAG and Certified Defense\n\nRobustRAG is a defense framework with certifiable robustness against retrieval corruption attacks, where malicious passages injected into retrieval results can lead to inaccurate model responses. The key insight of RobustRAG is an isolate-then-aggregate strategy: it isolates passages into disjoint groups, generates LLM responses based on the concatenated passages from each isolated group, and then securely aggregates these responses for a robust output. RobustRAG was accepted at IEEE SaTML 2026.\n\n## ReliabilityRAG at NeurIPS 2025\n\nReliabilityRAG uses a MIS (Maximal Independent Set) variant that prioritizes higher-reliability documents and provides provable robustness guarantees against bounded adversarial corruption, along with a scalable weighted sample and aggregate framework that utilizes reliability information while efficiently handling many documents. ReliabilityRAG is a framework for adversarial robustness that explicitly leverages reliability information of retrieved documents. ReliabilityRAG was published at NeurIPS 2025 as a poster presentation.\n\n## Comparison\n\nReliabilityRAG addresses limitations of RobustRAG, a major existing RAG framework aimed at providing adversarial robustness, which suffers from limited performance in benign (no-attack) scenarios and struggles in complex generation tasks."
    ],
    "durationSeconds": 10.159376947,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bf2f9776-033d-4b31-a28d-a39e34bb311e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-30T07:51:23.572Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012i5HfDyh35AJGFYKKAEjPb`</summary>

```json
{
  "query": "conformal prediction adversarial robustness RAG abstention certified guarantee 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70ad191b-9157-431f-83f8-ca5886151a0b",
  "isSidechain": false,
  "requestId": "req_011CbYPXLzYBAKEkS2vJdVPh",
  "type": "assistant",
  "uuid": "b223e203-9a50-4cc9-91c9-c5afd5b5b4ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NkcoYMJfWEzgDyS5EAMNAP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 869,
      "cache_read_input_tokens": 21730,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 869,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 21730,
          "cache_creation_input_tokens": 869,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 869
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

_source line 20 · 2026-05-30T07:51:31.621Z_

<details><summary>↩ Tool result · `toolu_012i5HfDyh35AJGFYKKAEjPb`</summary>

```text
Web search results for query: "conformal prediction adversarial robustness RAG abstention certified guarantee 2025 2026"

Links: [{"title":"Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0031320325007113"},{"title":"Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks | Request PDF","url":"https://www.researchgate.net/publication/393421882_Verifiably_robust_conformal_prediction_for_probabilistic_guarantees_under_adversarial_attacks"},{"title":"Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks - King's College London","url":"https://kclpure.kcl.ac.uk/portal/en/publications/verifiably-robust-conformal-prediction-for-probabilistic-guarante"},{"title":"Adversarially Robust Conformal Prediction","url":"https://www.emergentmind.com/topics/adversarially-robust-conformal-prediction"},{"title":"Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://arxiv.org/html/2506.07804v1"},{"title":"Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://arxiv.org/pdf/2506.07804"},{"title":"Provably Robust Conformal Prediction with Improved efficiency","url":"https://lilywenglab.github.io/Provably-Robust-Conformal-Prediction/"}]

Based on the web search results, here are the key findings on conformal prediction, adversarial robustness, RAG, abstention, and certified guarantees from 2025-2026:

## Verifiably Robust Conformal Prediction (VRCP)

A recent work presents Verifiably Robust Conformal Prediction (VRCP) that recovers conformal prediction's probabilistic guarantees under adversarial attacks (published February 2026). VRCP combines CP with neural network verification, and unlike existing methods, VRCP supports both classification and regression, and supports all widely-used norms on the adversarial perturbation bounds.

## Framework for Guaranteed Robustness

Conformal Prediction has emerged as a promising paradigm distinguished by its distribution-free properties and robust uncertainty quantification capabilities, excelling in both regression and classification tasks by providing statistically rigorous confidence intervals. CP substantially enhances model robustness against adversarial perturbations, with significant potential for deployment in safety-critical applications such as autonomous driving and medical diagnosis.

## Recent Advances in Adversarial Robustness

Probabilistic, two-quantile, and smoothing-based approaches (aPRCP, CAS, RCP1, BinCP) offer set-size reductions of 2x–10x compared to prior robust CP methods, with negligible empirical coverage loss. Reasoning-enhanced frameworks (COLEP) further tighten coverage (up to +14% certified coverage improvement) and reduce set size via logical correction and exact marginalization using probabilistic circuits.

The search results focus primarily on conformal prediction and adversarial robustness, but do not contain specific information about RAG (Retrieval-Augmented Generation) or abstention mechanisms in this context.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b223e203-9a50-4cc9-91c9-c5afd5b5b4ab",
  "isSidechain": false,
  "promptId": "121afd3a-f968-4ef5-8969-c92e4fdf9808",
  "type": "user",
  "uuid": "57b7047e-f627-4bce-96ed-3e48f8d1affb",
  "toolUseResult": {
    "query": "conformal prediction adversarial robustness RAG abstention certified guarantee 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Pces11aqqtjGLNXYbkZBRt",
        "content": [
          {
            "title": "Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S0031320325007113"
          },
          {
            "title": "Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks | Request PDF",
            "url": "https://www.researchgate.net/publication/393421882_Verifiably_robust_conformal_prediction_for_probabilistic_guarantees_under_adversarial_attacks"
          },
          {
            "title": "Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks - King's College London",
            "url": "https://kclpure.kcl.ac.uk/portal/en/publications/verifiably-robust-conformal-prediction-for-probabilistic-guarante"
          },
          {
            "title": "Adversarially Robust Conformal Prediction",
            "url": "https://www.emergentmind.com/topics/adversarially-robust-conformal-prediction"
          },
          {
            "title": "Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability",
            "url": "https://arxiv.org/html/2506.07804v1"
          },
          {
            "title": "Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability",
            "url": "https://arxiv.org/pdf/2506.07804"
          },
          {
            "title": "Provably Robust Conformal Prediction with Improved efficiency",
            "url": "https://lilywenglab.github.io/Provably-Robust-Conformal-Prediction/"
          }
        ]
      },
      "Based on the web search results, here are the key findings on conformal prediction, adversarial robustness, RAG, abstention, and certified guarantees from 2025-2026:\n\n## Verifiably Robust Conformal Prediction (VRCP)\n\nA recent work presents Verifiably Robust Conformal Prediction (VRCP) that recovers conformal prediction's probabilistic guarantees under adversarial attacks (published February 2026). VRCP combines CP with neural network verification, and unlike existing methods, VRCP supports both classification and regression, and supports all widely-used norms on the adversarial perturbation bounds.\n\n## Framework for Guaranteed Robustness\n\nConformal Prediction has emerged as a promising paradigm distinguished by its distribution-free properties and robust uncertainty quantification capabilities, excelling in both regression and classification tasks by providing statistically rigorous confidence intervals. CP substantially enhances model robustness against adversarial perturbations, with significant potential for deployment in safety-critical applications such as autonomous driving and medical diagnosis.\n\n## Recent Advances in Adversarial Robustness\n\nProbabilistic, two-quantile, and smoothing-based approaches (aPRCP, CAS, RCP1, BinCP) offer set-size reductions of 2x–10x compared to prior robust CP methods, with negligible empirical coverage loss. Reasoning-enhanced frameworks (COLEP) further tighten coverage (up to +14% certified coverage improvement) and reduce set size via logical correction and exact marginalization using probabilistic circuits.\n\nThe search results focus primarily on conformal prediction and adversarial robustness, but do not contain specific information about RAG (Retrieval-Augmented Generation) or abstention mechanisms in this context."
    ],
    "durationSeconds": 8.044432594999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b223e203-9a50-4cc9-91c9-c5afd5b5b4ab",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Conformal Abstention for RAG under LP-Bounded Retrieval Shifts  ## Core Problem  How can a RAG system provide di…",
  "leafUuid": "57b7047e-f627-4bce-96ed-3e48f8d1affb",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal abstention for RAG under adversarial retrieval shifts",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764"
}
```

---

### Tool call

_source line 23 · 2026-05-30T07:51:33.851Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CMvv1Af1t2SXL2vJiq2Jsh`</summary>

```json
{
  "query": "\"conformal factuality\" RAG robust distribution shift Chen 2026 arXiv 2603.16817"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57b7047e-f627-4bce-96ed-3e48f8d1affb",
  "isSidechain": false,
  "requestId": "req_011CbYPY63eDmQf9KvuSwLwZ",
  "type": "assistant",
  "uuid": "c2dbc5e0-935e-4fd9-a808-c8b12800b107",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCWPXtuKrheoTn9C4qpQ5h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 914,
      "cache_read_input_tokens": 22599,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 914,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 22599,
          "cache_creation_input_tokens": 914,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 914
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

_source line 24 · 2026-05-30T07:51:40.507Z_

<details><summary>↩ Tool result · `toolu_01CMvv1Af1t2SXL2vJiq2Jsh`</summary>

```text
Web search results for query: ""conformal factuality" RAG robust distribution shift Chen 2026 arXiv 2603.16817"

Links: [{"title":"[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/abs/2603.16817"},{"title":"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/pdf/2603.16817"},{"title":"Not all distributional shifts are equal: Fine-grained robust conformal inference","url":"https://arxiv.org/pdf/2402.13042"},{"title":"Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/html/2502.14105v2"},{"title":"[2506.20978v1] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/abs/2506.20978v1"},{"title":"[2506.20978] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/abs/2506.20978"}]

I found the paper you're looking for! Here are the key details:

**Title:** Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights

**Authors:** Yi Chen, Daiwei Chen, Sukrut Madhay Chikodikar, Caitlyn Heqi Yin, and Ramya Korlakai Vinavak from University of Wisconsin-Madison

**Publication Date:** March 17, 2026

**Main Findings:** The research found that (i) conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, (ii) conformal factuality guarantee is not robust to distribution shifts and distractors, highlighting the limitation that requires calibration data to closely match deployment conditions, and (iii) lightweight entailment-based verifiers match or outperform LLM-based model confidence scorers while requiring over 100× fewer FLOPs.

The paper systematically analyzes how conformal factuality—a method that offers statistical reliability guarantees for RAG-based language models—behaves under real-world conditions, particularly when facing distribution shifts and distractors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2dbc5e0-935e-4fd9-a808-c8b12800b107",
  "isSidechain": false,
  "promptId": "121afd3a-f968-4ef5-8969-c92e4fdf9808",
  "type": "user",
  "uuid": "1f438457-ecd3-4685-a24b-47971ee44d7d",
  "toolUseResult": {
    "query": "\"conformal factuality\" RAG robust distribution shift Chen 2026 arXiv 2603.16817",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UNB7hgzZNKaSuQzNEn1kEU",
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
            "title": "Not all distributional shifts are equal: Fine-grained robust conformal inference",
            "url": "https://arxiv.org/pdf/2402.13042"
          },
          {
            "title": "Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/html/2502.14105v2"
          },
          {
            "title": "[2506.20978v1] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality",
            "url": "https://arxiv.org/abs/2506.20978v1"
          },
          {
            "title": "[2506.20978] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality",
            "url": "https://arxiv.org/abs/2506.20978"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details:\n\n**Title:** Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights\n\n**Authors:** Yi Chen, Daiwei Chen, Sukrut Madhay Chikodikar, Caitlyn Heqi Yin, and Ramya Korlakai Vinavak from University of Wisconsin-Madison\n\n**Publication Date:** March 17, 2026\n\n**Main Findings:** The research found that (i) conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, (ii) conformal factuality guarantee is not robust to distribution shifts and distractors, highlighting the limitation that requires calibration data to closely match deployment conditions, and (iii) lightweight entailment-based verifiers match or outperform LLM-based model confidence scorers while requiring over 100× fewer FLOPs.\n\nThe paper systematically analyzes how conformal factuality—a method that offers statistical reliability guarantees for RAG-based language models—behaves under real-world conditions, particularly when facing distribution shifts and distractors."
    ],
    "durationSeconds": 6.6509347130000025,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c2dbc5e0-935e-4fd9-a808-c8b12800b107",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-30T07:51:42.935Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MJtzcVbz7hMpQVSe7nLVuU`</summary>

```json
{
  "query": "RAGDefender cosine similarity poisoning detection ACSAC 2025 PoisonedRAG USENIX Security"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f438457-ecd3-4685-a24b-47971ee44d7d",
  "isSidechain": false,
  "requestId": "req_011CbYPYjzfmQKDw5TDriMAa",
  "type": "assistant",
  "uuid": "02fb127b-8e67-4d8e-a06e-bd35efe1f638",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XB23MRFvxsaBux9x2trKKV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 704,
      "cache_read_input_tokens": 23513,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 704,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 23513,
          "cache_creation_input_tokens": 704,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 704
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

_source line 26 · 2026-05-30T07:51:51.958Z_

<details><summary>↩ Tool result · `toolu_01MJtzcVbz7hMpQVSe7nLVuU`</summary>

```text
Web search results for query: "RAGDefender cosine similarity poisoning detection ACSAC 2025 PoisonedRAG USENIX Security"

Links: [{"title":"Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems","url":"https://arxiv.org/html/2511.01268v1"},{"title":"RAG Security: How Attackers Poison Your Knowledge Base | BeyondScale","url":"https://beyondscale.tech/blog/rag-security-data-poisoning-guide"},{"title":"Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks","url":"https://kevinkoo001.github.io/assets/pdf/acsac25-ragdefender.pdf"},{"title":"GitHub - SecAI-Lab/RAGDefender: Artifacts for paper \"Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems\" · GitHub","url":"https://github.com/SecAI-Lab/RAGDefender"},{"title":"Secure Retrieval-Augmented Generation against Poisoning Attacks","url":"https://arxiv.org/pdf/2510.25025"},{"title":"GitHub - sleeepeer/PoisonedRAG: [USENIX Security 2025] PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models · GitHub","url":"https://github.com/sleeepeer/PoisonedRAG"},{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models | USENIX","url":"https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag"},{"title":"Safeguarding RAG Pipelines with GMTP: A Gradient-based Masked Token Probability Method for Poisoned Document Detection","url":"https://arxiv.org/pdf/2507.18202"}]

Based on the search results, here's what I found about these research topics:

## RAGDefender (ACSAC 2025)

RAGDefender is a paper titled "Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems" by Minseok Kim, Hankook Lee, and Hyungjoon Koo, appearing at the Annual Computer Security Applications Conference (ACSAC) in 2025. The project includes a GitHub repository with code and evaluation tools for defending against poisoning attacks.

## PoisonedRAG (USENIX Security 2025)

PoisonedRAG is the first knowledge database corruption attack against Retrieval-Augmented Generation (RAG) systems, published at USENIX Security 2025. The attack could achieve a 90% attack success rate when injecting five malicious texts for each target question into a knowledge database with millions of texts.

## Cosine Similarity in Poisoning Attacks

In the PoisonedRAG attack, the attacker crafts malicious document content to maximize cosine similarity with the target query's embedding, which is a key mechanism for ensuring the poisoned documents are retrieved when targeted queries are issued.

## Detection and Defense

Several defenses have been evaluated against PoisonedRAG, but results show they are insufficient to defend against the attack, highlighting the need for new defenses.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02fb127b-8e67-4d8e-a06e-bd35efe1f638",
  "isSidechain": false,
  "promptId": "121afd3a-f968-4ef5-8969-c92e4fdf9808",
  "type": "user",
  "uuid": "81e56837-64af-4120-b09c-7734c32c9817",
  "toolUseResult": {
    "query": "RAGDefender cosine similarity poisoning detection ACSAC 2025 PoisonedRAG USENIX Security",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Hnb7WnJY6d1BD7Kh32fsjx",
        "content": [
          {
            "title": "Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems",
            "url": "https://arxiv.org/html/2511.01268v1"
          },
          {
            "title": "RAG Security: How Attackers Poison Your Knowledge Base | BeyondScale",
            "url": "https://beyondscale.tech/blog/rag-security-data-poisoning-guide"
          },
          {
            "title": "Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks",
            "url": "https://kevinkoo001.github.io/assets/pdf/acsac25-ragdefender.pdf"
          },
          {
            "title": "GitHub - SecAI-Lab/RAGDefender: Artifacts for paper \"Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems\" · GitHub",
            "url": "https://github.com/SecAI-Lab/RAGDefender"
          },
          {
            "title": "Secure Retrieval-Augmented Generation against Poisoning Attacks",
            "url": "https://arxiv.org/pdf/2510.25025"
          },
          {
            "title": "GitHub - sleeepeer/PoisonedRAG: [USENIX Security 2025] PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models · GitHub",
            "url": "https://github.com/sleeepeer/PoisonedRAG"
          },
          {
            "title": "RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2512.24268"
          },
          {
            "title": "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models | USENIX",
            "url": "https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag"
          },
          {
            "title": "Safeguarding RAG Pipelines with GMTP: A Gradient-based Masked Token Probability Method for Poisoned Document Detection",
            "url": "https://arxiv.org/pdf/2507.18202"
          }
        ]
      },
      "Based on the search results, here's what I found about these research topics:\n\n## RAGDefender (ACSAC 2025)\n\nRAGDefender is a paper titled \"Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems\" by Minseok Kim, Hankook Lee, and Hyungjoon Koo, appearing at the Annual Computer Security Applications Conference (ACSAC) in 2025. The project includes a GitHub repository with code and evaluation tools for defending against poisoning attacks.\n\n## PoisonedRAG (USENIX Security 2025)\n\nPoisonedRAG is the first knowledge database corruption attack against Retrieval-Augmented Generation (RAG) systems, published at USENIX Security 2025. The attack could achieve a 90% attack success rate when injecting five malicious texts for each target question into a knowledge database with millions of texts.\n\n## Cosine Similarity in Poisoning Attacks\n\nIn the PoisonedRAG attack, the attacker crafts malicious document content to maximize cosine similarity with the target query's embedding, which is a key mechanism for ensuring the poisoned documents are retrieved when targeted queries are issued.\n\n## Detection and Defense\n\nSeveral defenses have been evaluated against PoisonedRAG, but results show they are insufficient to defend against the attack, highlighting the need for new defenses."
    ],
    "durationSeconds": 9.018382721999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "02fb127b-8e67-4d8e-a06e-bd35efe1f638",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-30T07:51:54.725Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VypEXw5j1G2asyrwYJiJrb`</summary>

```json
{
  "query": "RPS provably reliable conformal prediction data poisoning ICLR 2025 spotlight partition vote"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81e56837-64af-4120-b09c-7734c32c9817",
  "isSidechain": false,
  "requestId": "req_011CbYPZb5uxnNu9v7A1MJ6b",
  "type": "assistant",
  "uuid": "91edca01-5269-41aa-bede-88568dedaaf1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MgX9dte3tZ8gvG84Xa7bGL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 963,
      "cache_read_input_tokens": 24217,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 963,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 24217,
          "cache_creation_input_tokens": 963,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 963
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

_source line 28 · 2026-05-30T07:52:01.609Z_

<details><summary>↩ Tool result · `toolu_01VypEXw5j1G2asyrwYJiJrb`</summary>

```text
Web search results for query: "RPS provably reliable conformal prediction data poisoning ICLR 2025 spotlight partition vote"

Links: [{"title":"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning | OpenReview","url":"https://openreview.net/forum?id=ofuLWn8DFZ"},{"title":"GitHub - yascho/reliable_conformal_prediction: Implementation of the reliable conformal prediction sets introduced in the paper: \"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning\" accepted at ICLR 2025 (Spotlight).","url":"https://github.com/yascho/reliable_conformal_prediction"},{"title":"ICLR Poster Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning","url":"https://iclr.cc/virtual/2025/poster/28340"},{"title":"Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning","url":"https://arxiv.org/pdf/2410.09878"},{"title":"PROVABLY RELIABLE CONFORMAL PREDICTION SETS IN THE PRESENCE OF DATA POISONING - Technical University of Munich","url":"https://portal.fis.tum.de/en/publications/provably-reliable-conformal-prediction-sets-in-the-presence-of-da/"},{"title":"Nine papers accepted at ICLR 2025, one at KAIS 2025 - Data Analytics and Machine Learning","url":"https://www.cs.cit.tum.de/en/daml/all-news/article/nine-papers-accepted-at-iclr-2025/"},{"title":"[2410.09878] Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning","url":"https://arxiv.org/abs/2410.09878"},{"title":"provably reliable conformal prediction sets","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4d21a4b33361c40c2142db9511c126-Paper-Conference.pdf"}]

Based on the search results, I found comprehensive information about your query:

## RPS: Provably Reliable Conformal Prediction Sets

The paper "Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning" was published as an ICLR 2025 Spotlight.

**What is RPS?**

RPS is the first efficient method for constructing conformal prediction sets with provable reliability guarantees under poisoning. Conformal prediction is normally not reliable under poisoning attacks where adversaries manipulate both training and calibration data, which can significantly alter prediction sets in practice.

**How does RPS work?**

The method uses two key components:

1. To ensure reliability under training poisoning, RPS introduces smoothed score functions that reliably aggregate predictions of classifiers trained on distinct partitions of the training data.

2. To ensure reliability under calibration poisoning, it constructs multiple prediction sets, each calibrated on distinct subsets of the calibration data.

The approach uses smoothed score functions and majority-voting prediction sets calibrated on distinct data subsets to ensure reliability even under malicious poisoning manipulations.

**Authors and Implementation:**

The paper was authored by Yan Scholten and Stephan Günnemann, and reference implementation of RPS is available with demo notebooks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91edca01-5269-41aa-bede-88568dedaaf1",
  "isSidechain": false,
  "promptId": "121afd3a-f968-4ef5-8969-c92e4fdf9808",
  "type": "user",
  "uuid": "be6227ca-cdc3-41c2-940f-aeb46b09f716",
  "toolUseResult": {
    "query": "RPS provably reliable conformal prediction data poisoning ICLR 2025 spotlight partition vote",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SCJnpogbXGG7v4C9HbypHm",
        "content": [
          {
            "title": "Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning | OpenReview",
            "url": "https://openreview.net/forum?id=ofuLWn8DFZ"
          },
          {
            "title": "GitHub - yascho/reliable_conformal_prediction: Implementation of the reliable conformal prediction sets introduced in the paper: \"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning\" accepted at ICLR 2025 (Spotlight).",
            "url": "https://github.com/yascho/reliable_conformal_prediction"
          },
          {
            "title": "ICLR Poster Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning",
            "url": "https://iclr.cc/virtual/2025/poster/28340"
          },
          {
            "title": "Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning",
            "url": "https://arxiv.org/pdf/2410.09878"
          },
          {
            "title": "PROVABLY RELIABLE CONFORMAL PREDICTION SETS IN THE PRESENCE OF DATA POISONING - Technical University of Munich",
            "url": "https://portal.fis.tum.de/en/publications/provably-reliable-conformal-prediction-sets-in-the-presence-of-da/"
          },
          {
            "title": "Nine papers accepted at ICLR 2025, one at KAIS 2025 - Data Analytics and Machine Learning",
            "url": "https://www.cs.cit.tum.de/en/daml/all-news/article/nine-papers-accepted-at-iclr-2025/"
          },
          {
            "title": "[2410.09878] Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning",
            "url": "https://arxiv.org/abs/2410.09878"
          },
          {
            "title": "provably reliable conformal prediction sets",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4d21a4b33361c40c2142db9511c126-Paper-Conference.pdf"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about your query:\n\n## RPS: Provably Reliable Conformal Prediction Sets\n\nThe paper \"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning\" was published as an ICLR 2025 Spotlight.\n\n**What is RPS?**\n\nRPS is the first efficient method for constructing conformal prediction sets with provable reliability guarantees under poisoning. Conformal prediction is normally not reliable under poisoning attacks where adversaries manipulate both training and calibration data, which can significantly alter prediction sets in practice.\n\n**How does RPS work?**\n\nThe method uses two key components:\n\n1. To ensure reliability under training poisoning, RPS introduces smoothed score functions that reliably aggregate predictions of classifiers trained on distinct partitions of the training data.\n\n2. To ensure reliability under calibration poisoning, it constructs multiple prediction sets, each calibrated on distinct subsets of the calibration data.\n\nThe approach uses smoothed score functions and majority-voting prediction sets calibrated on distinct data subsets to ensure reliability even under malicious poisoning manipulations.\n\n**Authors and Implementation:**\n\nThe paper was authored by Yan Scholten and Stephan Günnemann, and reference implementation of RPS is available with demo notebooks."
    ],
    "durationSeconds": 6.879159023999994,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "91edca01-5269-41aa-bede-88568dedaaf1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-30T07:52:01.612Z_

```json
{
  "parentUuid": "be6227ca-cdc3-41c2-940f-aeb46b09f716",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "850807e3-8a8d-4ffd-b1c0-69fb4866841e",
  "timestamp": "2026-05-30T07:52:01.612Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-30T07:52:03.973Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017dWxoVRnSknXEJzKqffktW`</summary>

```json
{
  "query": "PASC pipeline-aware conformal prediction multi-stage NLP arXiv 2605.18812 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "850807e3-8a8d-4ffd-b1c0-69fb4866841e",
  "isSidechain": false,
  "requestId": "req_011CbYPaJDvydUuWdTQDB4on",
  "type": "assistant",
  "uuid": "bb50560f-18e5-48bc-bfc1-d04e1e89ddfc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hkd8rxLZKmAQwrvHz8uqhD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1014,
      "cache_read_input_tokens": 25180,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1014,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 25180,
          "cache_creation_input_tokens": 1014,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1014
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

_source line 31 · 2026-05-30T07:52:11.183Z_

<details><summary>↩ Tool result · `toolu_017dWxoVRnSknXEJzKqffktW`</summary>

```text
Web search results for query: "PASC pipeline-aware conformal prediction multi-stage NLP arXiv 2605.18812 2025"

Links: [{"title":"[2605.18812] PASC: Pipeline-Aware Conformal Prediction with Joint Coverage Guarantees for Multi-Stage NLP and LLM Pipelines","url":"https://arxiv.org/abs/2605.18812"},{"title":"PASC: Pipeline-Aware Conformal Prediction with Joint Coverage Guarantees for Multi-Stage NLP and LLM Pipelines","url":"https://arxiv.org/html/2605.18812"},{"title":"Conformal Prediction with Large Language Models for Multi-Choice   Question Answering","url":"https://arxiv.org/pdf/2305.18404"},{"title":"Conformal Prediction for Natural Language Processing: A Survey","url":"https://arxiv.org/pdf/2405.01976"},{"title":"Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition","url":"https://arxiv.org/pdf/2510.04406"},{"title":"Conformal Prediction for Multimodal Regression","url":"https://arxiv.org/pdf/2410.19653"}]

Based on the search results, I found the paper you're looking for:

PASC (Pipeline-Aware Split Conformal) is a method that reduces multi-stage joint coverage to a single scalar conformal prediction problem on the joint maximum nonconformity score.

Modern NLP and LLM systems are pipelines including named entity recognition (NER) -> entity disambiguation (NED) -> entity typing, retrieval-augmented generation (retriever -> reader), and agentic chains of planner -> tool -> critic. Errors compound across stages, but existing uncertainty quantification methods either calibrate each stage independently (no joint coverage) or apply a Bonferroni union bound (joint coverage, but conservative).

PASC provides a finite-sample distribution-free guarantee that all K stages are simultaneously covered with probability at least 1 - alpha, and is nearly tight up to a 1/(n+1) factor. On a three-stage NER -> NED -> entity-typing pipeline over CoNLL-2003, PASC achieves 96.4% end-to-end coverage versus 93.4% for Bonferroni and 86.5% for independent CP, at identical average prediction size.

The paper (arXiv 2605.18812) was published recently and is available at https://arxiv.org/abs/2605.18812.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb50560f-18e5-48bc-bfc1-d04e1e89ddfc",
  "isSidechain": false,
  "promptId": "121afd3a-f968-4ef5-8969-c92e4fdf9808",
  "type": "user",
  "uuid": "77123756-b59b-4982-af9c-176af240290c",
  "toolUseResult": {
    "query": "PASC pipeline-aware conformal prediction multi-stage NLP arXiv 2605.18812 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01X5SaxUEvN25UMssXf7qQHy",
        "content": [
          {
            "title": "[2605.18812] PASC: Pipeline-Aware Conformal Prediction with Joint Coverage Guarantees for Multi-Stage NLP and LLM Pipelines",
            "url": "https://arxiv.org/abs/2605.18812"
          },
          {
            "title": "PASC: Pipeline-Aware Conformal Prediction with Joint Coverage Guarantees for Multi-Stage NLP and LLM Pipelines",
            "url": "https://arxiv.org/html/2605.18812"
          },
          {
            "title": "Conformal Prediction with Large Language Models for Multi-Choice   Question Answering",
            "url": "https://arxiv.org/pdf/2305.18404"
          },
          {
            "title": "Conformal Prediction for Natural Language Processing: A Survey",
            "url": "https://arxiv.org/pdf/2405.01976"
          },
          {
            "title": "Modular and Adaptive Conformal Prediction for Sequential Models via Residual Decomposition",
            "url": "https://arxiv.org/pdf/2510.04406"
          },
          {
            "title": "Conformal Prediction for Multimodal Regression",
            "url": "https://arxiv.org/pdf/2410.19653"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nPASC (Pipeline-Aware Split Conformal) is a method that reduces multi-stage joint coverage to a single scalar conformal prediction problem on the joint maximum nonconformity score.\n\nModern NLP and LLM systems are pipelines including named entity recognition (NER) -> entity disambiguation (NED) -> entity typing, retrieval-augmented generation (retriever -> reader), and agentic chains of planner -> tool -> critic. Errors compound across stages, but existing uncertainty quantification methods either calibrate each stage independently (no joint coverage) or apply a Bonferroni union bound (joint coverage, but conservative).\n\nPASC provides a finite-sample distribution-free guarantee that all K stages are simultaneously covered with probability at least 1 - alpha, and is nearly tight up to a 1/(n+1) factor. On a three-stage NER -> NED -> entity-typing pipeline over CoNLL-2003, PASC achieves 96.4% end-to-end coverage versus 93.4% for Bonferroni and 86.5% for independent CP, at identical average prediction size.\n\nThe paper (arXiv 2605.18812) was published recently and is available at https://arxiv.org/abs/2605.18812."
    ],
    "durationSeconds": 7.20463038599999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bb50560f-18e5-48bc-bfc1-d04e1e89ddfc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-30T07:52:54.467Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information from my searches. Let me synthesize the findings and provide a comprehensive evaluation of this proposal.

Let me think about this proposal carefully:

**What the proposal is about:**
- LP-RAG-Abstain: A method that provides distribution-free certified abstention guarantees for RAG systems under bounded retrieval distributional shifts (including adversarial corpus poisoning)
- Uses LP-CP (Lévy-Prokhorov Conformal Prediction) framework applied to retrieval-level pairwise cosine similarity scores
- Key insight: anchoring nonconformity scores at retrieval-agreement level (not answer-confidence level) is necessary for LP-CP to give non-vacuous guarantees because the Lipschitz constant is analytically bounded


- **Strengths**: The proposal identifies a genuine gap in the literature—no prior work combines conformal prediction with RAG systems under adversarial robustness. The theoretical foundation is solid, with the retrieval-level scoring approach justified by Lipschitz constant analysis. It's also well-differentiated from existing methods like TRAQ.

- **Experimental rigor**: The evaluation is comprehensive, covering eight baselines, multiple attack vectors, different embedding models, ablations, and adaptive attacks with cross-validation and parameter heatmaps.

- **Practical appeal**: The abstention mechanism addresses safety-critical use cases, and operating at the retrieval level keeps the approach agnostic to the downstream LLM.

- **Core concern**: The main technical novelty reduces to applying conformal prediction with a pairwise cosine similarity scoring function, which raises questions about the depth of the contribution.

- **Conditional guarantees**: The method requires knowing attack bounds (ρ₀, ε₀) upfront; if actual attacks exceed these, the guarantees break down—a potential reviewer objection.

- **Positioning against RAGDefender**: Both use the same similarity signal, so the distinction hinges on the decision rule and formal guarantees rather than a fundamentally different approach.

- **Lipschitz analysis**: The theoretical justification for why retrieval-level anchoring works better than answer-level scoring depends on how tight the Lipschitz bounds actually are in practice.

- **Practical conservatism**: If certified coverage diverges too far from empirical results, the method risks being overly conservative and unusable.

- **Limited scope of abstention**: Unlike RobustRAG or ReliabilityRAG, this approach can only refuse to answer under attack rather than produce correct outputs, which some might see as a weaker defense.

The proposal is well-structured with a clear gap in the literature and sound theory, but the main vulnerabilities are the incremental nature relative to existing work, the conditional nature of the guarantees, and whether the certified bounds remain practical.

Thinking through the acceptance probability: the research problem is genuinely novel and well-motivated, the method is principled though potentially viewed as an application of existing techniques, and the experimental plan is thorough. The feasibility is strong since there's no training overhead. I'd estimate this lands around 40-42%, making it a competitive paper that hinges on how reviewers weigh novelty against the solid execution and real problem being solved. Given typical AAAI acceptance rates around 20-25%, this puts it above the median but not a clear accept. average quality. Let me think about whether that's justified.

Arguments for higher probability:
- Clear, verifiable gap in literature
- Strong theoretical contribution (Lipschitz analysis, necessary condition argument)
- Comprehensive experimental design
- Timely topic (RAG security + formal guarantees)
- Well-positioned relative to very recent work

Arguments for lower probability:
- Core method could be seen as straightforward LP-CP application
- Conditional guarantees might be viewed as limited
- Same signal as RAGDefender
- No actual experimental results yet (this is a proposal)

The proposal is extremely well-researched with a thorough literature review and genuine gap. The key insight about why retrieval-level scoring is necessary through Lipschitz analysis feels like a real contribution rather than just applying existing techniques, and the experimental design is remarkably comprehensive for a proposal. I'll settle on 35-48%, with a median around 40%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77123756-b59b-4982-af9c-176af240290c",
  "isSidechain": false,
  "requestId": "req_011CbYPb1VdYFsFjvwrG4u8U",
  "type": "assistant",
  "uuid": "fea1a8ed-8268-4a88-a948-e838e8687a09",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ZUhurUH8qFVVLeBYJb2PY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 712,
      "cache_read_input_tokens": 26194,
      "output_tokens": 6906,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 712,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6906,
          "cache_read_input_tokens": 26194,
          "cache_creation_input_tokens": 712,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 712
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

_source line 33 · 2026-05-30T07:54:43.704Z_

Now I have sufficient information from the literature searches. Let me compile the evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [LP-CP: Conformal Prediction under Lévy-Prokhorov Distribution Shifts](https://arxiv.org/abs/2502.14105) (NeurIPS 2025): 本 proposal 的核心理论基础。提供了在 LP 分布偏移下的闭式最坏情形分位数，其 (ρ, ε) 参数化恰好映射到 RAG 投毒场景。原论文未涉及 RAG 应用。
- [TRAQ: Trustworthy Retrieval Augmented QA via Conformal Prediction](https://arxiv.org/pdf/2307.04642) (NAACL 2024): CP-for-RAG 的开创性工作，提供端到端覆盖保证，但假设可交换性，不处理对抗性检索偏移。
- [C-RAG: Certified Generation Risks for RAG](https://arxiv.org/abs/2402.12888) (ICML 2024): 为 RAG 提供共形风险控制，但同样假设良性检索分布。
- [Chen et al.: Is Conformal Factuality for RAG-based LLMs Robust?](https://arxiv.org/abs/2603.16817) (arXiv 2026.03): 明确诊断了 CP 保证在 RAG 分布偏移下失效的问题，但**未提出解决方案**——这正是本 proposal 声称要填补的空白。
- [RobustRAG: Certifiably Robust RAG against Retrieval Corruption](https://arxiv.org/pdf/2405.15556) (SaTML 2026): 隔离-聚合策略，在 RealtimeQA 上认证鲁棒准确率 38%（清洁 71%）。仅产生答案，无弃权机制。
- [ReliabilityRAG](https://openreview.net/forum?id=D9JeNTs5Bu) (NeurIPS 2025): 基于图论 MIS 的可靠性加权防御，k′ ≤ k/5 投毒预算下的可证鲁棒性。同样仅产生答案。
- [RAGDefender: Rescuing the Unpoisoned](https://kevinkoo001.github.io/assets/pdf/acsac25-ragdefender.pdf) (ACSAC 2025): 使用余弦相似度聚类检测投毒文档，0.18 ASR @ 10× 投毒比。**与本 proposal 使用相同底层信号**，但基于启发式阈值，无形式化保证。
- [RPS: Provably Reliable CP under Data Poisoning](https://openreview.net/forum?id=ofuLWn8DFZ) (ICLR 2025 Spotlight): 分区投票处理校准时投毒——与 RAG 中测试时检索投毒是根本不同的威胁模型，保证不可迁移。
- [PoisonedRAG](https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag) (USENIX Security 2025): 多文档注入攻击达 97% ASR，包含黑盒和白盒变体。proposal 的主要攻击评估对象。
- [PASC: Pipeline-Aware Conformal Prediction](https://arxiv.org/abs/2605.18812) (arXiv 2026.05): 多阶段 NLP 管道的联合覆盖保证，含 RAG 管道。与本 proposal 的组合扩展方向互补。
- [OPSA: Enhancing Adversarial Robustness with CP](https://arxiv.org/abs/2506.07804) (arXiv 2025): CP 目标自适应攻击方法论，proposal 的自适应攻击评估参考。

- **调研总结**: {CP} ∩ {RAG} ∩ {对抗鲁棒性/分布偏移} 这个三方交叉确实是空白。Chen et al. (2026) 明确提出了问题但未给出方案；RobustRAG 和 ReliabilityRAG 提供认证防御但无弃权机制；TRAQ/C-RAG 提供 CP 保证但不处理偏移。LP-CP 的 (ρ, ε) 参数化与 RAG 投毒参数的自然映射尚未被任何工作利用。该 proposal 瞄准了一个真实且有文献支撑的研究空白。

【整体印象】:
如果我是审稿人，第一反应是这是一份**精心准备、定位清晰**的投稿。研究空白是真实可验证的（Chen et al. 2026 的诊断 + 无人提出方案），理论动机有说服力（Lipschitz 分析解释了为什么检索层锚定是必要的而非仅仅方便），实验设计异常完备。我会倾向于 **weak accept**，但会对两个问题保持警惕：(1) 核心方法是否会被视为 LP-CP 的直接应用 + RAGDefender 的信号？(2) 条件保证（需预设 ρ₀, ε₀）的实际效用如何？如果作者能在论文中充分论证 Lipschitz 必要性分析本身的理论贡献深度，并展示认证边界与经验覆盖的差距不大，这篇论文有较好的中稿机会。

【核心贡献】:
1. **理论贡献**：证明了在 RAG 系统中，检索层锚定是 LP-CP 产生非空洞保证的**必要条件**（通过 Lipschitz 常数分析：答案层 ∝ 模型深度和上下文长度不可控增长 vs. 检索层 O(2/k) 解析有界）。这不仅是一个应用层面的设计选择，而是一个有理论支撑的必要性结论。
2. **系统贡献**：首个在分布偏移下为 RAG 提供分布无关认证弃权保证的框架（"Safe Silence"保证），填补了 CP-for-RAG 与对抗鲁棒 RAG 之间的明确空白。
3. **实践贡献**：LLM 无关、可与下游任何生成器组合、可与 TRAQ/C-RAG 等答案层 CP 方法组合。

**贡献价值评估**：该贡献对领域有中等偏上的价值。它为一个重要的实际问题（RAG 在对抗环境下何时应拒绝回答）提供了第一个理论框架。对安全关键 RAG 应用（医疗、法律、金融）有直接意义。但核心理论深度（LP-CP 的应用 + Lipschitz 分析）可能不足以达到 top-tier 理论贡献的水平。

【方法合理性】:
方法整体**合理且原则性强**。LP-CP 的 (ρ, ε) 参数化与 RAG 投毒的自然对应是优雅的，检索层余弦相似度的 Lipschitz 有界性论证在数学上可信。

**潜在替代方案的考量**：
1. **更简单的替代**：直接在 RAGDefender 的余弦相似度阈值上加 Bonferroni 校正 → 但这无法给出随攻击预算连续变化的保证，且 proposal 已在 ablation 中包含了 LP-CP vs. Bonferroni 对比。
2. **RPS 式分区投票**：将 top-k 文档分区 + 分别校准 → 但 RPS 处理的是校准时投毒，RAG 中投毒发生在测试时检索阶段，威胁模型不同。proposal 正确指出了这一区别。
3. **直接用答案层 CP**：如 TRAQ 的 answer-set approach → 但 Chen et al. 已证明在分布偏移下失效，且 proposal 的 Lipschitz 分析解释了为什么这在理论上也行不通。

方法的主要合理性风险在于：**Lipschitz 上界的紧致性**。如果 O(2/k) 的解析上界在实践中远大于实际 Lipschitz 常数，认证保证将过于保守（高弃权率）。Proposal 已规划了经验 Lipschitz 常数估计和紧致性分析，这是正确的应对策略。

【5 维度打分】:

  1. 研究问题: 【强】 — 问题定义精确，研究空白有文献明确支撑（Chen et al. 2026 诊断 + 无人解决）。{CP} ∩ {RAG} ∩ {对抗鲁棒性} 的空白经过 2 份 RAG 安全综述、TACL CP-NLP 综述和 15+ 定向搜索验证。安全关键 RAG 应用中"何时应拒绝回答"是实际且重要的问题。唯一保留：弃权（vs. 鲁棒回答）的实际部署价值可能被部分审稿人质疑——但 proposal 的"Safe Silence"论证有效地回应了这一点。

  2. 方法与创新: 【中偏强】 — Lipschitz 必要性分析（检索层 vs. 答案层）是一个有价值的理论洞见，超越了简单的"把 LP-CP 应用到 RAG"。但核心技术路径——LP-CP + 余弦相似度分数——的组合确实是对已有工具的应用，RAGDefender (ACSAC 2025) 已使用了相同的底层信号（余弦相似度区分投毒）。关键差异在保证层面（分布无关覆盖 vs. 启发式阈值），这是实质性的但可能被部分审稿人视为增量式。与 RobustRAG、ReliabilityRAG 的差异化（弃权 vs. 答案）清晰。

  3. 实验设计: 【强】 — 这是 proposal 最突出的亮点之一。8 个 baseline（覆盖 CP-for-RAG、认证防御、启发式防御、朴素方案）、3 个数据集、2 种攻击（黑盒+白盒+单文档）、3 个嵌入模型、2 个 LLM、7 项消融、(ρ,ε) 热力图、自适应攻击评估（引用 OPSA 方法论）、跨攻击验证——几乎涵盖了审稿人可能要求的所有评估维度。分层实验组织（核心→泛化→消融→GPT-4o 有限实验）也体现了对计算资源的合理规划。唯一可补充的是更多真实场景（organic drift、domain mismatch）的评估，而非仅限于合成攻击。

  4. 可行性: 【强】 — 方法不需要模型训练，主要计算是嵌入余弦相似度（O(k²) per query）+ LP-CP 闭式计算。依赖开源嵌入模型和 LLM（Qwen3-Embedding-8B、Llama-3.1-8B）和公开数据集（NQ、HotpotQA、MS-MARCO）。PoisonedRAG 和 CorruptRAG 有开源代码。GPT-4o API 调用有成本但可控。整体技术可行性高，无需特殊资源。

  5. 写作与呈现: 【强】 — Proposal 结构清晰，定位精确，文献调研详尽（25+ 参考文献，覆盖 CP、RAG、攻防、鲁棒 CP 等多个子领域）。与每个相关工作的差异化分析具体且有说服力（特别是与 RAGDefender 的三层对比：信号层/决策规则层/保证层）。威胁模型定义清晰，与 RobustRAG 类比 (ρ₀, ε₀) 作为防御输入参数。理论论证逻辑链完整：Lipschitz 不可控 → 答案层 LP-CP 空洞 → 检索层锚定必要 → O(2/k) 有界 → 非空洞保证。

【概率估计】: [33% - 48%] 中位 40%

【估计理由】:
**上推因素**：(1) 研究空白真实且可验证，有 Chen et al. 2026 的明确诊断作为"问题提出"的文献支撑；(2) 理论动机严谨，Lipschitz 必要性分析超越了简单应用；(3) 实验设计在 proposal 阶段已达到极高完备度（8 baseline、自适应攻击、跨攻击验证、7 项消融），这本身就是强有力的信号；(4) 时效性好，RAG 安全和 CP 都是热点方向；(5) "Safe Silence"叙事对安全关键应用有说服力。

**下拉因素**：(1) 核心技术贡献可能被视为 LP-CP（已有工具）+ 余弦相似度（RAGDefender 已用信号）的组合应用，novelty 深度可能被质疑；(2) 条件保证（需要预设 ρ₀, ε₀）的实用性——实际部署中如何选择这些参数？过于保守的选择导致高弃权率，过于乐观则保证失效；(3) 弃权 vs. 鲁棒回答的价值争论——部分审稿人可能认为 RobustRAG/ReliabilityRAG 的"尽力回答"比"拒绝回答"更实用；(4) 尚无实验结果验证关键假设（Lipschitz 上界紧致性、认证边界非空洞性）。

**综合判断**：这是一份定位精准、准备充分的投稿，研究空白真实、方法原则性强、实验设计完备。中位 40% 反映了它在整体质量上高于平均水平，但面临 novelty 深度和实际效用方面的审稿人分歧风险。如果 Lipschitz 紧致性实验结果良好（认证与经验覆盖差距 < 10%），概率可上浮至 45-48%；如果紧致性差（差距 > 25%），则下滑至 30-33%。

【主要风险】:
1. **Novelty 深度质疑**：核心方法被审稿人解读为"LP-CP 直接应用 + RAGDefender 信号重用"，理论贡献被降格为"已知工具在新场景的组合"。需要论文中强有力地论证 Lipschitz 必要性分析本身是非平凡的理论贡献。
2. **认证边界过于保守**：如果 O(2/k) 的 Lipschitz 上界远大于实际值，LP-CP 的最坏情形分位数将导致极高的弃权率（例如 >50%），使方法在实践中无用。这是一个实验阶段才能验证的风险，但直接影响整篇论文的可信度。

【实施评估】:
  - 计算资源: 中等。主要需求：(1) 嵌入模型推理（Qwen3-Embedding-8B 最大，可用单 A100）；(2) LLM 推理（Llama-3.1-8B 可用单 A100/H100）；(3) PGD 自适应攻击需要嵌入模型梯度计算；(4) GPT-4o API 费用（限制实验范围控制成本）。总体 2-4 张 A100 即可完成所有实验。
  - 数据需求: 低。NQ、HotpotQA、MS-MARCO 均为公开标准数据集。PoisonedRAG 和 CorruptRAG 的攻击代码开源。
  - 人工介入: 低。无需人工标注。主要人工工作在理论推导（Lipschitz 上界证明）和实验调试。
  - 训练需求: 无。方法无需训练任何模型。仅需要嵌入模型和 LLM 的推理。
  - 新 Benchmark: 否。使用现有数据集和攻击方法。
  - 预估周期: 6-8 周。理论推导 1-2 周 + 核心实验 2-3 周 + 消融和泛化实验 2-3 周 + 论文写作 2 周（可与实验并行）。AAAI 2026 截稿时间充裕。
```

Sources:
- [LP-CP: Conformal Prediction under Lévy-Prokhorov Distribution Shifts](https://arxiv.org/abs/2502.14105)
- [TRAQ: Trustworthy Retrieval Augmented QA](https://arxiv.org/pdf/2307.04642)
- [Chen et al.: Is Conformal Factuality for RAG-based LLMs Robust?](https://arxiv.org/abs/2603.16817)
- [RobustRAG: Certifiably Robust RAG](https://arxiv.org/pdf/2405.15556)
- [ReliabilityRAG (NeurIPS 2025)](https://openreview.net/forum?id=D9JeNTs5Bu)
- [RAGDefender (ACSAC 2025)](https://kevinkoo001.github.io/assets/pdf/acsac25-ragdefender.pdf)
- [RPS: Provably Reliable CP under Poisoning (ICLR 2025)](https://openreview.net/forum?id=ofuLWn8DFZ)
- [PoisonedRAG (USENIX Security 2025)](https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag)
- [PASC: Pipeline-Aware Conformal Prediction](https://arxiv.org/abs/2605.18812)
- [OPSA: Enhancing Adversarial Robustness with CP](https://arxiv.org/html/2506.07804v1)
- [Response Quality Assessment for RAG via Conditional Conformal Factuality](https://arxiv.org/abs/2506.20978)
- [Conformal-RAG (SIGIR 2025)](https://arxiv.org/html/2506.20978)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fea1a8ed-8268-4a88-a948-e838e8687a09",
  "isSidechain": false,
  "requestId": "req_011CbYPb1VdYFsFjvwrG4u8U",
  "type": "assistant",
  "uuid": "4684894f-6b51-40d9-aaad-cf6adca330cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ZUhurUH8qFVVLeBYJb2PY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 712,
      "cache_read_input_tokens": 26194,
      "output_tokens": 6906,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 712,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6906,
          "cache_read_input_tokens": 26194,
          "cache_creation_input_tokens": 712,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 712
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

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Conformal Abstention for RAG under LP-Bounded Retrieval Shifts  ## Core Problem  How can a RAG system provide di…",
  "leafUuid": "4684894f-6b51-40d9-aaad-cf6adca330cf",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal abstention for RAG under adversarial retrieval shifts",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Conformal Abstention for RAG under LP-Bounded Retrieval Shifts  ## Core Problem  How can a RAG system provide di…",
  "leafUuid": "4684894f-6b51-40d9-aaad-cf6adca330cf",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal abstention for RAG under adversarial retrieval shifts",
  "sessionId": "e33840bd-e0ef-41a3-8869-05f690526764"
}
```

---
