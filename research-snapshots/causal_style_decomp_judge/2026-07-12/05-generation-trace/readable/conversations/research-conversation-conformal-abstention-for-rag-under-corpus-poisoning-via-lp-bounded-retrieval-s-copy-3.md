# Research conversation: Conformal Abstention for RAG under Corpus Poisoning via LP-Bounded Retrieval Shifts ## Core Problem How can a RAG system

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/84c13c55-366d-4c46-b901-0f44d11301b4.jsonl`
- **Structured JSON:** [`c6104f8c6bf068a582d1.json`](../../sessions/c6/c6104f8c6bf068a582d1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T07:23:05.515Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T07:23:05.515Z",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "content": "# Conformal Abstention for RAG under Corpus Poisoning via LP-Bounded Retrieval Shifts\n\n## Core Problem\n\nHow can a RAG system provide distribution-free, certified abstention guarantees on answer correctness when the retrieval corpus is adversarially poisoned — a setting where standard conformal prediction (TRAQ, C-RAG) breaks due to exchangeability violation, and existing certified defenses (RobustRAG, ReliabilityRAG) can only generate answers but cannot formally decide when to abstain?\n\n## Core Insight\n\nWe show that anchoring the nonconformity score at the retrieval-agreement level — rather than the answer-confidence level used by prior CP-for-RAG methods (TRAQ, C-RAG) — is what enables LP-CP's score propagation theorem to apply under adversarial retrieval corruption. The key reason: answer-level scores (e.g., LLM output probabilities) have uncontrollable Lipschitz constants with respect to input perturbations, making worst-case quantile propagation vacuous. Retrieval-level pairwise cosine similarity on normalized embeddings admits an analytically bounded Lipschitz constant, yielding non-trivial closed-form worst-case quantiles. This design choice simultaneously (1) directly probes the attack surface (poisoning acts on retrieval, not generation), (2) makes the method LLM-agnostic and composable with any downstream generator, and (3) enables the first certified abstention guarantee for adversarial RAG.\n\n## Research Opportunity\n\nThe intersection of {conformal prediction} ∩ {RAG} ∩ {adversarial robustness} is empty as of May 2026, verified across two RAG security surveys (arXiv:2603.21654, arXiv:2604.08304), the TACL CP-for-NLP survey, and 15+ targeted searches. Chen et al. (arXiv:2603.16817, Mar 2026) explicitly diagnosed that conformal factuality guarantees break under RAG distribution shift but proposed no solution. The Lévy-Prokhorov conformal prediction framework (LP-CP, NeurIPS 2025, arXiv:2502.14105) provides the exact mathematical decomposition — ρ for global contamination fraction, ε for local embedding perturbation — that maps onto corpus poisoning parameters. No concurrent work addresses this gap.\n\n## Research Landscape\n\n**CP for benign RAG.** TRAQ (NAACL 2024) provides end-to-end coverage via calibrated retrieval and answer sets. C-RAG (ICML 2024) certifies conformal generation risk bounds. Conformal-RAG (SIGIR 2025) offers group-conditional coverage for sub-claims. Principled Context Engineering for RAG (arXiv:2511.17908) uses CP for context filtering, reducing retained context by 2–3× while maintaining coverage — but only in benign settings. None handle adversarial retrieval.\n\n**Certified RAG defenses (answer-only, no abstention).** RobustRAG (SaTML 2026) achieves 26–36% certified robust accuracy on NQ via isolate-then-aggregate. ReliabilityRAG (NeurIPS 2025) uses graph-theoretic MIS with reliability-weighted documents under k′ ≤ k/5 poisoning budget. Both must produce an answer even under high uncertainty; neither offers formal abstention.\n\n**Heuristic RAG defenses.** RAGDefender (ACSAC 2025) achieves 0.18 ASR at 10× poisoning ratio via cosine-similarity clustering, finding poisoned docs cluster tightly (0.976 vs 0.309 cosine similarity). TrustRAG (arXiv:2501.00879) uses K-means clustering + cosine similarity for plug-and-play detection. RAGPart & RAGMask (arXiv:2512.24268) use document partitioning and token masking at retrieval stage, evaluated across four retrievers. These methods rely on heuristic thresholds — no coverage guarantees, no formal abstention decision, no robustness certificate parameterized by attack budget.\n\n**Poisoning-robust CP (non-RAG).** RPS (ICLR 2025 Spotlight) uses partition-and-vote with smoothed scores for calibration poisoning. LP-CP (NeurIPS 2025, arXiv:2502.14105) provides closed-form worst-case quantiles under Lévy-Prokhorov distribution shifts. Neither addresses test-time retrieval corruption in RAG.\n\n**Conformal abstention (non-adversarial).** Learning Conformal Abstention Policies (arXiv:2502.06884) integrates RL with CP for adaptive abstention in LLMs/VLMs but relies on training and does not handle adversarial settings. Selective Conformal Risk Control (arXiv:2512.12844) integrates CP with selective classification but not in RAG or adversarial contexts.\n\n**Attack landscape.** PoisonedRAG (USENIX Security 2025) achieves 97% ASR via multi-document injection. CorruptRAG (arXiv:2504.03957) demonstrates high ASR with single-document injection (ρ→0), representing the most practical and stealthy attack regime. Benchmarking Poisoning Attacks against RAG (arXiv:2505.18543) provides a unified evaluation framework across 5 datasets, 13 attacks, and 7 defenses.\n\n**Critical gap.** No existing method provides distribution-free, certified abstention for RAG under adversarial retrieval corruption parameterized by attack budget.\n\n## Proposed Approach\n\n**LP-RAG-Abstain** provides distribution-free certified abstention for RAG under adversarial corpus poisoning.\n\n**Threat model.** Attacker injects poisoned documents into the corpus. Defense assumes upper bounds (ρ₀, ε₀) on: ρ = fraction of poisoned documents in top-k retrieval, ε = maximum embedding perturbation per poisoned document. These are defense input parameters (analogous to RobustRAG's k′ ≤ k/5), not quantities to estimate. Guarantees are conditional: valid whenever the actual attack falls within (ρ₀, ε₀).\n\n**Score design.** Define retrieval-agreement nonconformity score s(q) from pairwise cosine similarities among top-k retrieved passages for query q. For normalized embeddings on the unit sphere, cosine similarity is Lipschitz-continuous with analytically bounded constant. The aggregate score (mean pairwise similarity) inherits a Lipschitz constant of O(2/k) with respect to single-document replacement, enabling LP-CP's propagation theorem to yield closed-form worst-case quantiles that are non-vacuous for practical (ρ, ε) ranges.\n\n**Lipschitz tightness.** The practical utility of LP-RAG-Abstain depends on the Lipschitz constant being small enough that worst-case quantile shifts remain manageable. We will: (1) derive the analytic Lipschitz upper bound for the proposed score, (2) empirically estimate the constant on real embedding data to verify tightness, (3) report the gap between certified coverage and empirical coverage to quantify conservatism, and (4) if necessary, explore Lipschitz-regularized score designs (cf. Efficient Robust CP via Lipschitz-Bounded Networks, arXiv:2506.05434).\n\n**Abstention rule.** Map (ρ₀, ε₀) to LP ambiguity set. Compute worst-case conformal quantile via LP-CP's closed-form expression. Abstain when prediction set is empty under worst-case quantile. Guarantee: P(correct ∈ set ∨ abstain) ≥ 1−α.\n\n**Adversary-budget monotonicity.** LP-RAG-Abstain exhibits a favorable theoretical property: certified coverage improves as attacker budget (ρ, ε) decreases, with the tightest guarantees (lowest abstention rate, smallest prediction sets) at the most practical attack regime — single/few-document poisoning (CorruptRAG, arXiv:2504.03957). This contrasts with isolate-then-aggregate methods (RobustRAG) whose partitioning overhead is constant regardless of attack strength.\n\n**Why not just threshold on clustering scores?** Heuristic detection methods (RAGDefender, TrustRAG) use cosine similarity clustering with tuned thresholds. LP-RAG-Abstain provides three advantages: (1) distribution-free finite-sample coverage guarantee vs. no statistical guarantee; (2) guarantees parameterized by attack budget (ρ, ε) — users declare threat tolerance, system adapts automatically; (3) no threshold tuning or dataset-specific calibration beyond standard CP calibration set.\n\n**\"Safe Silence\" guarantee.** Unlike answer-only defenses (RobustRAG, ReliabilityRAG) that must produce output even under high uncertainty, LP-RAG-Abstain formally guarantees: \"either I return a set containing the correct answer, or I explicitly abstain.\" In safety-critical RAG applications (medical, legal, financial), confidently wrong answers are far more harmful than acknowledged uncertainty. This directly addresses the \"robustness + usefulness\" desiderata identified by Chen et al. (arXiv:2603.16817).\n\n## Experimental Design\n\n**Datasets.** NQ, HotpotQA, MS-MARCO — covering Wikipedia-based and web-passage corpora.\n\n**Attacks.** PoisonedRAG (multi-document, USENIX Security 2025), CorruptRAG (single-document, arXiv:2504.03957).\n\n**Embedding models.** Qwen3-Embedding-8B (primary), BGE-large, Contriever — testing generalization across embedding architectures and dimensionalities. Report empirical Lipschitz constant for each.\n\n**Generator LLMs.** Llama-3.1-8B (open-source) and GPT-4o (closed-source) — testing across LLM vulnerability profiles.\n\n**Baselines.**\n- No-defense vanilla RAG (lower bound)\n- TRAQ (NAACL 2024): CP without adversarial awareness — demonstrate coverage breakdown under attack\n- RobustRAG (SaTML 2026): certified answer-only defense\n- ReliabilityRAG (NeurIPS 2025): certified answer-only defense (stronger)\n- RAGDefender (ACSAC 2025): heuristic detection\n- Naive selective prediction: LLM confidence threshold abstention\n- LP-RAG-Abstain (proposed)\n\n**Evaluation metrics.**\n- Coverage (poisoned): P(correct ∈ set ∨ abstain) — core guarantee\n- Coverage (clean): P(correct ∈ set) without poisoning — should ≥ 1−α\n- Abstention rate (poisoned vs. clean)\n- Certified robust accuracy on non-abstained queries (EM and F1)\n- Prediction set size (mean/median)\n- Accuracy-abstention tradeoff AUC (varying α)\n- Wall-clock inference time per query\n- LLM API call count per query\n\n**Ablation studies.**\n1. ρ sensitivity: fix ε, vary ρ ∈ {0, 0.05, 0.1, 0.2, 0.4} — certified accuracy and abstention rate curves\n2. ε sensitivity: fix ρ, vary ε — LP bound tightness\n3. Score function: pairwise cosine agreement (proposed) vs. average retrieval score vs. answer entropy\n4. k sensitivity: k ∈ {5, 10, 20, 50} — effect on retrieval-agreement score\n5. α sweep: α ∈ {0.01, 0.05, 0.10, 0.20} — coverage-abstention tradeoff\n6. Calibration set size: {100, 300, 500, 1000, 2000} — sample efficiency\n7. LP-CP vs. Bonferroni correction: demonstrate tightness advantage of closed-form quantile\n\n**(ρ, ε) heatmap.** Jointly vary (ρ, ε) and plot certified accuracy and abstention rate as 2D heatmaps, enabling users to select operating points matching their threat assumptions.\n\n**Adaptive attack evaluation.** Design adversary with full knowledge of the defense (pairwise cosine agreement score), attempting to maximize embedding distance among poisoned documents within ε constraint. Verify coverage guarantee still holds. Compare with RobustRAG's adaptive attack results.\n\n**Targets.** Exceed RobustRAG's 26–36% certified robust accuracy; maintain >90% clean coverage; achieve <15% clean abstention rate.\n\n## Key References\n\n- TRAQ: Trustworthy Retrieval Augmented QA via Conformal Prediction (NAACL 2024)\n- C-RAG: Certified Generation Risks for RAG (ICML 2024)\n- Response Quality Assessment for RAG via Conditional Conformal Factuality [Conformal-RAG] (SIGIR 2025)\n- Certifiably Robust RAG against Retrieval Corruption [RobustRAG] (SaTML 2026)\n- ReliabilityRAG: Provably Robust Defense for RAG-based Web-Search (NeurIPS 2025)\n- PoisonedRAG: Knowledge Corruption Attacks to RAG of LLMs (USENIX Security 2025)\n- CorruptRAG: Practical Poisoning Attacks against RAG (arXiv:2504.03957)\n- Conformal Prediction under Lévy-Prokhorov Distribution Shifts [LP-CP] (NeurIPS 2025, arXiv:2502.14105)\n- Provably Reliable Conformal Prediction Sets under Data Poisoning [RPS] (ICLR 2025 Spotlight)\n- Rescuing the Unpoisoned [RAGDefender] (ACSAC 2025)\n- TrustRAG: Enhancing Robustness and Trustworthiness in RAG (arXiv:2501.00879)\n- RAGPart & RAGMask: Retrieval-Stage Defenses (arXiv:2512.24268)\n- Is Conformal Factuality for RAG-based LLMs Robust? (arXiv:2603.16817, 2026)\n- RAG security surveys (arXiv:2603.21654, arXiv:2604.08304)\n- TACL CP-for-NLP survey\n- Principled Context Engineering for RAG (arXiv:2511.17908)\n- Learning Conformal Abstention Policies (arXiv:2502.06884)\n- Selective Conformal Risk Control (arXiv:2512.12844)\n- Benchmarking Poisoning Attacks against RAG (arXiv:2505.18543)"
}
```

---

### Runtime record

_source line 2 · 2026-05-30T07:23:05.528Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T07:23:05.528Z",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4"
}
```

---

## Round 1

46 recorded events

### User

_source line 3 · 2026-05-30T07:23:05.665Z_

# Conformal Abstention for RAG under Corpus Poisoning via LP-Bounded Retrieval Shifts

## Core Problem

How can a RAG system provide distribution-free, certified abstention guarantees on answer correctness when the retrieval corpus is adversarially poisoned — a setting where standard conformal prediction (TRAQ, C-RAG) breaks due to exchangeability violation, and existing certified defenses (RobustRAG, ReliabilityRAG) can only generate answers but cannot formally decide when to abstain?

## Core Insight

We show that anchoring the nonconformity score at the retrieval-agreement level — rather than the answer-confidence level used by prior CP-for-RAG methods (TRAQ, C-RAG) — is what enables LP-CP's score propagation theorem to apply under adversarial retrieval corruption. The key reason: answer-level scores (e.g., LLM output probabilities) have uncontrollable Lipschitz constants with respect to input perturbations, making worst-case quantile propagation vacuous. Retrieval-level pairwise cosine similarity on normalized embeddings admits an analytically bounded Lipschitz constant, yielding non-trivial closed-form worst-case quantiles. This design choice simultaneously (1) directly probes the attack surface (poisoning acts on retrieval, not generation), (2) makes the method LLM-agnostic and composable with any downstream generator, and (3) enables the first certified abstention guarantee for adversarial RAG.

## Research Opportunity

The intersection of {conformal prediction} ∩ {RAG} ∩ {adversarial robustness} is empty as of May 2026, verified across two RAG security surveys (arXiv:2603.21654, arXiv:2604.08304), the TACL CP-for-NLP survey, and 15+ targeted searches. Chen et al. (arXiv:2603.16817, Mar 2026) explicitly diagnosed that conformal factuality guarantees break under RAG distribution shift but proposed no solution. The Lévy-Prokhorov conformal prediction framework (LP-CP, NeurIPS 2025, arXiv:2502.14105) provides the exact mathematical decomposition — ρ for global contamination fraction, ε for local embedding perturbation — that maps onto corpus poisoning parameters. No concurrent work addresses this gap.

## Research Landscape

**CP for benign RAG.** TRAQ (NAACL 2024) provides end-to-end coverage via calibrated retrieval and answer sets. C-RAG (ICML 2024) certifies conformal generation risk bounds. Conformal-RAG (SIGIR 2025) offers group-conditional coverage for sub-claims. Principled Context Engineering for RAG (arXiv:2511.17908) uses CP for context filtering, reducing retained context by 2–3× while maintaining coverage — but only in benign settings. None handle adversarial retrieval.

**Certified RAG defenses (answer-only, no abstention).** RobustRAG (SaTML 2026) achieves 26–36% certified robust accuracy on NQ via isolate-then-aggregate. ReliabilityRAG (NeurIPS 2025) uses graph-theoretic MIS with reliability-weighted documents under k′ ≤ k/5 poisoning budget. Both must produce an answer even under high uncertainty; neither offers formal abstention.

**Heuristic RAG defenses.** RAGDefender (ACSAC 2025) achieves 0.18 ASR at 10× poisoning ratio via cosine-similarity clustering, finding poisoned docs cluster tightly (0.976 vs 0.309 cosine similarity). TrustRAG (arXiv:2501.00879) uses K-means clustering + cosine similarity for plug-and-play detection. RAGPart & RAGMask (arXiv:2512.24268) use document partitioning and token masking at retrieval stage, evaluated across four retrievers. These methods rely on heuristic thresholds — no coverage guarantees, no formal abstention decision, no robustness certificate parameterized by attack budget.

**Poisoning-robust CP (non-RAG).** RPS (ICLR 2025 Spotlight) uses partition-and-vote with smoothed scores for calibration poisoning. LP-CP (NeurIPS 2025, arXiv:2502.14105) provides closed-form worst-case quantiles under Lévy-Prokhorov distribution shifts. Neither addresses test-time retrieval corruption in RAG.

**Conformal abstention (non-adversarial).** Learning Conformal Abstention Policies (arXiv:2502.06884) integrates RL with CP for adaptive abstention in LLMs/VLMs but relies on training and does not handle adversarial settings. Selective Conformal Risk Control (arXiv:2512.12844) integrates CP with selective classification but not in RAG or adversarial contexts.

**Attack landscape.** PoisonedRAG (USENIX Security 2025) achieves 97% ASR via multi-document injection. CorruptRAG (arXiv:2504.03957) demonstrates high ASR with single-document injection (ρ→0), representing the most practical and stealthy attack regime. Benchmarking Poisoning Attacks against RAG (arXiv:2505.18543) provides a unified evaluation framework across 5 datasets, 13 attacks, and 7 defenses.

**Critical gap.** No existing method provides distribution-free, certified abstention for RAG under adversarial retrieval corruption parameterized by attack budget.

## Proposed Approach

**LP-RAG-Abstain** provides distribution-free certified abstention for RAG under adversarial corpus poisoning.

**Threat model.** Attacker injects poisoned documents into the corpus. Defense assumes upper bounds (ρ₀, ε₀) on: ρ = fraction of poisoned documents in top-k retrieval, ε = maximum embedding perturbation per poisoned document. These are defense input parameters (analogous to RobustRAG's k′ ≤ k/5), not quantities to estimate. Guarantees are conditional: valid whenever the actual attack falls within (ρ₀, ε₀).

**Score design.** Define retrieval-agreement nonconformity score s(q) from pairwise cosine similarities among top-k retrieved passages for query q. For normalized embeddings on the unit sphere, cosine similarity is Lipschitz-continuous with analytically bounded constant. The aggregate score (mean pairwise similarity) inherits a Lipschitz constant of O(2/k) with respect to single-document replacement, enabling LP-CP's propagation theorem to yield closed-form worst-case quantiles that are non-vacuous for practical (ρ, ε) ranges.

**Lipschitz tightness.** The practical utility of LP-RAG-Abstain depends on the Lipschitz constant being small enough that worst-case quantile shifts remain manageable. We will: (1) derive the analytic Lipschitz upper bound for the proposed score, (2) empirically estimate the constant on real embedding data to verify tightness, (3) report the gap between certified coverage and empirical coverage to quantify conservatism, and (4) if necessary, explore Lipschitz-regularized score designs (cf. Efficient Robust CP via Lipschitz-Bounded Networks, arXiv:2506.05434).

**Abstention rule.** Map (ρ₀, ε₀) to LP ambiguity set. Compute worst-case conformal quantile via LP-CP's closed-form expression. Abstain when prediction set is empty under worst-case quantile. Guarantee: P(correct ∈ set ∨ abstain) ≥ 1−α.

**Adversary-budget monotonicity.** LP-RAG-Abstain exhibits a favorable theoretical property: certified coverage improves as attacker budget (ρ, ε) decreases, with the tightest guarantees (lowest abstention rate, smallest prediction sets) at the most practical attack regime — single/few-document poisoning (CorruptRAG, arXiv:2504.03957). This contrasts with isolate-then-aggregate methods (RobustRAG) whose partitioning overhead is constant regardless of attack strength.

**Why not just threshold on clustering scores?** Heuristic detection methods (RAGDefender, TrustRAG) use cosine similarity clustering with tuned thresholds. LP-RAG-Abstain provides three advantages: (1) distribution-free finite-sample coverage guarantee vs. no statistical guarantee; (2) guarantees parameterized by attack budget (ρ, ε) — users declare threat tolerance, system adapts automatically; (3) no threshold tuning or dataset-specific calibration beyond standard CP calibration set.

**"Safe Silence" guarantee.** Unlike answer-only defenses (RobustRAG, ReliabilityRAG) that must produce output even under high uncertainty, LP-RAG-Abstain formally guarantees: "either I return a set containing the correct answer, or I explicitly abstain." In safety-critical RAG applications (medical, legal, financial), confidently wrong answers are far more harmful than acknowledged uncertainty. This directly addresses the "robustness + usefulness" desiderata identified by Chen et al. (arXiv:2603.16817).

## Experimental Design

**Datasets.** NQ, HotpotQA, MS-MARCO — covering Wikipedia-based and web-passage corpora.

**Attacks.** PoisonedRAG (multi-document, USENIX Security 2025), CorruptRAG (single-document, arXiv:2504.03957).

**Embedding models.** Qwen3-Embedding-8B (primary), BGE-large, Contriever — testing generalization across embedding architectures and dimensionalities. Report empirical Lipschitz constant for each.

**Generator LLMs.** Llama-3.1-8B (open-source) and GPT-4o (closed-source) — testing across LLM vulnerability profiles.

**Baselines.**
- No-defense vanilla RAG (lower bound)
- TRAQ (NAACL 2024): CP without adversarial awareness — demonstrate coverage breakdown under attack
- RobustRAG (SaTML 2026): certified answer-only defense
- ReliabilityRAG (NeurIPS 2025): certified answer-only defense (stronger)
- RAGDefender (ACSAC 2025): heuristic detection
- Naive selective prediction: LLM confidence threshold abstention
- LP-RAG-Abstain (proposed)

**Evaluation metrics.**
- Coverage (poisoned): P(correct ∈ set ∨ abstain) — core guarantee
- Coverage (clean): P(correct ∈ set) without poisoning — should ≥ 1−α
- Abstention rate (poisoned vs. clean)
- Certified robust accuracy on non-abstained queries (EM and F1)
- Prediction set size (mean/median)
- Accuracy-abstention tradeoff AUC (varying α)
- Wall-clock inference time per query
- LLM API call count per query

**Ablation studies.**
1. ρ sensitivity: fix ε, vary ρ ∈ {0, 0.05, 0.1, 0.2, 0.4} — certified accuracy and abstention rate curves
2. ε sensitivity: fix ρ, vary ε — LP bound tightness
3. Score function: pairwise cosine agreement (proposed) vs. average retrieval score vs. answer entropy
4. k sensitivity: k ∈ {5, 10, 20, 50} — effect on retrieval-agreement score
5. α sweep: α ∈ {0.01, 0.05, 0.10, 0.20} — coverage-abstention tradeoff
6. Calibration set size: {100, 300, 500, 1000, 2000} — sample efficiency
7. LP-CP vs. Bonferroni correction: demonstrate tightness advantage of closed-form quantile

**(ρ, ε) heatmap.** Jointly vary (ρ, ε) and plot certified accuracy and abstention rate as 2D heatmaps, enabling users to select operating points matching their threat assumptions.

**Adaptive attack evaluation.** Design adversary with full knowledge of the defense (pairwise cosine agreement score), attempting to maximize embedding distance among poisoned documents within ε constraint. Verify coverage guarantee still holds. Compare with RobustRAG's adaptive attack results.

**Targets.** Exceed RobustRAG's 26–36% certified robust accuracy; maintain >90% clean coverage; achieve <15% clean abstention rate.

## Key References

- TRAQ: Trustworthy Retrieval Augmented QA via Conformal Prediction (NAACL 2024)
- C-RAG: Certified Generation Risks for RAG (ICML 2024)
- Response Quality Assessment for RAG via Conditional Conformal Factuality [Conformal-RAG] (SIGIR 2025)
- Certifiably Robust RAG against Retrieval Corruption [RobustRAG] (SaTML 2026)
- ReliabilityRAG: Provably Robust Defense for RAG-based Web-Search (NeurIPS 2025)
- PoisonedRAG: Knowledge Corruption Attacks to RAG of LLMs (USENIX Security 2025)
- CorruptRAG: Practical Poisoning Attacks against RAG (arXiv:2504.03957)
- Conformal Prediction under Lévy-Prokhorov Distribution Shifts [LP-CP] (NeurIPS 2025, arXiv:2502.14105)
- Provably Reliable Conformal Prediction Sets under Data Poisoning [RPS] (ICLR 2025 Spotlight)
- Rescuing the Unpoisoned [RAGDefender] (ACSAC 2025)
- TrustRAG: Enhancing Robustness and Trustworthiness in RAG (arXiv:2501.00879)
- RAGPart & RAGMask: Retrieval-Stage Defenses (arXiv:2512.24268)
- Is Conformal Factuality for RAG-based LLMs Robust? (arXiv:2603.16817, 2026)
- RAG security surveys (arXiv:2603.21654, arXiv:2604.08304)
- TACL CP-for-NLP survey
- Principled Context Engineering for RAG (arXiv:2511.17908)
- Learning Conformal Abstention Policies (arXiv:2502.06884)
- Selective Conformal Risk Control (arXiv:2512.12844)
- Benchmarking Poisoning Attacks against RAG (arXiv:2505.18543)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a45afd59-6eac-4f72-8319-52cc86d3dd24",
  "type": "user",
  "uuid": "c5ea61e8-34e7-4f57-b55e-3ab6f75ffb6e",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T07:23:05.664Z_

```json
{
  "parentUuid": "c5ea61e8-34e7-4f57-b55e-3ab6f75ffb6e",
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
  "uuid": "4a1650fc-a832-460e-a89f-3de83fb35982",
  "timestamp": "2026-05-30T07:23:05.664Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T07:23:05.664Z_

```json
{
  "parentUuid": "4a1650fc-a832-460e-a89f-3de83fb35982",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ff039def-6084-4a13-aa8a-18b59c7bae48",
  "timestamp": "2026-05-30T07:23:05.664Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
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
  "aiTitle": "Conformal abstention for poisoned RAG systems",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4"
}
```

---

### Assistant

_source line 7 · 2026-05-30T07:23:14.634Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to act as the "补救 agent" (remediation agent) to review this proposal for AAAI 2026 submission. My job is to focus exclusively on experimental design and technical execution — baselines, evaluation metrics, ablation studies, feasibility, and compute fairness. I must NOT touch novelty, significance, or framing.

Let me first do the required pre-research using WebSearch to understand current experimental standards in this area before giving any suggestions.

Let me search for:
1. Recent papers on conformal prediction for RAG - how they design experiments
2. RobustRAG and ReliabilityRAG experimental setups


3. LP-CP experimental evaluation
4. Poisoning attack evaluation standards
5. Current best practices for evaluating abstention/selective prediction

I'll start with these targeted searches to ground my feedback in what the community is actually doing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff039def-6084-4a13-aa8a-18b59c7bae48",
  "isSidechain": false,
  "requestId": "req_011CbYMNLSKQYcFEnT2mvaSG",
  "type": "assistant",
  "uuid": "2abcc729-0d97-4caf-9ad0-4f1716125657",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AkudPTV3Wpr7CpYszRDqYP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4970,
      "cache_read_input_tokens": 14080,
      "output_tokens": 308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4970,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 308,
          "cache_read_input_tokens": 14080,
          "cache_creation_input_tokens": 4970,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4970
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

_source line 8 · 2026-05-30T07:23:14.648Z_

I'll start by conducting the required pre-research to understand current experimental standards in this area before giving any recommendations. Let me run several targeted searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2abcc729-0d97-4caf-9ad0-4f1716125657",
  "isSidechain": false,
  "requestId": "req_011CbYMNLSKQYcFEnT2mvaSG",
  "type": "assistant",
  "uuid": "2a99194b-1701-4215-8aab-f808676f029c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AkudPTV3Wpr7CpYszRDqYP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4970,
      "cache_read_input_tokens": 14080,
      "output_tokens": 308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4970,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 308,
          "cache_read_input_tokens": 14080,
          "cache_creation_input_tokens": 4970,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4970
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

_source line 9 · 2026-05-30T07:23:15.231Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LYinR4okpbYt5f2PpR9TYT`</summary>

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
  "parentUuid": "2a99194b-1701-4215-8aab-f808676f029c",
  "isSidechain": false,
  "requestId": "req_011CbYMNLSKQYcFEnT2mvaSG",
  "type": "assistant",
  "uuid": "44f67781-a50c-46b6-98d9-50d130e6471d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AkudPTV3Wpr7CpYszRDqYP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4970,
      "cache_read_input_tokens": 14080,
      "output_tokens": 308,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4970,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 308,
          "cache_read_input_tokens": 14080,
          "cache_creation_input_tokens": 4970,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4970
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

_source line 10 · 2026-05-30T07:23:15.239Z_

<details><summary>↩ Tool result · `toolu_01LYinR4okpbYt5f2PpR9TYT`</summary>

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
  "parentUuid": "44f67781-a50c-46b6-98d9-50d130e6471d",
  "isSidechain": false,
  "promptId": "a45afd59-6eac-4f72-8319-52cc86d3dd24",
  "type": "user",
  "uuid": "ad8bbf5e-f8ca-49d6-bea6-f66122ebd0f5",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "44f67781-a50c-46b6-98d9-50d130e6471d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
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
  "lastPrompt": "# Conformal Abstention for RAG under Corpus Poisoning via LP-Bounded Retrieval Shifts  ## Core Problem  How can a RAG system provide distribution-free, certified abstention guarantees on answer correc…",
  "leafUuid": "ad8bbf5e-f8ca-49d6-bea6-f66122ebd0f5",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal abstention for poisoned RAG systems",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4"
}
```

---

### Assistant

_source line 13 · 2026-05-30T07:23:17.694Z_

Now let me run multiple targeted searches in parallel to understand the experimental standards in this area.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad8bbf5e-f8ca-49d6-bea6-f66122ebd0f5",
  "isSidechain": false,
  "requestId": "req_011CbYMP3XMNXRuFPt56LGJP",
  "type": "assistant",
  "uuid": "f470b3bd-09aa-4ad4-9111-ddab7d67356e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q9Hyne7uf92oeTxGEy5hsL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 836,
      "cache_read_input_tokens": 19050,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 836,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 92,
          "cache_read_input_tokens": 19050,
          "cache_creation_input_tokens": 836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 836
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

_source line 14 · 2026-05-30T07:23:18.254Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012qBnHyyD44LmcwJDpvtaaP`</summary>

```json
{
  "query": "RobustRAG SaTML 2026 experimental setup baselines evaluation metrics certified robust accuracy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f470b3bd-09aa-4ad4-9111-ddab7d67356e",
  "isSidechain": false,
  "requestId": "req_011CbYMP3XMNXRuFPt56LGJP",
  "type": "assistant",
  "uuid": "456d993f-966c-48a3-84ca-565ea89ac72a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q9Hyne7uf92oeTxGEy5hsL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 836,
      "cache_read_input_tokens": 19050,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 836,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 92,
          "cache_read_input_tokens": 19050,
          "cache_creation_input_tokens": 836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 836
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

_source line 15 · 2026-05-30T07:23:25.263Z_

<details><summary>↩ Tool result · `toolu_012qBnHyyD44LmcwJDpvtaaP`</summary>

```text
Web search results for query: "RobustRAG SaTML 2026 experimental setup baselines evaluation metrics certified robust accuracy"

Links: [{"title":"IEEE SaTML 2026 · Program","url":"https://satml.org/program/"},{"title":"IEEE SaTML 2026 · Accepted Papers","url":"https://satml.org/accepted-papers/"},{"title":"This is the preprint of the work has been accepted for publication at the IEEE Conference on Secure and Trustworthy Machine Learning (SaTML 2026). Cascading Robustness Verification: Toward Efficient Model‑Agnostic Certification","url":"https://arxiv.org/html/2602.04236"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/html/2405.15556"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/pdf/2405.15556"},{"title":"[2405.15556] Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/abs/2405.15556"},{"title":"How to Evaluate RAG Systems Accurately: Metrics, Benchmarks & Frameworks in 2026","url":"https://nandigamharikrishna.substack.com/p/how-to-evaluate-rag-systems-accurately"}]

Based on the search results, here's information about RobustRAG's experimental setup, baselines, evaluation metrics, and certified robust accuracy:

## Overview
RobustRAG is a defense framework that addresses retrieval-augmented generation (RAG) susceptibility to retrieval corruption attacks, where malicious passages injected into retrieval results can lead to inaccurate model responses, proposing the first defense framework with certifiable robustness against such attacks.

## Experimental Setup
The evaluation was conducted using three datasets (RealtimeQA, Natural Questions, and Biography Generation) and three LLMs (Mistral-7B, Llama-2-7B, and GPT-3.5).

## Core Approach
The key insight of RobustRAG is an isolate-then-aggregate strategy: passages are isolated into disjoint groups, LLM responses are generated based on the concatenated passages from each isolated group, and then responses are securely aggregated for a robust output. The framework designs keyword-based and decoding-based algorithms for securely aggregating responses.

## Evaluation Metrics and Results
RobustRAG achieves certifiable robustness by formally certifying non-trivial lower bounds on response quality—even against an adaptive attacker with full knowledge of the defense and the ability to arbitrarily inject a bounded number of malicious passages.

On the RealtimeQA dataset, RobustRAG achieves 71% clean accuracy and 38% certifiable robust accuracy, compared to 69% clean accuracy and no certifiable accuracy for vanilla approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "456d993f-966c-48a3-84ca-565ea89ac72a",
  "isSidechain": false,
  "promptId": "a45afd59-6eac-4f72-8319-52cc86d3dd24",
  "type": "user",
  "uuid": "ae0b320d-0c16-4778-866a-a55b5b596a93",
  "toolUseResult": {
    "query": "RobustRAG SaTML 2026 experimental setup baselines evaluation metrics certified robust accuracy",
    "results": [
      {
        "tool_use_id": "srvtoolu_014MHihhNuKBcVecZ1d6UcWC",
        "content": [
          {
            "title": "IEEE SaTML 2026 · Program",
            "url": "https://satml.org/program/"
          },
          {
            "title": "IEEE SaTML 2026 · Accepted Papers",
            "url": "https://satml.org/accepted-papers/"
          },
          {
            "title": "This is the preprint of the work has been accepted for publication at the IEEE Conference on Secure and Trustworthy Machine Learning (SaTML 2026). Cascading Robustness Verification: Toward Efficient Model‑Agnostic Certification",
            "url": "https://arxiv.org/html/2602.04236"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://arxiv.org/html/2405.15556"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://arxiv.org/pdf/2405.15556"
          },
          {
            "title": "[2405.15556] Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://arxiv.org/abs/2405.15556"
          },
          {
            "title": "How to Evaluate RAG Systems Accurately: Metrics, Benchmarks & Frameworks in 2026",
            "url": "https://nandigamharikrishna.substack.com/p/how-to-evaluate-rag-systems-accurately"
          }
        ]
      },
      "Based on the search results, here's information about RobustRAG's experimental setup, baselines, evaluation metrics, and certified robust accuracy:\n\n## Overview\nRobustRAG is a defense framework that addresses retrieval-augmented generation (RAG) susceptibility to retrieval corruption attacks, where malicious passages injected into retrieval results can lead to inaccurate model responses, proposing the first defense framework with certifiable robustness against such attacks.\n\n## Experimental Setup\nThe evaluation was conducted using three datasets (RealtimeQA, Natural Questions, and Biography Generation) and three LLMs (Mistral-7B, Llama-2-7B, and GPT-3.5).\n\n## Core Approach\nThe key insight of RobustRAG is an isolate-then-aggregate strategy: passages are isolated into disjoint groups, LLM responses are generated based on the concatenated passages from each isolated group, and then responses are securely aggregated for a robust output. The framework designs keyword-based and decoding-based algorithms for securely aggregating responses.\n\n## Evaluation Metrics and Results\nRobustRAG achieves certifiable robustness by formally certifying non-trivial lower bounds on response quality—even against an adaptive attacker with full knowledge of the defense and the ability to arbitrarily inject a bounded number of malicious passages.\n\nOn the RealtimeQA dataset, RobustRAG achieves 71% clean accuracy and 38% certifiable robust accuracy, compared to 69% clean accuracy and no certifiable accuracy for vanilla approaches."
    ],
    "durationSeconds": 7.0040074139999975,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "456d993f-966c-48a3-84ca-565ea89ac72a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-30T07:23:27.589Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QFWY3DiFK9woKZDZYi36Fq`</summary>

```json
{
  "query": "ReliabilityRAG NeurIPS 2025 provably robust defense experimental evaluation datasets baselines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae0b320d-0c16-4778-866a-a55b5b596a93",
  "isSidechain": false,
  "requestId": "req_011CbYMPn6Sfeeq1p9cBWNjr",
  "type": "assistant",
  "uuid": "a33cf7ac-4ac2-409c-acea-1b0879327c55",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UNG4T9AyMZHuR3dFRR1tr2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 816,
      "cache_read_input_tokens": 19886,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 816,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 19886,
          "cache_creation_input_tokens": 816,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 816
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

_source line 17 · 2026-05-30T07:23:36.152Z_

<details><summary>↩ Tool result · `toolu_01QFWY3DiFK9woKZDZYi36Fq`</summary>

```text
Web search results for query: "ReliabilityRAG NeurIPS 2025 provably robust defense experimental evaluation datasets baselines"

Links: [{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/pdf/2509.23519"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search | OpenReview","url":"https://openreview.net/forum?id=D9JeNTs5Bu"},{"title":"NeurIPS Poster ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://neurips.cc/virtual/2025/poster/119236"},{"title":"[2509.23519] ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/abs/2509.23519"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://neurips.cc/media/neurips-2025/Slides/119236.pdf"},{"title":"RAGShield: Provenance-Verified Defense-in-Depth Against Knowledge Base Poisoning in Government Retrieval-Augmented Generation Systems","url":"https://arxiv.org/html/2604.00387v1"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG- ...","url":"https://www.semanticscholar.org/paper/ReliabilityRAG:-Effective-and-Provably-Robust-for-Shen-Imana/80c7921964f622abe6c023a2df5d5a824f9c66d9"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/pdf/2405.15556"}]

Based on the search results, here's information about ReliabilityRAG at NeurIPS 2025:

## Overview
ReliabilityRAG was published at NeurIPS 2025 as a paper on adversarial robustness for Retrieval-Augmented Generation (RAG) systems.

## Core Approach
ReliabilityRAG introduces a framework for adversarial robustness that explicitly leverages reliability information of retrieved documents, adopting a graph-theoretic perspective to identify a "consistent majority" among retrieved documents to filter out malicious ones. The approach is based on finding a Maximum Independent Set (MIS) on a document graph where edges encode contradiction, and the MIS variant explicitly prioritizes higher-reliability documents and provides provable robustness guarantees against bounded adversarial corruption under natural assumptions.

## Scalability
To address the computational cost of exact MIS for large retrieval sets, the work includes a scalable weighted sample and aggregate framework that explicitly utilizes reliability information while efficiently handling many documents.

## Experimental Results
ReliabilityRAG provides superior robustness against adversarial attacks compared to prior methods, maintains high benign accuracy, and excels in long-form generation tasks where prior robustness-focused methods struggled.

The paper is available on arXiv (2509.23519) and the OpenReview platform as a NeurIPS 2025 poster presentation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a33cf7ac-4ac2-409c-acea-1b0879327c55",
  "isSidechain": false,
  "promptId": "a45afd59-6eac-4f72-8319-52cc86d3dd24",
  "type": "user",
  "uuid": "283f18d3-598d-47da-bc40-3a51654f7c88",
  "toolUseResult": {
    "query": "ReliabilityRAG NeurIPS 2025 provably robust defense experimental evaluation datasets baselines",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SqYxj2aZhNi1xQQeY9EPyL",
        "content": [
          {
            "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://arxiv.org/pdf/2509.23519"
          },
          {
            "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search | OpenReview",
            "url": "https://openreview.net/forum?id=D9JeNTs5Bu"
          },
          {
            "title": "NeurIPS Poster ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://neurips.cc/virtual/2025/poster/119236"
          },
          {
            "title": "[2509.23519] ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://arxiv.org/abs/2509.23519"
          },
          {
            "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://neurips.cc/media/neurips-2025/Slides/119236.pdf"
          },
          {
            "title": "RAGShield: Provenance-Verified Defense-in-Depth Against Knowledge Base Poisoning in Government Retrieval-Augmented Generation Systems",
            "url": "https://arxiv.org/html/2604.00387v1"
          },
          {
            "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG- ...",
            "url": "https://www.semanticscholar.org/paper/ReliabilityRAG:-Effective-and-Provably-Robust-for-Shen-Imana/80c7921964f622abe6c023a2df5d5a824f9c66d9"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://arxiv.org/pdf/2405.15556"
          }
        ]
      },
      "Based on the search results, here's information about ReliabilityRAG at NeurIPS 2025:\n\n## Overview\nReliabilityRAG was published at NeurIPS 2025 as a paper on adversarial robustness for Retrieval-Augmented Generation (RAG) systems.\n\n## Core Approach\nReliabilityRAG introduces a framework for adversarial robustness that explicitly leverages reliability information of retrieved documents, adopting a graph-theoretic perspective to identify a \"consistent majority\" among retrieved documents to filter out malicious ones. The approach is based on finding a Maximum Independent Set (MIS) on a document graph where edges encode contradiction, and the MIS variant explicitly prioritizes higher-reliability documents and provides provable robustness guarantees against bounded adversarial corruption under natural assumptions.\n\n## Scalability\nTo address the computational cost of exact MIS for large retrieval sets, the work includes a scalable weighted sample and aggregate framework that explicitly utilizes reliability information while efficiently handling many documents.\n\n## Experimental Results\nReliabilityRAG provides superior robustness against adversarial attacks compared to prior methods, maintains high benign accuracy, and excels in long-form generation tasks where prior robustness-focused methods struggled.\n\nThe paper is available on arXiv (2509.23519) and the OpenReview platform as a NeurIPS 2025 poster presentation."
    ],
    "durationSeconds": 8.555546168000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a33cf7ac-4ac2-409c-acea-1b0879327c55",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-30T07:23:38.339Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q3p5dXdBrgR4JTpSRJyUnT`</summary>

```json
{
  "query": "LP-CP Lévy-Prokhorov conformal prediction NeurIPS 2025 arXiv 2502.14105 experiments evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "283f18d3-598d-47da-bc40-3a51654f7c88",
  "isSidechain": false,
  "requestId": "req_011CbYMQadeNkBZSNCK3HLnB",
  "type": "assistant",
  "uuid": "03f30e15-6bda-4fa6-a41a-e09721c7cadd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FEkBPsvx16uVW4bdkAMhVm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 903,
      "cache_read_input_tokens": 20702,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 903,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 85,
          "cache_read_input_tokens": 20702,
          "cache_creation_input_tokens": 903,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 903
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

_source line 19 · 2026-05-30T07:23:43.816Z_

<details><summary>↩ Tool result · `toolu_01Q3p5dXdBrgR4JTpSRJyUnT`</summary>

```text
Web search results for query: "LP-CP Lévy-Prokhorov conformal prediction NeurIPS 2025 arXiv 2502.14105 experiments evaluation"

Links: [{"title":"[2502.14105] Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/abs/2502.14105"},{"title":"Conformal Prediction under Lévy-Prokhorov Distribution ...","url":"https://arxiv.org/pdf/2502.14105"},{"title":"Conformal Prediction under Lévy-Prokhorov Distribution ...","url":"https://openreview.net/pdf/860efa6f37cc6b64df19821bba75d83edb3b9603.pdf"},{"title":"Coverage Guarantees for Pseudo-Calibrated Conformal Prediction under Distribution Shift","url":"https://arxiv.org/html/2602.14913v1"},{"title":"(PDF) Conformal Prediction under L\\'evy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://www.researchgate.net/publication/389176501_Conformal_Prediction_under_L'evy-Prokhorov_Distribution_Shifts_Robustness_to_Local_and_Global_Perturbations"},{"title":"Conformal Prediction under Lévy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations | OpenReview","url":"https://openreview.net/forum?id=1ULQvdbZ3X"},{"title":"Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/html/2502.14105v2"},{"title":"NeurIPS Poster Conformal Prediction under Lévy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/120230"}]

Based on the web search results, I found information about the paper arXiv 2502.14105:

## Paper Overview

The paper addresses robustness in conformal prediction under distribution shifts by modeling them using Lévy-Prokhorov (LP) ambiguity sets, which capture both local and global perturbations.

## Key Contributions

The paper provides a self-contained overview of LP ambiguity sets and their connections to popular metrics such as Wasserstein and Total Variation.

By propagating the LP ambiguity set through the scoring function, the authors reduce complex high-dimensional distribution shifts to manageable one-dimensional distribution shifts, enabling exact quantification of worst-case quantiles and coverage.

## Venue

The work was presented at NeurIPS 2025 and addresses how conformal prediction can be made robust under distribution shifts using Lévy-Prokhorov ambiguity sets.

## Experiments

The paper validates the proposed approach on three benchmark datasets. However, the specific details about the datasets and evaluation metrics are not fully available in the search results provided.

The paper represents a significant contribution to the field of robust machine learning by providing a theoretically grounded framework for conformal prediction that remains valid under realistic distribution shifts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03f30e15-6bda-4fa6-a41a-e09721c7cadd",
  "isSidechain": false,
  "promptId": "a45afd59-6eac-4f72-8319-52cc86d3dd24",
  "type": "user",
  "uuid": "66bacda6-1c65-47f8-a427-2acc7fcfb959",
  "toolUseResult": {
    "query": "LP-CP Lévy-Prokhorov conformal prediction NeurIPS 2025 arXiv 2502.14105 experiments evaluation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TL4g6uVdx7qKUMGVKh4uBQ",
        "content": [
          {
            "title": "[2502.14105] Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/abs/2502.14105"
          },
          {
            "title": "Conformal Prediction under Lévy-Prokhorov Distribution ...",
            "url": "https://arxiv.org/pdf/2502.14105"
          },
          {
            "title": "Conformal Prediction under Lévy-Prokhorov Distribution ...",
            "url": "https://openreview.net/pdf/860efa6f37cc6b64df19821bba75d83edb3b9603.pdf"
          },
          {
            "title": "Coverage Guarantees for Pseudo-Calibrated Conformal Prediction under Distribution Shift",
            "url": "https://arxiv.org/html/2602.14913v1"
          },
          {
            "title": "(PDF) Conformal Prediction under L\\'evy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://www.researchgate.net/publication/389176501_Conformal_Prediction_under_L'evy-Prokhorov_Distribution_Shifts_Robustness_to_Local_and_Global_Perturbations"
          },
          {
            "title": "Conformal Prediction under Lévy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations | OpenReview",
            "url": "https://openreview.net/forum?id=1ULQvdbZ3X"
          },
          {
            "title": "Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/html/2502.14105v2"
          },
          {
            "title": "NeurIPS Poster Conformal Prediction under Lévy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://neurips.cc/virtual/2025/loc/san-diego/poster/120230"
          }
        ]
      },
      "Based on the web search results, I found information about the paper arXiv 2502.14105:\n\n## Paper Overview\n\nThe paper addresses robustness in conformal prediction under distribution shifts by modeling them using Lévy-Prokhorov (LP) ambiguity sets, which capture both local and global perturbations.\n\n## Key Contributions\n\nThe paper provides a self-contained overview of LP ambiguity sets and their connections to popular metrics such as Wasserstein and Total Variation.\n\nBy propagating the LP ambiguity set through the scoring function, the authors reduce complex high-dimensional distribution shifts to manageable one-dimensional distribution shifts, enabling exact quantification of worst-case quantiles and coverage.\n\n## Venue\n\nThe work was presented at NeurIPS 2025 and addresses how conformal prediction can be made robust under distribution shifts using Lévy-Prokhorov ambiguity sets.\n\n## Experiments\n\nThe paper validates the proposed approach on three benchmark datasets. However, the specific details about the datasets and evaluation metrics are not fully available in the search results provided.\n\nThe paper represents a significant contribution to the field of robust machine learning by providing a theoretically grounded framework for conformal prediction that remains valid under realistic distribution shifts."
    ],
    "durationSeconds": 5.472785915,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "03f30e15-6bda-4fa6-a41a-e09721c7cadd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-30T07:23:46.297Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ShjSSgpFrLnc1kGsPb8V8c`</summary>

```json
{
  "query": "TRAQ conformal prediction RAG NAACL 2024 experimental setup calibration set size evaluation NQ HotpotQA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66bacda6-1c65-47f8-a427-2acc7fcfb959",
  "isSidechain": false,
  "requestId": "req_011CbYMR9S7XV9sfAX8Chs9q",
  "type": "assistant",
  "uuid": "1181604a-5043-448e-968d-11038c4ca121",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lb29sG9DSLmH7bpFJYYMd6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 911,
      "cache_read_input_tokens": 21605,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 911,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 21605,
          "cache_creation_input_tokens": 911,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 911
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

_source line 21 · 2026-05-30T07:24:06.364Z_

<details><summary>↩ Tool result · `toolu_01ShjSSgpFrLnc1kGsPb8V8c`</summary>

```text
Web search results for query: "TRAQ conformal prediction RAG NAACL 2024 experimental setup calibration set size evaluation NQ HotpotQA"

Links: [{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.210/"},{"title":"[PDF] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/28e078b52a761cf3fe5941d3428acb7bbf608f21"},{"title":"[Quick Review] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction","url":"https://liner.com/review/traq-trustworthy-retrieval-augmented-question-answering-via-conformal-prediction"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction","url":"https://arxiv.org/html/2307.04642v2"},{"title":"[2307.04642] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction","url":"https://arxiv.org/abs/2307.04642"},{"title":"Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-21300-6_45"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2307.04642"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal   Prediction","url":"https://arxiv.org/pdf/2307.04642"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction | Underline","url":"https://underline.io/lecture/97447-traq-trustworthy-retrieval-augmented-question-answering-via-conformal-prediction"}]

I found the TRAQ paper published at NAACL 2024. Now let me search for more specific information about the experimental setup, calibration set size, and evaluation on NQ and HotpotQA.

Links: [{"title":"Trustworthy Retrieval Augmented Question Answering via ...","url":"https://aclanthology.org/2024.naacl-long.210.pdf"},{"title":"PeterJinGo/nq_hotpotqa_train · Datasets at Hugging Face","url":"https://huggingface.co/datasets/PeterJinGo/nq_hotpotqa_train"},{"title":"\\thetable Main results. The best performance is set in bold. {^†}/^⋆ represents in-domain/out-domain datasets.","url":"https://arxiv.org/html/2503.09516v3"},{"title":"Method of calibrating a setup","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11428770"},{"title":"\\thetable Main results. The best performance is set in bold, and the second best is set in underline.","url":"https://arxiv.org/html/2503.09516v1"},{"title":"HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering","url":"https://hotpotqa.github.io/"},{"title":"The overview of our framework. | Download Scientific Diagram","url":"https://www.researchgate.net/figure/The-overview-of-our-framework_fig1_392917877"}]

Good! I found a reference to the calibration set sizes. Let me search for the complete experimental setup details from the TRAQ paper.

Links: [{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction","url":"https://arxiv.org/html/2307.04642v2"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering","url":"https://arxiv.org/pdf/2307.04642"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering","url":"https://openreview.net/pdf/bb58dd5cdea83b300c9711a7c5d1add679fe1c38.pdf"},{"title":"Trustworthy Retrieval Augmented Question Answering via ...","url":"https://aclanthology.org/2024.naacl-long.210.pdf"},{"title":"Parallel Optimal Calibration of Mixed-Format Items for Achievement Tests","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11458722/"},{"title":"Benchmarking Optimization Algorithms for Automated Calibration of Quantum Devices","url":"https://arxiv.org/pdf/2509.08555"},{"title":"Optimizing calibration designs with uncertainty in abilities","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12516112/"},{"title":"Application of Multi-Criteria Optimization Methods in the Calibration Process of Digital Measuring Instruments","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10052159/"}]

Perfect! I've found the key information about the TRAQ paper's experimental setup. Let me do one more search to confirm the specific datasets used and get any additional evaluation details.

Links: [{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction","url":"https://arxiv.org/html/2307.04642v2"},{"title":"Trustworthy Retrieval Augmented Question Answering via ...","url":"https://aclanthology.org/2024.naacl-long.210.pdf"},{"title":"SINdex: Semantic INconsistency Index for Hallucination Detection in LLMs","url":"https://arxiv.org/html/2503.05980"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.210/"},{"title":"Nature | Vol 630 | 20 June 2024 | 625 Article","url":"https://sebastianfarquhar.com/assets/papers/farquharDetecting2024.pdf"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/de206617347756b2f30df7e45eb6122412c70a56.pdf"},{"title":"TriviaQA: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension | Request PDF","url":"https://www.researchgate.net/publication/316859263_TriviaQA_A_Large_Scale_Distantly_Supervised_Challenge_Dataset_for_Reading_Comprehension"},{"title":"TriviaQA: A Large Scale Distantly Supervised Challenge Dataset for   Reading Comprehension","url":"https://arxiv.org/pdf/1705.03551"}]

Based on my web search results, I now have comprehensive information about the TRAQ paper. Here's what I found:

## TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction

TRAQ (Li et al., NAACL 2024) was published at the 2024 Conference of the North American Chapter of the Association for Computational Linguistics in Mexico City.

### Methodology

TRAQ uses conformal prediction, a statistical technique for constructing prediction sets that are guaranteed to contain the semantically correct response with high probability. Additionally, TRAQ leverages Bayesian optimization to minimize the size of the constructed sets.

### Experimental Setup

**Calibration Set Size and Data Division:**
The researchers divided each dataset into calibration, optimization, and testing sets, with 300, 300, and 400 data points, respectively.

**Datasets Evaluated:**
TRAQ was evaluated on four datasets, including three standard QA datasets (Natural Question, TriviaQA, SQuAD-1), and one biomedical QA dataset (BioASQ). On each dataset, they collected 1,000 samples that met the criteria of Assumptions Retriever Correctness & LLM Correctness.

**Models and Components:**
Two fine-tuned DPR models were employed—one trained on the Natural Question, TriviaQA, and SQuAD-1 datasets, and the other fine-tuned on BioASQ. Furthermore, they used two generative large language models (LLMs): GPT-3.5-Turbo-0613 (GPT-3.5), whose internal embedding and prediction probabilities are not accessible, and Llama-2-7B (Llama-2).

### Results

In an extensive experimental evaluation, TRAQ demonstrated the desired correctness guarantee while reducing prediction set size by 16.2% on average compared to an ablation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1181604a-5043-448e-968d-11038c4ca121",
  "isSidechain": false,
  "promptId": "a45afd59-6eac-4f72-8319-52cc86d3dd24",
  "type": "user",
  "uuid": "3e426de5-9ee7-45bd-86ec-97470a1d9322",
  "toolUseResult": {
    "query": "TRAQ conformal prediction RAG NAACL 2024 experimental setup calibration set size evaluation NQ HotpotQA",
    "results": [
      {
        "tool_use_id": "srvtoolu_017yJRvf9eNZUxaFMYAiprjB",
        "content": [
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction - ACL Anthology",
            "url": "https://aclanthology.org/2024.naacl-long.210/"
          },
          {
            "title": "[PDF] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/28e078b52a761cf3fe5941d3428acb7bbf608f21"
          },
          {
            "title": "[Quick Review] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction",
            "url": "https://liner.com/review/traq-trustworthy-retrieval-augmented-question-answering-via-conformal-prediction"
          },
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction",
            "url": "https://arxiv.org/html/2307.04642v2"
          },
          {
            "title": "[2307.04642] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction",
            "url": "https://arxiv.org/abs/2307.04642"
          },
          {
            "title": "Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-3-032-21300-6_45"
          },
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/arXiv:2307.04642"
          },
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal   Prediction",
            "url": "https://arxiv.org/pdf/2307.04642"
          },
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction | Underline",
            "url": "https://underline.io/lecture/97447-traq-trustworthy-retrieval-augmented-question-answering-via-conformal-prediction"
          }
        ]
      },
      "I found the TRAQ paper published at NAACL 2024. Now let me search for more specific information about the experimental setup, calibration set size, and evaluation on NQ and HotpotQA.",
      {
        "tool_use_id": "srvtoolu_01554o2AXEGy6Z3yDomL23AG",
        "content": [
          {
            "title": "Trustworthy Retrieval Augmented Question Answering via ...",
            "url": "https://aclanthology.org/2024.naacl-long.210.pdf"
          },
          {
            "title": "PeterJinGo/nq_hotpotqa_train · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/PeterJinGo/nq_hotpotqa_train"
          },
          {
            "title": "\\thetable Main results. The best performance is set in bold. {^†}/^⋆ represents in-domain/out-domain datasets.",
            "url": "https://arxiv.org/html/2503.09516v3"
          },
          {
            "title": "Method of calibrating a setup",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11428770"
          },
          {
            "title": "\\thetable Main results. The best performance is set in bold, and the second best is set in underline.",
            "url": "https://arxiv.org/html/2503.09516v1"
          },
          {
            "title": "HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering",
            "url": "https://hotpotqa.github.io/"
          },
          {
            "title": "The overview of our framework. | Download Scientific Diagram",
            "url": "https://www.researchgate.net/figure/The-overview-of-our-framework_fig1_392917877"
          }
        ]
      },
      "Good! I found a reference to the calibration set sizes. Let me search for the complete experimental setup details from the TRAQ paper.",
      {
        "tool_use_id": "srvtoolu_01S86bFsbqVzAXbHCPx9JAek",
        "content": [
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction",
            "url": "https://arxiv.org/html/2307.04642v2"
          },
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering",
            "url": "https://arxiv.org/pdf/2307.04642"
          },
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering",
            "url": "https://openreview.net/pdf/bb58dd5cdea83b300c9711a7c5d1add679fe1c38.pdf"
          },
          {
            "title": "Trustworthy Retrieval Augmented Question Answering via ...",
            "url": "https://aclanthology.org/2024.naacl-long.210.pdf"
          },
          {
            "title": "Parallel Optimal Calibration of Mixed-Format Items for Achievement Tests",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11458722/"
          },
          {
            "title": "Benchmarking Optimization Algorithms for Automated Calibration of Quantum Devices",
            "url": "https://arxiv.org/pdf/2509.08555"
          },
          {
            "title": "Optimizing calibration designs with uncertainty in abilities",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12516112/"
          },
          {
            "title": "Application of Multi-Criteria Optimization Methods in the Calibration Process of Digital Measuring Instruments",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10052159/"
          }
        ]
      },
      "Perfect! I've found the key information about the TRAQ paper's experimental setup. Let me do one more search to confirm the specific datasets used and get any additional evaluation details.",
      {
        "tool_use_id": "srvtoolu_01KAsKGiwtSVkzbzvbUohU14",
        "content": [
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction",
            "url": "https://arxiv.org/html/2307.04642v2"
          },
          {
            "title": "Trustworthy Retrieval Augmented Question Answering via ...",
            "url": "https://aclanthology.org/2024.naacl-long.210.pdf"
          },
          {
            "title": "SINdex: Semantic INconsistency Index for Hallucination Detection in LLMs",
            "url": "https://arxiv.org/html/2503.05980"
          },
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction - ACL Anthology",
            "url": "https://aclanthology.org/2024.naacl-long.210/"
          },
          {
            "title": "Nature | Vol 630 | 20 June 2024 | 625 Article",
            "url": "https://sebastianfarquhar.com/assets/papers/farquharDetecting2024.pdf"
          },
          {
            "title": "000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019",
            "url": "https://openreview.net/pdf/de206617347756b2f30df7e45eb6122412c70a56.pdf"
          },
          {
            "title": "TriviaQA: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension | Request PDF",
            "url": "https://www.researchgate.net/publication/316859263_TriviaQA_A_Large_Scale_Distantly_Supervised_Challenge_Dataset_for_Reading_Comprehension"
          },
          {
            "title": "TriviaQA: A Large Scale Distantly Supervised Challenge Dataset for   Reading Comprehension",
            "url": "https://arxiv.org/pdf/1705.03551"
          }
        ]
      },
      "Based on my web search results, I now have comprehensive information about the TRAQ paper. Here's what I found:\n\n## TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction\n\nTRAQ (Li et al., NAACL 2024) was published at the 2024 Conference of the North American Chapter of the Association for Computational Linguistics in Mexico City.\n\n### Methodology\n\nTRAQ uses conformal prediction, a statistical technique for constructing prediction sets that are guaranteed to contain the semantically correct response with high probability. Additionally, TRAQ leverages Bayesian optimization to minimize the size of the constructed sets.\n\n### Experimental Setup\n\n**Calibration Set Size and Data Division:**\nThe researchers divided each dataset into calibration, optimization, and testing sets, with 300, 300, and 400 data points, respectively.\n\n**Datasets Evaluated:**\nTRAQ was evaluated on four datasets, including three standard QA datasets (Natural Question, TriviaQA, SQuAD-1), and one biomedical QA dataset (BioASQ). On each dataset, they collected 1,000 samples that met the criteria of Assumptions Retriever Correctness & LLM Correctness.\n\n**Models and Components:**\nTwo fine-tuned DPR models were employed—one trained on the Natural Question, TriviaQA, and SQuAD-1 datasets, and the other fine-tuned on BioASQ. Furthermore, they used two generative large language models (LLMs): GPT-3.5-Turbo-0613 (GPT-3.5), whose internal embedding and prediction probabilities are not accessible, and Llama-2-7B (Llama-2).\n\n### Results\n\nIn an extensive experimental evaluation, TRAQ demonstrated the desired correctness guarantee while reducing prediction set size by 16.2% on average compared to an ablation."
    ],
    "durationSeconds": 20.060503334,
    "searchCount": 4
  },
  "sourceToolAssistantUUID": "1181604a-5043-448e-968d-11038c4ca121",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Conformal Abstention for RAG under Corpus Poisoning via LP-Bounded Retrieval Shifts  ## Core Problem  How can a RAG system provide distribution-free, certified abstention guarantees on answer correc…",
  "leafUuid": "3e426de5-9ee7-45bd-86ec-97470a1d9322",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal abstention for poisoned RAG systems",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4"
}
```

---

### Tool call

_source line 24 · 2026-05-30T07:24:08.925Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VA2bVRzhTn6ofkxTTFUVQV`</summary>

```json
{
  "query": "PoisonedRAG USENIX Security 2025 evaluation setup attack success rate NQ datasets defense evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e426de5-9ee7-45bd-86ec-97470a1d9322",
  "isSidechain": false,
  "requestId": "req_011CbYMSosga5VPTztUcRo4U",
  "type": "assistant",
  "uuid": "f29fe47a-488c-4ca5-94e6-244e6543b4fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGoG3kZPap1FnkMUnyacio",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2411,
      "cache_read_input_tokens": 22516,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2411,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 22516,
          "cache_creation_input_tokens": 2411,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2411
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

_source line 25 · 2026-05-30T07:24:17.875Z_

<details><summary>↩ Tool result · `toolu_01VA2bVRzhTn6ofkxTTFUVQV`</summary>

```text
Web search results for query: "PoisonedRAG USENIX Security 2025 evaluation setup attack success rate NQ datasets defense evaluation"

Links: [{"title":"PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models | USENIX","url":"https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag"},{"title":"PoisonedRAG","url":"https://www.summarizepaper.com/en/arxiv-id/2402.07867v3/"},{"title":"PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models - Penn State","url":"https://pure.psu.edu/en/publications/poisonedrag-knowledge-corruption-attacks-to-retrieval-augmented-g/"},{"title":"RAG Security: How Attackers Poison Your Knowledge Base | BeyondScale","url":"https://beyondscale.tech/blog/rag-security-data-poisoning-guide"},{"title":"34th USENIX Security Symposium: PoisonedRAG: Knowledge Corruption Attack...","url":"https://usenixsecurity25.sched.com/event/289Bm/poisonedrag-knowledge-corruption-attacks-to-retrieval-augmented-generation-of-large-language-models"},{"title":"PoisonedRAG | Proceedings of the 34th USENIX Conference on Security Symposium","url":"https://dl.acm.org/doi/10.5555/3766078.3766275"},{"title":"GitHub - sleeepeer/PoisonedRAG: [USENIX Security 2025] PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models · GitHub","url":"https://github.com/sleeepeer/PoisonedRAG"},{"title":"Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems","url":"https://arxiv.org/pdf/2603.18034"},{"title":"[2402.07867] PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models","url":"https://arxiv.org/abs/2402.07867"},{"title":"Machine Against the RAG: Jamming Retrieval-Augmented ...","url":"https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-980-shafran.pdf"}]

I found comprehensive information about PoisonedRAG from the USENIX Security 2025 conference. Here are the key findings:

## Attack Success Rate

PoisonedRAG could achieve a 90% attack success rate when injecting five malicious texts for each target question into a knowledge database with millions of texts.

## NQ Datasets Evaluation

In black-box settings where the attacker has no access to the model's internals, PoisonedRAG achieved attack success rates of 97% on Natural Questions, 99% on HotpotQA, and 91% on MS-MARCO.

## Evaluation Setup

PoisonedRAG is the first knowledge corruption attack to RAG, where an attacker could inject a few malicious texts into the knowledge database of a RAG system to induce an LLM to generate an attacker-chosen target answer for an attacker-chosen target question. The knowledge corruption attacks are formulated as an optimization problem, whose solution is a set of malicious texts.

Depending on the background knowledge (e.g., black-box and white-box settings) of an attacker on a RAG system, two solutions to solve the optimization problem are proposed, respectively.

## Defense Evaluation

Several defenses were evaluated and the results show they are insufficient to defend against PoisonedRAG, highlighting the need for new defenses.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f29fe47a-488c-4ca5-94e6-244e6543b4fb",
  "isSidechain": false,
  "promptId": "a45afd59-6eac-4f72-8319-52cc86d3dd24",
  "type": "user",
  "uuid": "94d1783f-dd8c-4878-8865-132a44a0643e",
  "toolUseResult": {
    "query": "PoisonedRAG USENIX Security 2025 evaluation setup attack success rate NQ datasets defense evaluation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WsrfzfGk4BhYvupJWBWSC3",
        "content": [
          {
            "title": "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models | USENIX",
            "url": "https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag"
          },
          {
            "title": "PoisonedRAG",
            "url": "https://www.summarizepaper.com/en/arxiv-id/2402.07867v3/"
          },
          {
            "title": "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models - Penn State",
            "url": "https://pure.psu.edu/en/publications/poisonedrag-knowledge-corruption-attacks-to-retrieval-augmented-g/"
          },
          {
            "title": "RAG Security: How Attackers Poison Your Knowledge Base | BeyondScale",
            "url": "https://beyondscale.tech/blog/rag-security-data-poisoning-guide"
          },
          {
            "title": "34th USENIX Security Symposium: PoisonedRAG: Knowledge Corruption Attack...",
            "url": "https://usenixsecurity25.sched.com/event/289Bm/poisonedrag-knowledge-corruption-attacks-to-retrieval-augmented-generation-of-large-language-models"
          },
          {
            "title": "PoisonedRAG | Proceedings of the 34th USENIX Conference on Security Symposium",
            "url": "https://dl.acm.org/doi/10.5555/3766078.3766275"
          },
          {
            "title": "GitHub - sleeepeer/PoisonedRAG: [USENIX Security 2025] PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models · GitHub",
            "url": "https://github.com/sleeepeer/PoisonedRAG"
          },
          {
            "title": "Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems",
            "url": "https://arxiv.org/pdf/2603.18034"
          },
          {
            "title": "[2402.07867] PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models",
            "url": "https://arxiv.org/abs/2402.07867"
          },
          {
            "title": "Machine Against the RAG: Jamming Retrieval-Augmented ...",
            "url": "https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-980-shafran.pdf"
          }
        ]
      },
      "I found comprehensive information about PoisonedRAG from the USENIX Security 2025 conference. Here are the key findings:\n\n## Attack Success Rate\n\nPoisonedRAG could achieve a 90% attack success rate when injecting five malicious texts for each target question into a knowledge database with millions of texts.\n\n## NQ Datasets Evaluation\n\nIn black-box settings where the attacker has no access to the model's internals, PoisonedRAG achieved attack success rates of 97% on Natural Questions, 99% on HotpotQA, and 91% on MS-MARCO.\n\n## Evaluation Setup\n\nPoisonedRAG is the first knowledge corruption attack to RAG, where an attacker could inject a few malicious texts into the knowledge database of a RAG system to induce an LLM to generate an attacker-chosen target answer for an attacker-chosen target question. The knowledge corruption attacks are formulated as an optimization problem, whose solution is a set of malicious texts.\n\nDepending on the background knowledge (e.g., black-box and white-box settings) of an attacker on a RAG system, two solutions to solve the optimization problem are proposed, respectively.\n\n## Defense Evaluation\n\nSeveral defenses were evaluated and the results show they are insufficient to defend against PoisonedRAG, highlighting the need for new defenses."
    ],
    "durationSeconds": 8.946142615000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f29fe47a-488c-4ca5-94e6-244e6543b4fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-30T07:24:20.668Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0159SKBrG59pYNgUwZeSANv6`</summary>

```json
{
  "query": "CorruptRAG single document poisoning attack RAG 2025 evaluation experimental setup arXiv 2504.03957"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94d1783f-dd8c-4878-8865-132a44a0643e",
  "isSidechain": false,
  "requestId": "req_011CbYMTf1ufR62hTq2CrwYR",
  "type": "assistant",
  "uuid": "daa2f018-d0eb-4530-92a1-7b5f55741226",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EgM8ptF1akydQwaxyEbaKm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1042,
      "cache_read_input_tokens": 24927,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1042,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 24927,
          "cache_creation_input_tokens": 1042,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1042
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

_source line 27 · 2026-05-30T07:24:27.826Z_

<details><summary>↩ Tool result · `toolu_0159SKBrG59pYNgUwZeSANv6`</summary>

```text
Web search results for query: "CorruptRAG single document poisoning attack RAG 2025 evaluation experimental setup arXiv 2504.03957"

Links: [{"title":"Architecture Matters: Comparing RAG Systems under Knowledge Base Poisoning","url":"https://arxiv.org/html/2605.05632v1"},{"title":"Scalable RAG Poisoning through Transferable Attention- ...","url":"https://arxiv.org/pdf/2510.00586"},{"title":"[2504.03957] Practical Poisoning Attacks against Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2504.03957"},{"title":"Practical Poisoning Attacks against Retrieval-Augmented Generation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250403957Z/abstract"},{"title":"CtrlRAG: Black-box Document Poisoning Attacks for Retrieval-Augmented Generation of Large Language Models","url":"https://arxiv.org/pdf/2503.06950"},{"title":"Practical Poisoning Attacks against Retrieval-Augmented Generation Baolei Zhang","url":"https://arxiv.org/pdf/2504.03957"},{"title":"Addressing Corpus Knowledge Poisoning Attacks on RAG Using Sparse Attention","url":"https://arxiv.org/html/2602.04711v2"},{"title":"One Shot Dominance: Knowledge Poisoning Attack on Retrieval-Augmented Generation Systems","url":"https://arxiv.org/pdf/2505.11548"}]

Based on the search results, here's what I found about CorruptRAG and arXiv paper 2504.03957:

## Overview

CorruptRAG is a practical poisoning attack against RAG systems in which the attacker injects only a single poisoned text, enhancing both feasibility and stealth.

## Problem It Addresses

Most existing attacks assume that the attacker can insert a sufficient number of poisoned texts per query to outnumber correct-answer texts in retrieval, an assumption that is often unrealistic. CorruptRAG overcomes this limitation by constraining the attack to a single poisoned document.

## Attack Framework

CorruptRAG constrains the attacker to injecting only one poisoned text per query, which enhances both the feasibility and stealth of the attack while still allowing the attacker to manipulate the knowledge database, and frames poisoning attacks as an optimization problem aimed at injecting a single poisoned text per query into the knowledge database.

## Evaluation Results

Extensive experiments across multiple datasets demonstrate that CorruptRAG achieves higher attack success rates compared to existing baselines.

## Attack Variants

CorruptRAG (Zhang et al., 2025b) advances the threat model by constraining the attacker to a single poisoned text per query, substantially increasing the practical relevance of the attack. CorruptRAG injects templated or LLM-refined malicious passages to steer generation upon retrieval.

The paper presents a more practical and realistic threat model compared to prior work by demonstrating effective attacks with only a single poisoned document injection.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "daa2f018-d0eb-4530-92a1-7b5f55741226",
  "isSidechain": false,
  "promptId": "a45afd59-6eac-4f72-8319-52cc86d3dd24",
  "type": "user",
  "uuid": "77f7336e-7564-4a92-9b8f-dd18f27cb16a",
  "toolUseResult": {
    "query": "CorruptRAG single document poisoning attack RAG 2025 evaluation experimental setup arXiv 2504.03957",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JComEVjTfNYygwJrBf9Zyg",
        "content": [
          {
            "title": "Architecture Matters: Comparing RAG Systems under Knowledge Base Poisoning",
            "url": "https://arxiv.org/html/2605.05632v1"
          },
          {
            "title": "Scalable RAG Poisoning through Transferable Attention- ...",
            "url": "https://arxiv.org/pdf/2510.00586"
          },
          {
            "title": "[2504.03957] Practical Poisoning Attacks against Retrieval-Augmented Generation",
            "url": "https://arxiv.org/abs/2504.03957"
          },
          {
            "title": "Practical Poisoning Attacks against Retrieval-Augmented Generation - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250403957Z/abstract"
          },
          {
            "title": "CtrlRAG: Black-box Document Poisoning Attacks for Retrieval-Augmented Generation of Large Language Models",
            "url": "https://arxiv.org/pdf/2503.06950"
          },
          {
            "title": "Practical Poisoning Attacks against Retrieval-Augmented Generation Baolei Zhang",
            "url": "https://arxiv.org/pdf/2504.03957"
          },
          {
            "title": "Addressing Corpus Knowledge Poisoning Attacks on RAG Using Sparse Attention",
            "url": "https://arxiv.org/html/2602.04711v2"
          },
          {
            "title": "One Shot Dominance: Knowledge Poisoning Attack on Retrieval-Augmented Generation Systems",
            "url": "https://arxiv.org/pdf/2505.11548"
          }
        ]
      },
      "Based on the search results, here's what I found about CorruptRAG and arXiv paper 2504.03957:\n\n## Overview\n\nCorruptRAG is a practical poisoning attack against RAG systems in which the attacker injects only a single poisoned text, enhancing both feasibility and stealth.\n\n## Problem It Addresses\n\nMost existing attacks assume that the attacker can insert a sufficient number of poisoned texts per query to outnumber correct-answer texts in retrieval, an assumption that is often unrealistic. CorruptRAG overcomes this limitation by constraining the attack to a single poisoned document.\n\n## Attack Framework\n\nCorruptRAG constrains the attacker to injecting only one poisoned text per query, which enhances both the feasibility and stealth of the attack while still allowing the attacker to manipulate the knowledge database, and frames poisoning attacks as an optimization problem aimed at injecting a single poisoned text per query into the knowledge database.\n\n## Evaluation Results\n\nExtensive experiments across multiple datasets demonstrate that CorruptRAG achieves higher attack success rates compared to existing baselines.\n\n## Attack Variants\n\nCorruptRAG (Zhang et al., 2025b) advances the threat model by constraining the attacker to a single poisoned text per query, substantially increasing the practical relevance of the attack. CorruptRAG injects templated or LLM-refined malicious passages to steer generation upon retrieval.\n\nThe paper presents a more practical and realistic threat model compared to prior work by demonstrating effective attacks with only a single poisoned document injection."
    ],
    "durationSeconds": 7.151924260000015,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "daa2f018-d0eb-4530-92a1-7b5f55741226",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-30T07:24:29.982Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016PdK5Qejq1gxVrDPddXKPp`</summary>

```json
{
  "query": "conformal prediction abstention selective prediction evaluation metrics coverage abstention tradeoff 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77f7336e-7564-4a92-9b8f-dd18f27cb16a",
  "isSidechain": false,
  "requestId": "req_011CbYMUPeDGyTdFu3KUuQJu",
  "type": "assistant",
  "uuid": "0e67e0a5-c5b3-47d2-913a-c09d1b76f13b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012p17HQHqKcELhS2hAbGTVt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 849,
      "cache_read_input_tokens": 25969,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 849,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 25969,
          "cache_creation_input_tokens": 849,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 849
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

_source line 29 · 2026-05-30T07:24:38.025Z_

<details><summary>↩ Tool result · `toolu_016PdK5Qejq1gxVrDPddXKPp`</summary>

```text
Web search results for query: "conformal prediction abstention selective prediction evaluation metrics coverage abstention tradeoff 2025 2026"

Links: [{"title":"Learning Conformal Abstention Policies for Adaptive Risk Management in   Large Language and Vision-Language Models","url":"https://arxiv.org/pdf/2502.06884"},{"title":"Selective Omniprediction and Fair Abstention | OpenReview","url":"https://openreview.net/forum?id=BoYGLpNXZd"},{"title":"Explicit Abstention Knobs for Predictable Reliability in Video Question Answering","url":"https://arxiv.org/html/2601.00138v1"},{"title":"Conformal Abstention Framework","url":"https://www.emergentmind.com/topics/conformal-abstention"},{"title":"Uncertainty-Driven Reliability: Selective Prediction and ...","url":"https://arxiv.org/pdf/2508.07556"},{"title":"Post-selection Inference for Conformal Prediction: Trading off Coverage   for Precision","url":"https://arxiv.org/pdf/2304.06158"},{"title":"Selective Omniprediction and Fair Abstention Sílvia Casacuberta","url":"https://openreview.net/pdf?id=BoYGLpNXZd"}]

I found several highly relevant recent papers on conformal prediction, abstention, and selective prediction. Here's a summary of key findings:

## Recent Research (2025-2026)

**Learnable Conformal Abstention:** Recent work proposes learnable conformal abstention, integrating reinforcement learning with conformal prediction to optimize abstention thresholds dynamically, balancing multiple objectives while minimizing prediction set size and maintaining reliable coverage.

**Key Challenge:** Conformal prediction methods provide statistical guarantees but rely on static thresholds that fail to adapt to varying task complexities, with methods like LAC tending to produce overly narrow prediction sets while APS generates excessively large sets.

**Selective Prediction and Fair Abstention:** Research extends multigroup fairness algorithms to selective classification, using calibrated and multiaccurate predictors to build selective classifiers that abstain optimally, with extensions to conformal prediction methods achieving marginal and group-conditional coverage guarantees.

**Evaluation and Tradeoffs:** Current frameworks support both hard abstention (refusing to answer) and soft abstention (outputting answer sets), with extensions to multiple operating points using dual-threshold or learnable thresholding policies.

**Coverage-Precision Tradeoff:** Practitioners can trade coverage probability for prediction set quality while maintaining finite sample guarantees, allowing free tradeoff between coverage and criteria like prediction set size.

The search results show active research in 2025 addressing the coverage-abstention tradeoff through more adaptive and fair approaches to conformal prediction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e67e0a5-c5b3-47d2-913a-c09d1b76f13b",
  "isSidechain": false,
  "promptId": "a45afd59-6eac-4f72-8319-52cc86d3dd24",
  "type": "user",
  "uuid": "ebe6a88c-4dad-475a-b482-83dcc787a937",
  "toolUseResult": {
    "query": "conformal prediction abstention selective prediction evaluation metrics coverage abstention tradeoff 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XimvghXpv7EcvBgDCffLae",
        "content": [
          {
            "title": "Learning Conformal Abstention Policies for Adaptive Risk Management in   Large Language and Vision-Language Models",
            "url": "https://arxiv.org/pdf/2502.06884"
          },
          {
            "title": "Selective Omniprediction and Fair Abstention | OpenReview",
            "url": "https://openreview.net/forum?id=BoYGLpNXZd"
          },
          {
            "title": "Explicit Abstention Knobs for Predictable Reliability in Video Question Answering",
            "url": "https://arxiv.org/html/2601.00138v1"
          },
          {
            "title": "Conformal Abstention Framework",
            "url": "https://www.emergentmind.com/topics/conformal-abstention"
          },
          {
            "title": "Uncertainty-Driven Reliability: Selective Prediction and ...",
            "url": "https://arxiv.org/pdf/2508.07556"
          },
          {
            "title": "Post-selection Inference for Conformal Prediction: Trading off Coverage   for Precision",
            "url": "https://arxiv.org/pdf/2304.06158"
          },
          {
            "title": "Selective Omniprediction and Fair Abstention Sílvia Casacuberta",
            "url": "https://openreview.net/pdf?id=BoYGLpNXZd"
          }
        ]
      },
      "I found several highly relevant recent papers on conformal prediction, abstention, and selective prediction. Here's a summary of key findings:\n\n## Recent Research (2025-2026)\n\n**Learnable Conformal Abstention:** Recent work proposes learnable conformal abstention, integrating reinforcement learning with conformal prediction to optimize abstention thresholds dynamically, balancing multiple objectives while minimizing prediction set size and maintaining reliable coverage.\n\n**Key Challenge:** Conformal prediction methods provide statistical guarantees but rely on static thresholds that fail to adapt to varying task complexities, with methods like LAC tending to produce overly narrow prediction sets while APS generates excessively large sets.\n\n**Selective Prediction and Fair Abstention:** Research extends multigroup fairness algorithms to selective classification, using calibrated and multiaccurate predictors to build selective classifiers that abstain optimally, with extensions to conformal prediction methods achieving marginal and group-conditional coverage guarantees.\n\n**Evaluation and Tradeoffs:** Current frameworks support both hard abstention (refusing to answer) and soft abstention (outputting answer sets), with extensions to multiple operating points using dual-threshold or learnable thresholding policies.\n\n**Coverage-Precision Tradeoff:** Practitioners can trade coverage probability for prediction set quality while maintaining finite sample guarantees, allowing free tradeoff between coverage and criteria like prediction set size.\n\nThe search results show active research in 2025 addressing the coverage-abstention tradeoff through more adaptive and fair approaches to conformal prediction."
    ],
    "durationSeconds": 8.038530889000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0e67e0a5-c5b3-47d2-913a-c09d1b76f13b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-30T07:24:38.055Z_

```json
{
  "parentUuid": "ebe6a88c-4dad-475a-b482-83dcc787a937",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "2bd9e99e-e048-4315-9529-20383df59c99",
  "timestamp": "2026-05-30T07:24:38.055Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-30T07:24:40.430Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011BcxZPYVjM59Csb2ZaawSL`</summary>

```json
{
  "query": "RAGDefender cosine similarity clustering defense poisoning RAG ACSAC 2025 evaluation baselines ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bd9e99e-e048-4315-9529-20383df59c99",
  "isSidechain": false,
  "requestId": "req_011CbYMV9JXnAu6TNQydFKRU",
  "type": "assistant",
  "uuid": "86141e73-46f7-4aa1-8ae4-7fb815453cbe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011zdzcCFPJCeFosgJ5my7Vs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 865,
      "cache_read_input_tokens": 26818,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 865,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 26818,
          "cache_creation_input_tokens": 865,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 865
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

_source line 32 · 2026-05-30T07:24:46.694Z_

<details><summary>↩ Tool result · `toolu_011BcxZPYVjM59Csb2ZaawSL`</summary>

```text
Web search results for query: "RAGDefender cosine similarity clustering defense poisoning RAG ACSAC 2025 evaluation baselines ablation"

Links: [{"title":"GitHub - SecAI-Lab/RAGDefender: Artifacts for paper \"Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems\" · GitHub","url":"https://github.com/SecAI-Lab/RAGDefender"},{"title":"Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks","url":"https://kevinkoo001.github.io/assets/pdf/acsac25-ragdefender.pdf"},{"title":"Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems","url":"https://arxiv.org/html/2511.01268v1"},{"title":"Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems","url":"https://arxiv.org/pdf/2511.01268"},{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"RAG Poisoning: Threats and Defenses","url":"https://www.emergentmind.com/topics/retrieval-augmented-generation-rag-poisoning"},{"title":"RAG security: the forgotten attack surface – Christian Schneider","url":"https://christian-schneider.net/blog/rag-security-forgotten-attack-surface/"}]

Based on the search results, here's what I found about RAGDefender:

## Overview

RAGDefender is a lightweight, efficient defense mechanism designed to protect Retrieval-Augmented Generation (RAG) systems from knowledge corruption attacks such as PoisonedRAG, Blind, and GARAG.

## Technical Approach

RAGDefender has a twofold approach: grouping the retrieved passages and identifying adversarial passages, using two novel strategies (clustering-based and concentration-based grouping) to rescue legitimate (i.e., unpoisoned) passages at the first stage.

## Key Advantages

RAGDefender operates during the post-retrieval phase, leveraging lightweight machine learning techniques to detect and filter out adversarial content without requiring additional model training or inference. It is designed for seamless integration into an existing RAG pipeline while imposing minimal computational overhead, as it requires neither supplementary LLM inference nor additional model training, and operates as a preprocessing module that filters retrieved passages before reaching the generator.

## Publication

The work was published at the Annual Computer Security Applications Conference (ACSAC) in 2025. You can access the paper and artifacts on the [GitHub repository](https://github.com/SecAI-Lab/RAGDefender) and [arXiv](https://arxiv.org/abs/2511.01268).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86141e73-46f7-4aa1-8ae4-7fb815453cbe",
  "isSidechain": false,
  "promptId": "a45afd59-6eac-4f72-8319-52cc86d3dd24",
  "type": "user",
  "uuid": "c69d4e7f-220c-4f27-a0f9-9c3e9aaf915c",
  "toolUseResult": {
    "query": "RAGDefender cosine similarity clustering defense poisoning RAG ACSAC 2025 evaluation baselines ablation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TMFqA6CRnctTjLW8vDKrMF",
        "content": [
          {
            "title": "GitHub - SecAI-Lab/RAGDefender: Artifacts for paper \"Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems\" · GitHub",
            "url": "https://github.com/SecAI-Lab/RAGDefender"
          },
          {
            "title": "Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks",
            "url": "https://kevinkoo001.github.io/assets/pdf/acsac25-ragdefender.pdf"
          },
          {
            "title": "Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems",
            "url": "https://arxiv.org/html/2511.01268v1"
          },
          {
            "title": "Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems",
            "url": "https://arxiv.org/pdf/2511.01268"
          },
          {
            "title": "RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2512.24268"
          },
          {
            "title": "RAG Poisoning: Threats and Defenses",
            "url": "https://www.emergentmind.com/topics/retrieval-augmented-generation-rag-poisoning"
          },
          {
            "title": "RAG security: the forgotten attack surface – Christian Schneider",
            "url": "https://christian-schneider.net/blog/rag-security-forgotten-attack-surface/"
          }
        ]
      },
      "Based on the search results, here's what I found about RAGDefender:\n\n## Overview\n\nRAGDefender is a lightweight, efficient defense mechanism designed to protect Retrieval-Augmented Generation (RAG) systems from knowledge corruption attacks such as PoisonedRAG, Blind, and GARAG.\n\n## Technical Approach\n\nRAGDefender has a twofold approach: grouping the retrieved passages and identifying adversarial passages, using two novel strategies (clustering-based and concentration-based grouping) to rescue legitimate (i.e., unpoisoned) passages at the first stage.\n\n## Key Advantages\n\nRAGDefender operates during the post-retrieval phase, leveraging lightweight machine learning techniques to detect and filter out adversarial content without requiring additional model training or inference. It is designed for seamless integration into an existing RAG pipeline while imposing minimal computational overhead, as it requires neither supplementary LLM inference nor additional model training, and operates as a preprocessing module that filters retrieved passages before reaching the generator.\n\n## Publication\n\nThe work was published at the Annual Computer Security Applications Conference (ACSAC) in 2025. You can access the paper and artifacts on the [GitHub repository](https://github.com/SecAI-Lab/RAGDefender) and [arXiv](https://arxiv.org/abs/2511.01268)."
    ],
    "durationSeconds": 6.258873997000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "86141e73-46f7-4aa1-8ae4-7fb815453cbe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-30T07:24:48.960Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E5hsirG61FRYMkbL1yjBcR`</summary>

```json
{
  "query": "benchmarking poisoning attacks RAG arXiv 2505.18543 unified evaluation framework datasets attacks defenses"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c69d4e7f-220c-4f27-a0f9-9c3e9aaf915c",
  "isSidechain": false,
  "requestId": "req_011CbYMVnEJAEZ64ns4i6hV9",
  "type": "assistant",
  "uuid": "c66262e1-54f2-47c7-bedb-d77b0675c582",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7zk56sy94huVn1NCL32mk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 795,
      "cache_read_input_tokens": 27683,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 795,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 27683,
          "cache_creation_input_tokens": 795,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 795
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
  "lastPrompt": "# Conformal Abstention for RAG under Corpus Poisoning via LP-Bounded Retrieval Shifts  ## Core Problem  How can a RAG system provide distribution-free, certified abstention guarantees on answer correc…",
  "leafUuid": "c66262e1-54f2-47c7-bedb-d77b0675c582",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal abstention for poisoned RAG systems",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4"
}
```

---

### Tool result

_source line 36 · 2026-05-30T07:24:56.527Z_

<details><summary>↩ Tool result · `toolu_01E5hsirG61FRYMkbL1yjBcR`</summary>

```text
Web search results for query: "benchmarking poisoning attacks RAG arXiv 2505.18543 unified evaluation framework datasets attacks defenses"

Links: [{"title":"[2505.18543] Benchmarking Poisoning Attacks against Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2505.18543"},{"title":"[PDF] Benchmarking Poisoning Attacks against Retrieval-Augmented Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Benchmarking-Poisoning-Attacks-against-Generation-Zhang-Xin/ccf24f7db7680562628545beaa26fca9d3745e1e"},{"title":"PoisonArena: Uncovering Competing Poisoning Attacks in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2505.12574"},{"title":"PoisonArena: Uncovering Competing Poisoning Attacks in ...","url":"https://poison-arena.github.io/"},{"title":"Benchmarking Poisoning Attacks against Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2505.18543"},{"title":"PoisonArena: Uncovering Competing Poisoning Attacks in Retrieval-Augmented Generation","url":"https://arxiv.org/html/2505.12574v4"},{"title":"(PDF) Benchmarking Poisoning Attacks against Retrieval-Augmented Generation","url":"https://www.researchgate.net/publication/392105526_Benchmarking_Poisoning_Attacks_against_Retrieval-Augmented_Generation"}]

Based on the search results, here's what I found about arXiv paper 2505.18543:

## Benchmarking Poisoning Attacks against Retrieval-Augmented Generation

The paper proposes the first comprehensive benchmark framework for evaluating poisoning attacks on RAG.

**Benchmark Scope:**
The benchmark covers 5 standard question answering (QA) datasets and 10 expanded variants, along with 13 poisoning attack methods and 7 defense mechanisms, representing a broad spectrum of existing techniques.

**Key Framework:**
The researchers introduce RAG Security Bench (RSB), a unified benchmark that systematically evaluates a broad range of poisoning attacks and defense mechanisms across RAG frameworks spanning four categories: sequential RAG with fixed retrieval-generation pipelines, branching RAG that explores multiple retrieval paths, conditional RAG that adapts retrieval based on the query content, and loop RAG that performs iterative refinement through repeated retrieval and generation cycles.

**Main Findings:**
- While existing attacks perform well on standard QA datasets, their effectiveness drops significantly on the expanded versions.
- Various advanced RAG architectures, such as sequential, branching, conditional, and loop RAG, as well as multi-turn conversational RAG, multimodal RAG systems, and RAG-based LLM agent systems, remain susceptible to poisoning attacks.
- Current defense techniques fail to provide robust protection, underscoring the pressing need for more resilient and generalizable defense strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c66262e1-54f2-47c7-bedb-d77b0675c582",
  "isSidechain": false,
  "promptId": "a45afd59-6eac-4f72-8319-52cc86d3dd24",
  "type": "user",
  "uuid": "e74bfe5f-d8ab-494e-804f-d0333e03fbeb",
  "toolUseResult": {
    "query": "benchmarking poisoning attacks RAG arXiv 2505.18543 unified evaluation framework datasets attacks defenses",
    "results": [
      {
        "tool_use_id": "srvtoolu_013USztKtv9qzgea9DoCPVMR",
        "content": [
          {
            "title": "[2505.18543] Benchmarking Poisoning Attacks against Retrieval-Augmented Generation",
            "url": "https://arxiv.org/abs/2505.18543"
          },
          {
            "title": "[PDF] Benchmarking Poisoning Attacks against Retrieval-Augmented Generation | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Benchmarking-Poisoning-Attacks-against-Generation-Zhang-Xin/ccf24f7db7680562628545beaa26fca9d3745e1e"
          },
          {
            "title": "PoisonArena: Uncovering Competing Poisoning Attacks in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2505.12574"
          },
          {
            "title": "PoisonArena: Uncovering Competing Poisoning Attacks in ...",
            "url": "https://poison-arena.github.io/"
          },
          {
            "title": "Benchmarking Poisoning Attacks against Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2505.18543"
          },
          {
            "title": "PoisonArena: Uncovering Competing Poisoning Attacks in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2505.12574v4"
          },
          {
            "title": "(PDF) Benchmarking Poisoning Attacks against Retrieval-Augmented Generation",
            "url": "https://www.researchgate.net/publication/392105526_Benchmarking_Poisoning_Attacks_against_Retrieval-Augmented_Generation"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2505.18543:\n\n## Benchmarking Poisoning Attacks against Retrieval-Augmented Generation\n\nThe paper proposes the first comprehensive benchmark framework for evaluating poisoning attacks on RAG.\n\n**Benchmark Scope:**\nThe benchmark covers 5 standard question answering (QA) datasets and 10 expanded variants, along with 13 poisoning attack methods and 7 defense mechanisms, representing a broad spectrum of existing techniques.\n\n**Key Framework:**\nThe researchers introduce RAG Security Bench (RSB), a unified benchmark that systematically evaluates a broad range of poisoning attacks and defense mechanisms across RAG frameworks spanning four categories: sequential RAG with fixed retrieval-generation pipelines, branching RAG that explores multiple retrieval paths, conditional RAG that adapts retrieval based on the query content, and loop RAG that performs iterative refinement through repeated retrieval and generation cycles.\n\n**Main Findings:**\n- While existing attacks perform well on standard QA datasets, their effectiveness drops significantly on the expanded versions.\n- Various advanced RAG architectures, such as sequential, branching, conditional, and loop RAG, as well as multi-turn conversational RAG, multimodal RAG systems, and RAG-based LLM agent systems, remain susceptible to poisoning attacks.\n- Current defense techniques fail to provide robust protection, underscoring the pressing need for more resilient and generalizable defense strategies."
    ],
    "durationSeconds": 7.5594835620000085,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c66262e1-54f2-47c7-bedb-d77b0675c582",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-30T07:24:58.805Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BgLxe3Ys4cVWQbVYnjQYXq`</summary>

```json
{
  "query": "Qwen3-Embedding-8B embedding model evaluation 2025 2026 sentence embedding benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e74bfe5f-d8ab-494e-804f-d0333e03fbeb",
  "isSidechain": false,
  "requestId": "req_011CbYMWWKcK6qDCAmqFEJQR",
  "type": "assistant",
  "uuid": "65056cb5-7006-40fc-ab05-f97836689584",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MyAKeN1NNC4BtmS6gtoRTm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 853,
      "cache_read_input_tokens": 28478,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 853,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 28478,
          "cache_creation_input_tokens": 853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 853
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

_source line 38 · 2026-05-30T07:25:05.186Z_

<details><summary>↩ Tool result · `toolu_01BgLxe3Ys4cVWQbVYnjQYXq`</summary>

```text
Web search results for query: "Qwen3-Embedding-8B embedding model evaluation 2025 2026 sentence embedding benchmark"

Links: [{"title":"[2601.04720] Qwen3-VL-Embedding and Qwen3-VL-Reranker: A Unified Framework for State-of-the-Art Multimodal Retrieval and Ranking","url":"https://arxiv.org/abs/2601.04720"},{"title":"Embedding Models 2026: Benchmark and Comparison | Ailog RAG","url":"https://app.ailog.fr/en/blog/news/embedding-models-2026"},{"title":"Qwen/Qwen3-Embedding-8B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Embedding-8B"},{"title":"qwen3-embedding","url":"https://ollama.com/library/qwen3-embedding"},{"title":"Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models | Qwen","url":"https://qwenlm.github.io/blog/qwen3-embedding/"},{"title":"GitHub - QwenLM/Qwen3-Embedding · GitHub","url":"https://github.com/QwenLM/Qwen3-Embedding"},{"title":"[2506.05176] Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models","url":"https://arxiv.org/abs/2506.05176"},{"title":"Qwen/Qwen3-VL-Embedding-8B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-VL-Embedding-8B"},{"title":"Qwen3-VL-Embedding and Qwen3-VL-Reranker: A Unified Framework for State-of-the-Art Multimodal Retrieval and Ranking","url":"https://arxiv.org/pdf/2601.04720"},{"title":"Qwen3-Embedding-8B - Model Info, Parameters, Benchmarks - SiliconFlow\"","url":"https://www.siliconflow.com/models/qwen3-embedding-8b"}]

Based on the search results, here's what I found about the Qwen3-Embedding-8B embedding model evaluation:

## Benchmark Performance

The 8B size embedding model ranks No.1 in the MTEB multilingual leaderboard (as of June 5, 2025, score 70.58). Additionally, Qwen3-Embedding-8B (70.6 MTEB) surpasses all API models including OpenAI (64.6) and Google (68.3).

## Model Capabilities

The Qwen3 Embedding series represents significant advancements in multiple text embedding and ranking tasks, including text retrieval, code retrieval, text classification, text clustering, and bitext mining. The series inherits the exceptional multilingual capabilities, long-text understanding, and reasoning skills of its foundational model.

## Related Multimodal Variant

There is also a multimodal variant: Qwen3-VL-Embedding-8B attains an overall score of 77.8 on MMEB-V2, ranking first among all models (as of January 8, 2025).

## Market Impact

The gap reversed in 2025-2026, indicating that open-source models like Qwen3-Embedding-8B have now surpassed proprietary API-based embedding solutions in performance benchmarks during this period.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65056cb5-7006-40fc-ab05-f97836689584",
  "isSidechain": false,
  "promptId": "a45afd59-6eac-4f72-8319-52cc86d3dd24",
  "type": "user",
  "uuid": "1049fc55-f412-4450-b02a-04c04de974bf",
  "toolUseResult": {
    "query": "Qwen3-Embedding-8B embedding model evaluation 2025 2026 sentence embedding benchmark",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ravo1dMaMCNH8JdeQjbatz",
        "content": [
          {
            "title": "[2601.04720] Qwen3-VL-Embedding and Qwen3-VL-Reranker: A Unified Framework for State-of-the-Art Multimodal Retrieval and Ranking",
            "url": "https://arxiv.org/abs/2601.04720"
          },
          {
            "title": "Embedding Models 2026: Benchmark and Comparison | Ailog RAG",
            "url": "https://app.ailog.fr/en/blog/news/embedding-models-2026"
          },
          {
            "title": "Qwen/Qwen3-Embedding-8B · Hugging Face",
            "url": "https://huggingface.co/Qwen/Qwen3-Embedding-8B"
          },
          {
            "title": "qwen3-embedding",
            "url": "https://ollama.com/library/qwen3-embedding"
          },
          {
            "title": "Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models | Qwen",
            "url": "https://qwenlm.github.io/blog/qwen3-embedding/"
          },
          {
            "title": "GitHub - QwenLM/Qwen3-Embedding · GitHub",
            "url": "https://github.com/QwenLM/Qwen3-Embedding"
          },
          {
            "title": "[2506.05176] Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models",
            "url": "https://arxiv.org/abs/2506.05176"
          },
          {
            "title": "Qwen/Qwen3-VL-Embedding-8B · Hugging Face",
            "url": "https://huggingface.co/Qwen/Qwen3-VL-Embedding-8B"
          },
          {
            "title": "Qwen3-VL-Embedding and Qwen3-VL-Reranker: A Unified Framework for State-of-the-Art Multimodal Retrieval and Ranking",
            "url": "https://arxiv.org/pdf/2601.04720"
          },
          {
            "title": "Qwen3-Embedding-8B - Model Info, Parameters, Benchmarks - SiliconFlow\"",
            "url": "https://www.siliconflow.com/models/qwen3-embedding-8b"
          }
        ]
      },
      "Based on the search results, here's what I found about the Qwen3-Embedding-8B embedding model evaluation:\n\n## Benchmark Performance\n\nThe 8B size embedding model ranks No.1 in the MTEB multilingual leaderboard (as of June 5, 2025, score 70.58). Additionally, Qwen3-Embedding-8B (70.6 MTEB) surpasses all API models including OpenAI (64.6) and Google (68.3).\n\n## Model Capabilities\n\nThe Qwen3 Embedding series represents significant advancements in multiple text embedding and ranking tasks, including text retrieval, code retrieval, text classification, text clustering, and bitext mining. The series inherits the exceptional multilingual capabilities, long-text understanding, and reasoning skills of its foundational model.\n\n## Related Multimodal Variant\n\nThere is also a multimodal variant: Qwen3-VL-Embedding-8B attains an overall score of 77.8 on MMEB-V2, ranking first among all models (as of January 8, 2025).\n\n## Market Impact\n\nThe gap reversed in 2025-2026, indicating that open-source models like Qwen3-Embedding-8B have now surpassed proprietary API-based embedding solutions in performance benchmarks during this period."
    ],
    "durationSeconds": 6.376005888999993,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "65056cb5-7006-40fc-ab05-f97836689584",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-30T07:25:10.049Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FUYGAypmNjUPQiSvkG56fY`</summary>

```json
{
  "query": "\"adaptive attack\" \"conformal prediction\" adversarial robustness evaluation worst-case 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1049fc55-f412-4450-b02a-04c04de974bf",
  "isSidechain": false,
  "requestId": "req_011CbYMX9wnY5x4pztgZk2Pk",
  "type": "assistant",
  "uuid": "0301abef-d000-4f7c-843e-132cdbccad80",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuXwAgMF6h8PQ3tHuNQrnG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 964,
      "cache_read_input_tokens": 29331,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 964,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 29331,
          "cache_creation_input_tokens": 964,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 964
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

_source line 40 · 2026-05-30T07:25:16.895Z_

<details><summary>↩ Tool result · `toolu_01FUYGAypmNjUPQiSvkG56fY`</summary>

```text
Web search results for query: ""adaptive attack" "conformal prediction" adversarial robustness evaluation worst-case 2025 2026"

Links: [{"title":"Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability | OpenReview","url":"https://openreview.net/forum?id=Oty1LQrnFc"},{"title":"Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://arxiv.org/pdf/2506.07804"},{"title":"Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0031320325007113"},{"title":"Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://arxiv.org/html/2506.07804v1"},{"title":"[2506.07804] Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://arxiv.org/abs/2506.07804"},{"title":"Probabilistically robust conformal prediction","url":"https://arxiv.org/pdf/2307.16360"},{"title":"How Worst-Case Are Adversarial Attacks? Linking Adversarial and Perturbation Robustness","url":"https://arxiv.org/html/2601.14519"}]

I found several recent papers and results related to adaptive attacks, conformal prediction, and adversarial robustness evaluation. Here's a summary of the key findings:

## Recent Work on Adaptive Attacks and Conformal Prediction

A recent study developed an adversarial attack method termed OPSA (OPtimal Size Attack), designed to reduce the efficiency of conformal prediction at any significance level by maximizing model uncertainty without requiring coverage guarantees. This work also introduced OPSA-AT (Adversarial Training), a defense strategy that integrates OPSA within a novel conformal training paradigm.

## Verifiably Robust Conformal Prediction

A study on Verifiably Robust Conformal Prediction (VRCP) recovers conformal prediction's probabilistic guarantees under adversarial attacks. VRCP combines CP with neural network verification.

## Probabilistically Robust Conformal Prediction

Another approach studies probabilistically robust conformal prediction (PRCP) which ensures robustness to most perturbations around clean input examples, generalizing standard CP and adversarially robust CP to achieve better trade-offs between nominal performance and robustness.

## Worst-Case Analysis

Adversarial robustness research has traditionally focused on worst-case perturbations to identify model vulnerabilities, with white-box adversarial attacks also widely employed as safety-oriented stress tests, though their validity as proxies for safety has been questioned due to limited realism and weak connection to naturally occurring perturbations.

These results are from 2025-2026 and represent current research directions in combining adaptive attacks with conformal prediction for robust model evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0301abef-d000-4f7c-843e-132cdbccad80",
  "isSidechain": false,
  "promptId": "a45afd59-6eac-4f72-8319-52cc86d3dd24",
  "type": "user",
  "uuid": "6987d18a-881c-41bf-abfb-306d31101b95",
  "toolUseResult": {
    "query": "\"adaptive attack\" \"conformal prediction\" adversarial robustness evaluation worst-case 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PvDi65DM8azbcPBpY1wMXc",
        "content": [
          {
            "title": "Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability | OpenReview",
            "url": "https://openreview.net/forum?id=Oty1LQrnFc"
          },
          {
            "title": "Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability",
            "url": "https://arxiv.org/pdf/2506.07804"
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
            "title": "[2506.07804] Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability",
            "url": "https://arxiv.org/abs/2506.07804"
          },
          {
            "title": "Probabilistically robust conformal prediction",
            "url": "https://arxiv.org/pdf/2307.16360"
          },
          {
            "title": "How Worst-Case Are Adversarial Attacks? Linking Adversarial and Perturbation Robustness",
            "url": "https://arxiv.org/html/2601.14519"
          }
        ]
      },
      "I found several recent papers and results related to adaptive attacks, conformal prediction, and adversarial robustness evaluation. Here's a summary of the key findings:\n\n## Recent Work on Adaptive Attacks and Conformal Prediction\n\nA recent study developed an adversarial attack method termed OPSA (OPtimal Size Attack), designed to reduce the efficiency of conformal prediction at any significance level by maximizing model uncertainty without requiring coverage guarantees. This work also introduced OPSA-AT (Adversarial Training), a defense strategy that integrates OPSA within a novel conformal training paradigm.\n\n## Verifiably Robust Conformal Prediction\n\nA study on Verifiably Robust Conformal Prediction (VRCP) recovers conformal prediction's probabilistic guarantees under adversarial attacks. VRCP combines CP with neural network verification.\n\n## Probabilistically Robust Conformal Prediction\n\nAnother approach studies probabilistically robust conformal prediction (PRCP) which ensures robustness to most perturbations around clean input examples, generalizing standard CP and adversarially robust CP to achieve better trade-offs between nominal performance and robustness.\n\n## Worst-Case Analysis\n\nAdversarial robustness research has traditionally focused on worst-case perturbations to identify model vulnerabilities, with white-box adversarial attacks also widely employed as safety-oriented stress tests, though their validity as proxies for safety has been questioned due to limited realism and weak connection to naturally occurring perturbations.\n\nThese results are from 2025-2026 and represent current research directions in combining adaptive attacks with conformal prediction for robust model evaluation."
    ],
    "durationSeconds": 6.840742630000008,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0301abef-d000-4f7c-843e-132cdbccad80",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-30T07:25:19.002Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XtNQsB4we4xd6rmU6bnrNy`</summary>

```json
{
  "query": "Lipschitz constant cosine similarity embedding space robustness certification adversarial NLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6987d18a-881c-41bf-abfb-306d31101b95",
  "isSidechain": false,
  "requestId": "req_011CbYMY1RMM9PAmRCtbATa8",
  "type": "assistant",
  "uuid": "894fab3b-789f-40e4-ba95-f93f19f15014",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WtG3urT25CWg3DB4L8dp9K",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 849,
      "cache_read_input_tokens": 30295,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 849,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 30295,
          "cache_creation_input_tokens": 849,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 849
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

_source line 42 · 2026-05-30T07:25:30.909Z_

<details><summary>↩ Tool result · `toolu_01XtNQsB4we4xd6rmU6bnrNy`</summary>

```text
Web search results for query: "Lipschitz constant cosine similarity embedding space robustness certification adversarial NLP 2025"

Links: [{"title":"[2510.25130] Lipschitz-aware Linearity Grafting for Certified Robustness","url":"https://arxiv.org/abs/2510.25130"},{"title":"arXiv:2506.23977v1 [cs.LG] 30 Jun 2025","url":"https://arxiv.org/pdf/2506.23977"},{"title":"Published as a conference paper at ICLR 2025 CERTIFIED ROBUSTNESS UNDER BOUNDED","url":"https://arxiv.org/pdf/2501.13676"},{"title":"Certified Robust Models with Slack Control and Large Lipschitz Constants","url":"https://arxiv.org/pdf/2309.06166"},{"title":"Lipschitz-aware Linearity Grafting for Certified Robustness","url":"https://arxiv.org/pdf/2510.25130"},{"title":"Adversarial Robustness of Neural Networks from the Perspective of Lipschitz Calculus: A Survey | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3648351"},{"title":"[2310.00116] Certified Robustness via Dynamic Margin Maximization and Improved Lipschitz Regularization","url":"https://arxiv.org/abs/2310.00116"},{"title":"Adversarial Robustness of Neural Networks from the ...","url":"https://dl.acm.org/doi/pdf/10.1145/3648351"}]

Based on the search results, I found several relevant recent works on Lipschitz constants, robustness certification, and adversarial NLP:

## Key Findings

**Certified Robustness and Lipschitz Constants in NLP:**

A method called LipsLev can verify NLP models for k > 1 with verified accuracy results including 13.93% for AG-News, 1.83% for SST-2, 75.33% for Fake-News and 6.80% for IMDB. This work, published as a conference paper at ICLR 2025, addresses certified robustness under bounded perturbations in NLP tasks.

**Lipschitz Constraints for Certified Robustness:**

Lipschitz constant is a fundamental property in certified robustness, as smaller values imply robustness to adversarial examples when a model is confident in its prediction. One recent approach involves grafting linearity into dominant neurons based on an adversarially pre-trained model and fine-tuning with existing adversarial training schemes, which tightens the local Lipschitz constant and enhances certified robustness.

**Broader Context:**

Many approaches have been proposed to improve robustness, such as designing architectures with better robustness properties like Lipschitz-capped networks, or developing training algorithms that increase the margin in the output space while regularizing the Lipschitz constant along vulnerable directions.

The search results show active recent work in 2025 combining Lipschitz theory with certified robustness for both vision and NLP domains.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "894fab3b-789f-40e4-ba95-f93f19f15014",
  "isSidechain": false,
  "promptId": "a45afd59-6eac-4f72-8319-52cc86d3dd24",
  "type": "user",
  "uuid": "b563ca53-91e1-47fa-a39c-032740c23044",
  "toolUseResult": {
    "query": "Lipschitz constant cosine similarity embedding space robustness certification adversarial NLP 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HiLa2mLHcHehwPprD4J26b",
        "content": [
          {
            "title": "[2510.25130] Lipschitz-aware Linearity Grafting for Certified Robustness",
            "url": "https://arxiv.org/abs/2510.25130"
          },
          {
            "title": "arXiv:2506.23977v1 [cs.LG] 30 Jun 2025",
            "url": "https://arxiv.org/pdf/2506.23977"
          },
          {
            "title": "Published as a conference paper at ICLR 2025 CERTIFIED ROBUSTNESS UNDER BOUNDED",
            "url": "https://arxiv.org/pdf/2501.13676"
          },
          {
            "title": "Certified Robust Models with Slack Control and Large Lipschitz Constants",
            "url": "https://arxiv.org/pdf/2309.06166"
          },
          {
            "title": "Lipschitz-aware Linearity Grafting for Certified Robustness",
            "url": "https://arxiv.org/pdf/2510.25130"
          },
          {
            "title": "Adversarial Robustness of Neural Networks from the Perspective of Lipschitz Calculus: A Survey | ACM Computing Surveys",
            "url": "https://dl.acm.org/doi/10.1145/3648351"
          },
          {
            "title": "[2310.00116] Certified Robustness via Dynamic Margin Maximization and Improved Lipschitz Regularization",
            "url": "https://arxiv.org/abs/2310.00116"
          },
          {
            "title": "Adversarial Robustness of Neural Networks from the ...",
            "url": "https://dl.acm.org/doi/pdf/10.1145/3648351"
          }
        ]
      },
      "Based on the search results, I found several relevant recent works on Lipschitz constants, robustness certification, and adversarial NLP:\n\n## Key Findings\n\n**Certified Robustness and Lipschitz Constants in NLP:**\n\nA method called LipsLev can verify NLP models for k > 1 with verified accuracy results including 13.93% for AG-News, 1.83% for SST-2, 75.33% for Fake-News and 6.80% for IMDB. This work, published as a conference paper at ICLR 2025, addresses certified robustness under bounded perturbations in NLP tasks.\n\n**Lipschitz Constraints for Certified Robustness:**\n\nLipschitz constant is a fundamental property in certified robustness, as smaller values imply robustness to adversarial examples when a model is confident in its prediction. One recent approach involves grafting linearity into dominant neurons based on an adversarially pre-trained model and fine-tuning with existing adversarial training schemes, which tightens the local Lipschitz constant and enhances certified robustness.\n\n**Broader Context:**\n\nMany approaches have been proposed to improve robustness, such as designing architectures with better robustness properties like Lipschitz-capped networks, or developing training algorithms that increase the margin in the output space while regularizing the Lipschitz constant along vulnerable directions.\n\nThe search results show active recent work in 2025 combining Lipschitz theory with certified robustness for both vision and NLP domains."
    ],
    "durationSeconds": 11.900062909,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "894fab3b-789f-40e4-ba95-f93f19f15014",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-30T07:27:14.055Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information from my pre-research. Let me synthesize what I've found and give a thorough evaluation of the experimental design.

Key findings from my research:

1. **RobustRAG (SaTML 2026)**: Uses 3 datasets (RealtimeQA, NQ, Biography Generation), 3 LLMs (Mistral-7B, Llama-2-7B, GPT-3.5). Achieves 71% clean accuracy and 38% certifiable robust accuracy on RealtimeQA.

2. **ReliabilityRAG (NeurIPS 2025)**: Uses graph-theoretic MIS approach, evaluated on robustness and long-form generation.


3. **LP-CP (NeurIPS 2025)**: Validated on 3 benchmark datasets, provides closed-form worst-case quantiles.

4. **TRAQ (NAACL 2024)**: Tested across 4 datasets (NQ, TriviaQA, SQuAD-1, BioASQ) with 1000 samples each, split into calibration, optimization, and testing phases, using GPT-3.5 and Llama-2-7B.

5. **PoisonedRAG (USENIX Security 2025)**: Demonstrates high attack success rates on NQ and other datasets.

6. **CorruptRAG**: Offers a more practical single-document poisoning approach.

7. **RAGDefender (ACSAC 2025)**: Lightweight post-retrieval clustering defense mechanism.

8. **Benchmarking (arXiv 2505.18543)**: Comprehensive evaluation across multiple datasets, attacks, and defenses in a unified framework.

9. **Qwen3-Embedding-8B**: Top-performing open-source embedding model on multilingual benchmarks.

Looking at the experimental design, the proposal covers standard benchmark datasets and includes both multi-document and single-document attack variants, with multiple embedding models being evaluated.

Now I'm noticing a critical gap: the proposal mentions RPS from ICLR 2025 in related work but doesn't actually include it as a baseline, which is problematic since RPS directly addresses conformal prediction under data poisoning.  While RPS targets calibration-time poisoning rather than test-time retrieval corruption, the proposal should at least explain this distinction. I'm also considering whether the dataset choices are sufficient—RealtimeQA would strengthen direct comparison with RobustRAG, and TriviaQA would help with TRAQ comparisons, though the current selection of NQ, HotpotQA, and MS-MARCO is reasonable. The calibration set ablation covering {100, 300, 500, 1000, 2000} is solid and includes TRAQ's setting of 300.

On evaluation metrics, I notice the proposal lacks explicit attack success rate (ASR), which is standard in poisoning papers—the "certified robust accuracy on non-abstained queries" is related but should be stated directly for comparability. For fairness in compute comparisons, I should account for the multiple LLM calls required by RobustRAG's isolate-then-aggregate approach, not just wall-clock time and API calls. The Contriever embedding model from 2022 is somewhat dated for 2026, though it's presented alongside newer models so it's a minor concern. I also need to clarify whether the proposal addresses both black-box and white-box variants of PoisonedRAG.

The adaptive attack construction needs more specificity—right now it's vague about how the adversary with full defense knowledge is actually designed. There are real feasibility concerns around GPT-4o API costs scaling across three datasets with multiple attack settings and parameter combinations, plus the computational demands of the 8B embedding model. A critical gap is cross-attack transferability: I should test whether calibration against PoisonedRAG generalizes to other attacks like CorruptRAG, which matters for real-world robustness. TriviaQA is also missing as a dataset, which is relevant since TRAQ uses it.

Looking back at the baselines, I notice C-RAG and Conformal-RAG are mentioned in related work but not actually included in the comparison, even though they're directly relevant CP-for-RAG methods that should be evaluated against. RPS from ICLR 2025 is the most compelling missing baseline since it directly addresses conformal prediction under poisoning with a partition-and-vote approach—even though it targets calibration rather than retrieval corruption, demonstrating its limitations on RAG would strongly motivate the proposed method. I should also add ASR (Attack Success Rate) to the evaluation metrics, which is the standard poisoning paper metric I'm currently missing alongside the coverage, abstention rate, and robustness measures already planned. Even though the proposal uses "coverage," reviewers who come from the security side will expect ASR. Beyond just AUC, I should consider showing the full Pareto frontier of selective accuracy versus coverage, and how coverage varies across queries of different difficulty levels. The proposal does have an accuracy-abstention tradeoff AUC that partially addresses this concern.

For feasibility, the embedding computation with Qwen3-Embedding-8B is manageable through batching across GPUs, though I need to clarify whether poisoning attacks require re-embedding the entire corpus or just the injected documents. LLM inference costs could add up quickly with GPT-4o across multiple datasets, queries, and attack conditions, though it's still within reasonable bounds. Calibration is computationally cheap, and the attack execution itself is straightforward.

The main concern I'm flagging is that C-RAG is missing from the baselines—including it alongside TRAQ would strengthen the argument that conformal prediction methods fail under adversarial retrieval, since a reviewer could otherwise dismiss the findings as specific to TRAQ rather than a fundamental limitation of the approach.

RPS is also a critical omission since it's the closest related work on conformal prediction under poisoning, and reviewers will definitely ask why it wasn't compared even though it targets a different threat model.

Beyond the baselines, I need to clarify which PoisonedRAG variant (black-box or white-box) the evaluation uses since they have very different attack success rates, ensure ASR is reported alongside the conformal prediction metrics for security-focused reviewers, and test cross-attack robustness by calibrating under one attack and evaluating under another to better reflect real deployment scenarios.

The RealtimeQA dataset is a minor gap since RobustRAG uses it for main results, so including it would enable more direct comparison.

Actually, stepping back—I should distinguish between what's genuinely critical versus what's nice-to-have. The proposal is fairly comprehensive, so the real gaps are C-RAG and RPS as baselines, specifying the PoisonedRAG variant, and reporting ASR. Cross-attack robustness and RealtimeQA are valuable but less essential.

On the poisoning ratio front, the proposal uses ρ as a fraction of poisoned documents in the top-k, which is a cleaner parameterization than testing discrete counts. That works fine. But there's a subtlety with the certified robust accuracy target—if the method abstains heavily on difficult queries, it could artificially inflate accuracy on the remaining set. The proposal mentions tracking the accuracy-abstention tradeoff and its AUC, which is the right approach, though I need to verify they're reporting both metrics together rather than just the final number.

The threat model parameters (ρ, ε) are treated as fixed defense inputs rather than quantities to estimate, which aligns with RobustRAG's paradigm and is standard for certified defenses. That's reasonable.

The real crux is the Lipschitz constant bound for cosine similarity on normalized embeddings—if that O(2/k) bound is too loose, the worst-case quantiles become vacuous and the method abstains on everything. The proposal acknowledges this risk and plans to derive the analytic bound, empirically measure how tight it actually is, and report the gap between theory and practice.

This is a genuine feasibility concern rather than just a research risk. The key question is whether a single poisoned document's embedding shift under ε perturbation, combined with ρ fraction of documents being replaced, actually produces the claimed O(ρ) change in mean pairwise cosine similarity. The O(2/k) Lipschitz constant with respect to single-document replacement seems plausible, but the tightness of this bound will determine whether the approach yields useful guarantees in practice. So the worst-case perturbation bound works out to O(ρ), which is manageable—the Lipschitz analysis holds up and the feasibility risk isn't prohibitive. Now I'm ready to wrap up my assessment and flag the key experimental gaps that need addressing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b563ca53-91e1-47fa-a39c-032740c23044",
  "isSidechain": false,
  "requestId": "req_011CbYMZ3JEmS2QhH6YKpVNZ",
  "type": "assistant",
  "uuid": "425a19fb-4bea-4c54-a646-015bc73d5a07",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H2qaUJmZMueqzuH1MtMNEL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 863,
      "cache_read_input_tokens": 31144,
      "output_tokens": 9767,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 863,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9767,
          "cache_read_input_tokens": 31144,
          "cache_creation_input_tokens": 863,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 863
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

_source line 44 · 2026-05-30T07:29:04.530Z_

Now I have sufficient information to give a thorough assessment. Let me compile my findings.

---

【状态】: 有缺陷待补救

【前置调研发现】
- **RobustRAG (SaTML 2026, arXiv:2405.15556)**: 实验使用 3 数据集（RealtimeQA, NQ, Biography Generation）、3 LLM（Mistral-7B, Llama-2-7B, GPT-3.5）。主要指标为 clean accuracy 和 certified robust accuracy（RealtimeQA 上 71% clean / 38% certified）。采用 isolate-then-aggregate，需要多次 LLM 推理。
- **ReliabilityRAG (NeurIPS 2025, arXiv:2509.23519)**: 基于图论 MIS 方法，使用 reliability-weighted documents，实验评估 robustness 和 benign accuracy，并特别在 long-form generation 上展示优势。报告 certified robust accuracy 和 benign accuracy。
- **TRAQ (NAACL 2024, arXiv:2307.04642)**: 使用 4 数据集（NQ, TriviaQA, SQuAD-1, BioASQ），1000 样本/数据集，300/300/400 (calibration/optimization/test) 划分。使用 GPT-3.5 和 Llama-2-7B。主要指标为 coverage 和 prediction set size。
- **PoisonedRAG (USENIX Security 2025, arXiv:2402.07867)**: 在 NQ 上 97% ASR、HotpotQA 上 99% ASR、MS-MARCO 上 91% ASR。区分 black-box 和 white-box 两种攻击变体，两者 ASR 差异显著。
- **CorruptRAG (arXiv:2504.03957)**: 单文档注入攻击，更实际的威胁模型。在多数据集上实验验证。
- **RAG Security Bench (arXiv:2505.18543)**: 统一评测框架，覆盖 5 数据集（+10 扩展变体）、13 种攻击、7 种防御。发现现有攻击在扩展数据集上效果显著下降，现有防御普遍不足。
- **LP-CP (NeurIPS 2025, arXiv:2502.14105)**: 在 3 个 benchmark 数据集上验证。将分布偏移建模为 LP ambiguity set，通过 score function 传播实现一维量化。
- **C-RAG (ICML 2024)**: 提供 conformal generation risk bounds，与 TRAQ 并列为 CP-for-RAG 两大代表工作。
- **RPS (ICLR 2025 Spotlight)**: 用 partition-and-vote + smoothed scores 处理 calibration 数据投毒下的 conformal prediction，是目前最接近"CP + 投毒"交叉领域的工作。
- **Qwen3-Embedding-8B**: MTEB multilingual 排行榜第一（70.58 分），超越所有 API 模型，8B 参数量需要 ~16GB GPU 显存。

- **调研总结**: 该领域当前实验标准要求：(1) 至少 3 个 QA 数据集 + 2-3 个 LLM；(2) 同时报告 clean 和 adversarial 两种设置下的指标；(3) certified defense 论文需报告 certified robust accuracy；(4) 攻击论文使用 ASR 作为核心指标，防御论文也需对照报告 ASR；(5) 审稿人普遍期望 adaptive attack 评估和 ablation on threat model parameters。

---

【缺陷 1】
- 类别: baseline 不足
- 问题: Proposal 的 baselines 中缺少 **C-RAG (ICML 2024)**。C-RAG 是 related work 中明确提到的两个 CP-for-RAG 代表方法之一（与 TRAQ 并列），提供 conformal generation risk bounds。当前 baselines 只有 TRAQ 来演示"CP 方法在 adversarial retrieval 下失效"，仅一个数据点说服力不足。审稿人很可能会问："TRAQ 的 coverage 在攻击下崩了，但 C-RAG 基于 risk bound 的方法可能更鲁棒——你为什么没测？"
- 严重度: 可补救
- 补救方案: 将 C-RAG 加入 baselines，在相同攻击条件下测其 coverage / risk bound 是否同样崩溃。这会使"现有 CP-for-RAG 方法均不处理 adversarial retrieval"的论证从一个数据点变为两个独立数据点，显著增强说服力。C-RAG 代码已公开，实验成本低。
- 调研依据: C-RAG (ICML 2024) 与 TRAQ 是该领域仅有的两个 CP-for-RAG 工作，在 proposal 自己的 related work 中并列提及但未纳入 baseline。

【缺陷 2】
- 类别: baseline 不足
- 问题: Proposal 的 baselines 中缺少 **RPS (ICLR 2025 Spotlight)**。RPS 是目前唯一在"conformal prediction + data poisoning"交叉领域的主流工作（partition-and-vote + smoothed scores），在 related work 中被明确提及。虽然 RPS 针对 calibration-time 投毒而非 test-time retrieval corruption，但作为最接近的现有方法，审稿人几乎一定会要求对比。不将其纳入 baseline 或至少给出实验排除理由，是明显的审稿漏洞。
- 严重度: 可补救
- 补救方案: 两种选择（推荐方案 1）：(1) 将 RPS 作为 baseline 纳入实验，在 test-time retrieval corruption 攻击下运行 RPS，展示其 partition-and-vote 机制在此场景下性能退化（预期结果：RPS 假设 calibration set 被投毒，但 RAG 投毒发生在 test-time retrieval，所以 RPS 的 robustness guarantee 不适用），从而明确区分两种投毒模型。(2) 如果实验成本太高，至少在论文中给出详细的理论分析说明 RPS 为什么不适用于 test-time retrieval corruption，而非完全不提。
- 调研依据: RPS (ICLR 2025 Spotlight) 是 LP-CP 之外最重要的 robust CP 工作，proposal 自己在 related work 中提到但 baseline 中遗漏。

【缺陷 3】
- 类别: 评估方案缺陷
- 问题: Proposal 的评估指标中缺少 **Attack Success Rate (ASR)**。ASR 是 RAG 投毒防御领域的核心标准指标（PoisonedRAG 报告 97% ASR on NQ，CorruptRAG 也以 ASR 为主要指标，RAG Security Bench 使用 ASR 作为统一指标）。Proposal 使用 coverage 和 certified robust accuracy 来衡量防御效果，这在 CP 社区是合理的，但对于来自安全/对抗鲁棒性背景的审稿人（AAAI 审稿人群体多样），缺少 ASR 会造成可比性障碍。
- 严重度: 可补救
- 补救方案: 在评估指标中显式加入 ASR（对于非 abstain 的查询，攻击者成功诱导错误答案的比例）。对于 LP-RAG-Abstain，可以同时报告 (1) overall ASR（含 abstain queries，abstain 视为攻击失败），(2) conditional ASR（仅在非 abstain queries 中的 ASR）。这样既兼容安全社区的评估习惯，又能展示 abstention 机制的价值——overall ASR 应显著低于 baseline 方法。
- 调研依据: PoisonedRAG (USENIX Security 2025)、CorruptRAG (arXiv:2504.03957)、RAG Security Bench (arXiv:2505.18543) 均以 ASR 为核心评估指标。

【缺陷 4】
- 类别: 实验设计不足
- 问题: Proposal 使用 PoisonedRAG 作为攻击之一，但未指定使用其 **black-box 还是 white-box 变体**。根据 PoisonedRAG 论文，两种变体的攻击方式和 ASR 差异显著（black-box 使用 LLM 生成毒文档，white-box 使用梯度优化嵌入）。对于 LP-RAG-Abstain 而言，white-box 攻击能直接优化嵌入空间中的位置，可能对基于 cosine similarity 的 score function 构成更大挑战。如果只测 black-box 而不测 white-box，审稿人会认为评估不充分。
- 严重度: 可补救
- 补救方案: 明确指定评估 PoisonedRAG 的 **both** 变体：(1) black-box（LLM-generated poisoned passages）——更实际的攻击场景；(2) white-box（gradient-optimized embeddings）——更强的攻击，直接优化嵌入空间，与 LP-RAG-Abstain 的 ε bound 直接相关。在两种变体下分别报告所有指标，展示方法在不同攻击强度下的鲁棒性。
- 调研依据: PoisonedRAG (USENIX Security 2025) 明确区分 black-box 和 white-box 两种攻击设置，其论文中两者结果差异显著。

【缺陷 5】
- 类别: 实验设计不足
- 问题: Proposal 缺少 **cross-attack robustness 评估**。当前实验设计是分别在 PoisonedRAG 和 CorruptRAG 攻击下评估，但未考虑一个关键的实际部署问题：如果 (ρ₀, ε₀) 是基于某种攻击类型的假设设定的，系统在面对未知类型的攻击时表现如何？例如，在 PoisonedRAG（多文档注入）的 ρ 假设下，系统面对 CorruptRAG（单文档但高质量注入）时是否仍然有效？这对于论文的实际价值主张（"Safe Silence" guarantee）至关重要。
- 严重度: 可补救
- 补救方案: 增加一组 cross-attack 实验：(1) 在 PoisonedRAG 的 ρ 参数下校准，在 CorruptRAG 攻击下测试；(2) 反之亦然。展示 LP-RAG-Abstain 的覆盖保证是否在跨攻击类型时仍然成立（理论上应该成立，因为保证是参数化于 (ρ, ε) 而非特定攻击类型，但实验验证必不可少）。这也能展示方法的通用性优势。
- 调研依据: RAG Security Bench (arXiv:2505.18543) 的统一评估框架覆盖 13 种攻击，发现不同攻击类型间效果差异大；基于领域实验规范判断，跨攻击泛化是审稿人常见关注点。

【缺陷 6】
- 类别: 评估方案缺陷
- 问题: Proposal 使用 NQ、HotpotQA、MS-MARCO 三个数据集，但 **缺少 RobustRAG 使用的 RealtimeQA 数据集**。RobustRAG 的主要结果（71% clean / 38% certified robust accuracy）报告在 RealtimeQA 上。如果 proposal 声称 "Exceed RobustRAG's 26–36% certified robust accuracy" 但不在同一数据集上比较，可比性会受质疑。
- 严重度: 可补救
- 补救方案: 建议增加 RealtimeQA 作为第四个数据集，至少在主实验中使用，以确保与 RobustRAG 在相同数据集上直接比较。RealtimeQA 数据集公开可用，增加实验成本不大。如果确实无法添加，至少确保在 NQ 上（RobustRAG 也使用 NQ）进行详尽的头对头比较，并在论文中注明 RobustRAG 在 NQ 上的具体数字作为对照。
- 调研依据: RobustRAG (SaTML 2026) 在 RealtimeQA、NQ、Biography Generation 三个数据集上报告结果，RealtimeQA 是其主结果数据集。

【缺陷 7】
- 类别: 实验设计不足
- 问题: Proposal 的 adaptive attack evaluation 描述过于笼统——"Design adversary with full knowledge of the defense (pairwise cosine agreement score), attempting to maximize embedding distance among poisoned documents within ε constraint"。未明确 adaptive attack 的具体构造方式（优化目标函数是什么？用什么算法求解？是否考虑了同时优化 retrieval ranking 和 score manipulation 的联合攻击？）。近期研究（如 OPSA）表明，针对 conformal prediction 的 adaptive attack 设计需要仔细考虑优化目标。如果 adaptive attack 设计不够强，审稿人会质疑 robustness claim 的可信度。
- 严重度: 可补救
- 补救方案: 明确 adaptive attack 的设计：(1) **优化目标**: 在 ε-ball 内选择毒文档嵌入，使 pairwise cosine agreement score 最大化（即让毒文档在嵌入空间中尽可能接近干净文档，从而逃避检测），或最小化该 score（即最大化检测难度的另一方向），取两者中对防御更不利的结果；(2) **约束**: ‖e_poison - e_original‖₂ ≤ ε，且 ρk 个毒文档必须进入 top-k retrieval；(3) **求解算法**: 使用 PGD（projected gradient descent）在嵌入空间中优化；(4) **dual attack**: 同时尝试"让毒文档看起来正常"和"让 score 分布看起来正常"两种策略。报告 adaptive attack 下的 coverage 是否仍满足理论保证。
- 调研依据: OPSA (arXiv:2506.07804) 针对 conformal prediction 设计了专门的 adaptive attack；RobustRAG 论文中也包含 adaptive attack evaluation。

【缺陷 8】
- 类别: 可行性问题
- 问题: 完整实验矩阵的计算成本可能被低估。粗略估算：3 数据集 × 2 攻击（+各自变体）× 3 嵌入模型 × 2 LLM × 7 ablation 维度（每维 4-5 个取值）× (ρ, ε) heatmap（≥25 个网格点）= 数千组实验配置。其中 GPT-4o 的 API 成本和 Qwen3-Embedding-8B（8B 参数）的 GPU 需求可能构成瓶颈。如果不做优先级排序，可能导致实验周期过长或被迫削减实验规模。
- 严重度: 可补救
- 补救方案: 建议采用分层实验策略：(1) **核心实验**（必须完成）: 主嵌入模型 (Qwen3-Embedding-8B) + 主 LLM (Llama-3.1-8B) + 所有数据集 + 所有攻击 + 所有 baselines → 约 60-100 组配置；(2) **泛化实验**（次优先）: 在 1 个数据集 (NQ) 上测试所有嵌入模型 × LLM 组合；(3) **ablation 实验**（聚焦关键变量）: ρ/ε/k/α 在主配置上进行，calibration set size 和 LP-CP vs. Bonferroni 在 1 个数据集上进行即可；(4) **heatmap**:仅在主配置上生成。这样可将总实验量控制在可管理范围内（~300-500 组），同时保留所有关键结论的支撑。对于 GPT-4o，可考虑将其仅用于核心实验和泛化实验，ablation 实验仅用 Llama-3.1-8B。
- 调研依据: 基于领域实验规范判断；TRAQ 使用 1000 样本/数据集，RobustRAG 使用 3 数据集 × 3 LLM 的矩阵但未做全组合 ablation。

---

**总结**: 该 proposal 的实验设计整体框架扎实——数据集选择合理、baseline 覆盖了主要类别（CP-for-RAG、certified defense、heuristic defense、naive baseline）、ablation 设计全面、评估指标覆盖了 CP 社区关心的核心量。以上 8 个缺陷均为**可补救**的完善性问题，无方向性致命缺陷。其中缺陷 1（补 C-RAG baseline）、缺陷 3（补 ASR 指标）、缺陷 4（明确攻击变体）优先级最高，修复成本低但对审稿人说服力影响大；缺陷 2（RPS baseline）和缺陷 7（adaptive attack 细化）次之；缺陷 5、6、8 属于锦上添花的完善项。

Sources:
- [RobustRAG: Certifiably Robust RAG against Retrieval Corruption](https://arxiv.org/abs/2405.15556)
- [ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search](https://arxiv.org/abs/2509.23519)
- [TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction](https://arxiv.org/abs/2307.04642)
- [PoisonedRAG: Knowledge Corruption Attacks to RAG of LLMs](https://arxiv.org/abs/2402.07867)
- [CorruptRAG: Practical Poisoning Attacks against RAG](https://arxiv.org/abs/2504.03957)
- [Benchmarking Poisoning Attacks against RAG](https://arxiv.org/abs/2505.18543)
- [LP-CP: Conformal Prediction under Lévy-Prokhorov Distribution Shifts](https://arxiv.org/abs/2502.14105)
- [Qwen3-Embedding-8B on Hugging Face](https://huggingface.co/Qwen/Qwen3-Embedding-8B)
- [Learning Conformal Abstention Policies](https://arxiv.org/abs/2502.06884)
- [Enhancing Adversarial Robustness with Conformal Prediction (OPSA)](https://arxiv.org/abs/2506.07804)
- [RAGDefender GitHub](https://github.com/SecAI-Lab/RAGDefender)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "425a19fb-4bea-4c54-a646-015bc73d5a07",
  "isSidechain": false,
  "requestId": "req_011CbYMZ3JEmS2QhH6YKpVNZ",
  "type": "assistant",
  "uuid": "64826d87-f675-4421-a6d5-b5dcf1743945",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H2qaUJmZMueqzuH1MtMNEL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 863,
      "cache_read_input_tokens": 31144,
      "output_tokens": 9767,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 863,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9767,
          "cache_read_input_tokens": 31144,
          "cache_creation_input_tokens": 863,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 863
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
  "lastPrompt": "# Conformal Abstention for RAG under Corpus Poisoning via LP-Bounded Retrieval Shifts  ## Core Problem  How can a RAG system provide distribution-free, certified abstention guarantees on answer correc…",
  "leafUuid": "64826d87-f675-4421-a6d5-b5dcf1743945",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal abstention for poisoned RAG systems",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Conformal Abstention for RAG under Corpus Poisoning via LP-Bounded Retrieval Shifts  ## Core Problem  How can a RAG system provide distribution-free, certified abstention guarantees on answer correc…",
  "leafUuid": "64826d87-f675-4421-a6d5-b5dcf1743945",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Conformal abstention for poisoned RAG systems",
  "sessionId": "84c13c55-366d-4c46-b901-0f44d11301b4"
}
```

---
