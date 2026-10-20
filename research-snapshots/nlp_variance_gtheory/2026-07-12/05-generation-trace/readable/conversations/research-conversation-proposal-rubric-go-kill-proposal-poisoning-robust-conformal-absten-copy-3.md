# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Poisoning-Robust Conformal Absten

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/8c716a8b-ada0-4852-9192-47e334d69867.jsonl`
- **Structured JSON:** [`7ed7c40a481e8ecba5d9.json`](../../sessions/7e/7ed7c40a481e8ecba5d9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T07:47:47.365Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T07:47:47.365Z",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores\n\n## Core Problem\n\nRAG systems in adversarial environments (medical QA, legal retrieval, financial compliance) need distribution-free abstention guarantees when the retrieval corpus is poisoned. Corpus poisoning is a practical threat: CorruptRAG (arXiv 2025) achieves high attack success with a single injected document; PoisonedRAG (USENIX Security 2025) reaches 90%+ ASR with 5 documents. Existing conformal prediction methods for RAG (TRAQ, NAACL 2024; C-RAG, ICML 2024; Conformal-RAG, SIGIR 2025) assume benign retrieval—Chen et al. (arXiv:2603.16817, Mar 2026) demonstrated these guarantees break under distribution shift, producing vacuous outputs. Poisoning-robust CP (RPS, ICLR 2025 Spotlight) addresses calibration-set poisoning, not test-time retrieval corruption. Certified RAG defenses (RobustRAG, SaTML 2026; ReliabilityRAG, NeurIPS 2025) provide robust point estimates but no abstention mechanism or coverage certificates. The gap: no method provides distribution-free abstention guarantees for RAG under adversarial retrieval corruption.\n\n## Core Contribution and Theoretical Insight\n\nPRCA's central contribution is a **partition-induced reduction**: partitioning retrieved passages into disjoint groups and computing inter-group agreement deterministically reduces arbitrary test-time retrieval corruption to a bounded TV shift in the one-dimensional nonconformity score distribution. This bounded shift is absorbed by CRC (ICLR 2024) via inflated quantiles, yielding formal coverage certificates. This reduction—from high-dimensional adversarial corruption to one-dimensional bounded distributional shift—parallels the approach of Conformal Prediction under Lévy-Prokhorov Distribution Shifts (arXiv:2502.14105), which reduces high-dimensional shifts to one-dimensional score shifts via ambiguity sets.\n\n**Why not simply combine existing methods?** Three natural alternatives fail:\n\n(1) **RobustRAG + standard CP**: Running RobustRAG's isolate-then-aggregate to obtain a robust answer, then applying TRAQ/C-RAG for conformal abstention, fails because RobustRAG's aggregation transforms the output distribution in a poisoning-dependent manner. Nonconformity scores from clean calibration are no longer exchangeable with test-time scores under attack, and the magnitude of distributional shift is uncharacterized. PRCA explicitly bounds this shift via partition structure.\n\n(2) **Full-context self-consistency + CP**: Generating K answers from the same full retrieval set and using agreement as a conformal score (the approach of Conformal Abstention, arXiv:2405.01563) fails under poisoning because all K samples share the same poisoned context. The model may produce consistently wrong answers with high agreement, making the score blind to corruption. Partition isolates poisoned passages into a bounded number of groups, enabling detection.\n\n(3) **Logprob-based confidence + CP**: Using LLM token-level logprobabilities as nonconformity scores fails because adversarially crafted passages (e.g., via Semantic Chameleon's gradient-guided attacks, arXiv Mar 2026) are designed to appear authoritative, inflating model confidence on wrong answers. Logprob monotonicity with respect to correctness breaks under adversarial retrieval.\n\n**Partition is a theoretical necessity, not a design choice**: it is the structural mechanism that transforms uncharacterizable adversarial corruption into a bounded, quantifiable distributional shift that CRC can absorb.\n\n## Research Landscape\n\n**Conformal prediction for RAG:** TRAQ (NAACL 2024) and C-RAG (ICML 2024) established conformal prediction for RAG under benign retrieval. Conformal-RAG (SIGIR 2025) extends to group-conditional coverage. Chen et al. (arXiv:2603.16817, Mar 2026) showed all such methods produce vacuous prediction sets under distribution shift and retrieval corruption, but proposed no solution.\n\n**Certified RAG defenses:** RobustRAG (SaTML 2026) provides certified defense via isolate-then-aggregate, achieving certified robust accuracy on RealtimeQA/NQ. ReliabilityRAG (NeurIPS 2025) uses graph-theoretic MIS with NLI-based contradiction detection for provably robust document filtering. Both provide robust point estimates but no coverage certificates or abstention mechanism.\n\n**Poisoning-robust CP:** RPS (ICLR 2025 Spotlight) achieves poisoning-robust CP via smoothed scores and majority voting but assumes calibration-set poisoning—certificates do not transfer to test-time retrieval corruption.\n\n**Partition-based defenses:** RAGPart (arXiv:2512.24268, Dec 2025) uses document partitioning at the retrieval stage (fragment embeddings) to dilute poisoning. Three key differences from PRCA: (1) RAGPart operates at retrieval/embedding stage, PRCA at generation/calibration stage; (2) RAGPart outputs filtered retrieval sets, PRCA outputs {answer, abstain} decisions with coverage certificates; (3) they are complementary—RAGPart can preprocess retrieval before PRCA's certified abstention.\n\n**Adversarial aggregation:** The Consensus Trap (arXiv:2604.17139, Apr 2026) proves response-level majority voting fails when corrupted agents form a local majority. PRCA's majority answer output could face this risk, but: (a) PRCA's primary guarantee is the coverage certificate on the abstention decision, not the majority answer's correctness; (b) under the standard threat model k < n/2, the number of corrupted groups m = ceil(k/floor(n/K)) < K/2, so the honest majority is preserved.\n\n**Attack landscape:** PoisonedRAG (USENIX Security 2025), CorruptRAG (arXiv 2025), RSB Benchmark (May 2025, 13 attack methods × 7 defenses), Semantic Chameleon (arXiv Mar 2026, gradient-guided corpus-dependent attacks).\n\n**Distribution-shift-robust CP:** LP-shift framework (arXiv:2502.14105) reduces high-dimensional shifts to one-dimensional score shifts. PRCA's partition-induced TV bound is a specific instantiation for adversarial retrieval corruption.\n\nNo existing work combines conformal abstention with retrieval-poisoning robustness.\n\n## Proposed Approach\n\n**Step 1: Partition-and-Generate.** Partition top-n retrieved passages into K disjoint groups (random assignment). Generate a per-group answer via isolated LLM calls.\n\n**Step 2: Agreement Nonconformity Score.** For each group pair (i, j), compute NLI entailment probability e(i,j) = P(answer_i entails answer_j) using DeBERTa-v3-large (following ReliabilityRAG's NLI approach). Define:\n\ns = 1 − mean({e(i,j)} over all pairs)\n\nCritical properties: (1) **Monotonicity**: s increases with disagreement; higher s → more likely to abstain, satisfying CRC's monotone-loss requirement. (2) **Corruption-boundedness**: under k-poisoning, at most m = ceil(k/floor(n/K)) groups are corrupted, affecting at most m(K−1) of C(K,2) pairwise comparisons, yielding bounded perturbation to s.\n\n**Toward tighter bounds:** The worst-case TV ≤ m/K is a combinatorial upper bound. Because s is a mean of bounded pairwise scores, the actual perturbation from m corrupted groups may be dampened. We will empirically estimate the actual TV distance between clean and poisoned score CDFs (via bootstrap) and compare against the theoretical bound, reporting the tightness ratio. Exploring concentration-based bounds (leveraging the mean structure) is a concrete research direction.\n\n**Clean-condition variance mitigation:** If different passage groups cover different answer facets, clean-condition agreement variance inflates s and may cause excessive abstention. NLI-based semantic entailment (rather than exact match) is robust to surface variation. Calibration on clean data naturally accounts for residual clean-condition variance in the score distribution.\n\n**Step 3: TV-Bounded Calibration.** Under k-poisoning with K groups, corruption bound m determines maximal TV distance: TV ≤ m/K. Using CRC (ICLR 2024) with TV-inflated quantile: set abstention threshold at the (1 − α + TV)-quantile of calibration scores, yielding formal certificate P(correct or abstain) ≥ 1 − α under k-poisoning.\n\n**Calibration protocol:** Calibration set constructed on clean corpus (standard assumption per RPS, ICLR 2025), n_cal ≥ 500 per dataset. Sensitivity experiment evaluates coverage degradation when actual poisoning budget exceeds assumed k.\n\n**Step 4: Abstention Decision.** At test time, if s > λ (calibrated threshold), abstain; otherwise, output the majority answer across groups.\n\n## Experimental Design\n\n**Datasets:** Primary: NQ, HotpotQA, MS-MARCO (standard RAG benchmarks, used by PoisonedRAG/RobustRAG). Secondary: PubMedQA (domain-specific, core metrics only, validating high-stakes scenario motivation).\n\n**Attack methods:**\n- PoisonedRAG (targeted, k ∈ {1, 3, 5, 10})\n- CorruptRAG (single-document high-ASR)\n- One DoS-type attack from RSB Benchmark (May 2025) taxonomy\n- **Agreement-aware adaptive attack**: attacker knows K-partition structure and optimizes poisoned passage content to maximize cross-group NLI entailment (minimize s) while ensuring target wrong answer\n\n**Models:** Three scales for model-agnosticism: (1) primary: Qwen3.5-7B (or Llama-3-8B); (2) medium: Qwen3.5-32B; (3) large: Qwen3.5-72B. NLI model: DeBERTa-v3-large.\n\n**Baselines (8 methods):**\n- Conformal: TRAQ (NAACL 2024), C-RAG (ICML 2024), Conformal-RAG (SIGIR 2025)\n- Certified defense: RobustRAG (SaTML 2026), ReliabilityRAG (NeurIPS 2025)\n- Partition-based: RAGPart (arXiv:2512.24268)—same partition, no conformal (ablation baseline)\n- Compute-normalized: TRAQ + K× self-consistency voting\n- Naive pipeline: RobustRAG + TRAQ (empirically validates the \"Why not combine?\" theoretical argument)\n\n**Metrics:**\n- Primary: Certified coverage rate, empirical coverage under attack, abstention rate\n- Secondary: Clean accuracy (no attack), prediction set size, vacuousness rate (per Chen et al. 2026)\n- Tradeoff: Coverage vs. abstention at varying α; coverage vs. poisoning budget k; certified vs. empirical gap\n- Efficiency: Wall-clock time per query, token consumption\n\n**Ablation matrix** (full ablation on 7B only; 32B/72B do core config only):\n- K ∈ {1, 3, 5, 7, 10}: K=1 is the degenerate no-partition baseline proving partition necessity\n- n ∈ {10, 20, 30}: retrieval depth vs. certificate tightness\n- Score function: NLI entailment (primary) vs. ROUGE-L vs. exact match\n- Calibration: CRC + TV inflation (full method) vs. CRC without inflation (isolates TV contribution) vs. vanilla split conformal (isolates CRC contribution)\n- Partition strategy: random vs. round-robin by retrieval score\n\n**Diagnostic experiments:**\n- **NLI reliability**: Collect clean-group and corrupted-group LLM outputs under attack; evaluate DeBERTa NLI entailment accuracy and calibration (reliability diagram) on these output pairs. If unreliable, evaluate ensemble NLI or temperature-scaled NLI as robustness enhancement. Motivated by The Semantic Illusion (arXiv:2512.15068) findings on NLI limitations.\n- **TV bound tightness**: Empirically estimate actual TV distance between clean and poisoned score CDFs (bootstrap/KDE) vs. theoretical m/K bound. Report tightness ratio across attack settings.\n- **k sensitivity**: Evaluate coverage degradation when actual poisoning exceeds assumed k upper bound.\n\n**Scale:** 200-300 queries per dataset per setting (primary datasets); 200 queries for PubMedQA. 95% confidence intervals reported. Full ablation on 7B; 32B/72B validate core configuration only.\n\n**Discussion items:** (1) Partition-induced reduction as a potential general principle for lifting point-estimate certified defenses to distributional guarantees (future work). (2) k-poisoning assumption validity across different attack types. (3) Gradient-based adaptive attacks (Semantic Chameleon) as future robustness evaluation.\n\n## Key References\n\n- TRAQ: Trustworthy Retrieval Augmented QA via Conformal Prediction (NAACL 2024)\n- C-RAG: Certified Generation Risks for RAG (ICML 2024)\n- Conformal Risk Control (ICLR 2024)\n- Provably Reliable Conformal Prediction Sets under Poisoning (ICLR 2025 Spotlight)\n- Certifiably Robust RAG against Retrieval Corruption (SaTML 2026)\n- ReliabilityRAG (NeurIPS 2025)\n- Is Conformal Factuality for RAG-based LLMs Robust? (arXiv:2603.16817, Mar 2026)\n- Conformal-RAG: Conditional Conformal Factuality (SIGIR 2025)\n- CorruptRAG: Practical Poisoning Attacks against RAG (arXiv 2025)\n- PoisonedRAG (USENIX Security 2025)\n- RSB Benchmark: Benchmarking Poisoning Attacks against RAG (May 2025)\n- RAGPart & RAGMask (arXiv:2512.24268, Dec 2025)\n- Conformal Prediction under Lévy-Prokhorov Distribution Shifts (arXiv:2502.14105)\n- Semantic Chameleon (arXiv Mar 2026)\n- Mitigating LLM Hallucinations via Conformal Abstention (arXiv:2405.01563)\n- The Consensus Trap (arXiv:2604.17139, Apr 2026)\n- The Semantic Illusion (arXiv:2512.15068)"
}
```

---

### Runtime record

_source line 2 · 2026-05-30T07:47:47.371Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T07:47:47.371Z",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867"
}
```

---

## Round 1

43 recorded events

### User

_source line 3 · 2026-05-30T07:47:47.394Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores

## Core Problem

RAG systems in adversarial environments (medical QA, legal retrieval, financial compliance) need distribution-free abstention guarantees when the retrieval corpus is poisoned. Corpus poisoning is a practical threat: CorruptRAG (arXiv 2025) achieves high attack success with a single injected document; PoisonedRAG (USENIX Security 2025) reaches 90%+ ASR with 5 documents. Existing conformal prediction methods for RAG (TRAQ, NAACL 2024; C-RAG, ICML 2024; Conformal-RAG, SIGIR 2025) assume benign retrieval—Chen et al. (arXiv:2603.16817, Mar 2026) demonstrated these guarantees break under distribution shift, producing vacuous outputs. Poisoning-robust CP (RPS, ICLR 2025 Spotlight) addresses calibration-set poisoning, not test-time retrieval corruption. Certified RAG defenses (RobustRAG, SaTML 2026; ReliabilityRAG, NeurIPS 2025) provide robust point estimates but no abstention mechanism or coverage certificates. The gap: no method provides distribution-free abstention guarantees for RAG under adversarial retrieval corruption.

## Core Contribution and Theoretical Insight

PRCA's central contribution is a **partition-induced reduction**: partitioning retrieved passages into disjoint groups and computing inter-group agreement deterministically reduces arbitrary test-time retrieval corruption to a bounded TV shift in the one-dimensional nonconformity score distribution. This bounded shift is absorbed by CRC (ICLR 2024) via inflated quantiles, yielding formal coverage certificates. This reduction—from high-dimensional adversarial corruption to one-dimensional bounded distributional shift—parallels the approach of Conformal Prediction under Lévy-Prokhorov Distribution Shifts (arXiv:2502.14105), which reduces high-dimensional shifts to one-dimensional score shifts via ambiguity sets.

**Why not simply combine existing methods?** Three natural alternatives fail:

(1) **RobustRAG + standard CP**: Running RobustRAG's isolate-then-aggregate to obtain a robust answer, then applying TRAQ/C-RAG for conformal abstention, fails because RobustRAG's aggregation transforms the output distribution in a poisoning-dependent manner. Nonconformity scores from clean calibration are no longer exchangeable with test-time scores under attack, and the magnitude of distributional shift is uncharacterized. PRCA explicitly bounds this shift via partition structure.

(2) **Full-context self-consistency + CP**: Generating K answers from the same full retrieval set and using agreement as a conformal score (the approach of Conformal Abstention, arXiv:2405.01563) fails under poisoning because all K samples share the same poisoned context. The model may produce consistently wrong answers with high agreement, making the score blind to corruption. Partition isolates poisoned passages into a bounded number of groups, enabling detection.

(3) **Logprob-based confidence + CP**: Using LLM token-level logprobabilities as nonconformity scores fails because adversarially crafted passages (e.g., via Semantic Chameleon's gradient-guided attacks, arXiv Mar 2026) are designed to appear authoritative, inflating model confidence on wrong answers. Logprob monotonicity with respect to correctness breaks under adversarial retrieval.

**Partition is a theoretical necessity, not a design choice**: it is the structural mechanism that transforms uncharacterizable adversarial corruption into a bounded, quantifiable distributional shift that CRC can absorb.

## Research Landscape

**Conformal prediction for RAG:** TRAQ (NAACL 2024) and C-RAG (ICML 2024) established conformal prediction for RAG under benign retrieval. Conformal-RAG (SIGIR 2025) extends to group-conditional coverage. Chen et al. (arXiv:2603.16817, Mar 2026) showed all such methods produce vacuous prediction sets under distribution shift and retrieval corruption, but proposed no solution.

**Certified RAG defenses:** RobustRAG (SaTML 2026) provides certified defense via isolate-then-aggregate, achieving certified robust accuracy on RealtimeQA/NQ. ReliabilityRAG (NeurIPS 2025) uses graph-theoretic MIS with NLI-based contradiction detection for provably robust document filtering. Both provide robust point estimates but no coverage certificates or abstention mechanism.

**Poisoning-robust CP:** RPS (ICLR 2025 Spotlight) achieves poisoning-robust CP via smoothed scores and majority voting but assumes calibration-set poisoning—certificates do not transfer to test-time retrieval corruption.

**Partition-based defenses:** RAGPart (arXiv:2512.24268, Dec 2025) uses document partitioning at the retrieval stage (fragment embeddings) to dilute poisoning. Three key differences from PRCA: (1) RAGPart operates at retrieval/embedding stage, PRCA at generation/calibration stage; (2) RAGPart outputs filtered retrieval sets, PRCA outputs {answer, abstain} decisions with coverage certificates; (3) they are complementary—RAGPart can preprocess retrieval before PRCA's certified abstention.

**Adversarial aggregation:** The Consensus Trap (arXiv:2604.17139, Apr 2026) proves response-level majority voting fails when corrupted agents form a local majority. PRCA's majority answer output could face this risk, but: (a) PRCA's primary guarantee is the coverage certificate on the abstention decision, not the majority answer's correctness; (b) under the standard threat model k < n/2, the number of corrupted groups m = ceil(k/floor(n/K)) < K/2, so the honest majority is preserved.

**Attack landscape:** PoisonedRAG (USENIX Security 2025), CorruptRAG (arXiv 2025), RSB Benchmark (May 2025, 13 attack methods × 7 defenses), Semantic Chameleon (arXiv Mar 2026, gradient-guided corpus-dependent attacks).

**Distribution-shift-robust CP:** LP-shift framework (arXiv:2502.14105) reduces high-dimensional shifts to one-dimensional score shifts. PRCA's partition-induced TV bound is a specific instantiation for adversarial retrieval corruption.

No existing work combines conformal abstention with retrieval-poisoning robustness.

## Proposed Approach

**Step 1: Partition-and-Generate.** Partition top-n retrieved passages into K disjoint groups (random assignment). Generate a per-group answer via isolated LLM calls.

**Step 2: Agreement Nonconformity Score.** For each group pair (i, j), compute NLI entailment probability e(i,j) = P(answer_i entails answer_j) using DeBERTa-v3-large (following ReliabilityRAG's NLI approach). Define:

s = 1 − mean({e(i,j)} over all pairs)

Critical properties: (1) **Monotonicity**: s increases with disagreement; higher s → more likely to abstain, satisfying CRC's monotone-loss requirement. (2) **Corruption-boundedness**: under k-poisoning, at most m = ceil(k/floor(n/K)) groups are corrupted, affecting at most m(K−1) of C(K,2) pairwise comparisons, yielding bounded perturbation to s.

**Toward tighter bounds:** The worst-case TV ≤ m/K is a combinatorial upper bound. Because s is a mean of bounded pairwise scores, the actual perturbation from m corrupted groups may be dampened. We will empirically estimate the actual TV distance between clean and poisoned score CDFs (via bootstrap) and compare against the theoretical bound, reporting the tightness ratio. Exploring concentration-based bounds (leveraging the mean structure) is a concrete research direction.

**Clean-condition variance mitigation:** If different passage groups cover different answer facets, clean-condition agreement variance inflates s and may cause excessive abstention. NLI-based semantic entailment (rather than exact match) is robust to surface variation. Calibration on clean data naturally accounts for residual clean-condition variance in the score distribution.

**Step 3: TV-Bounded Calibration.** Under k-poisoning with K groups, corruption bound m determines maximal TV distance: TV ≤ m/K. Using CRC (ICLR 2024) with TV-inflated quantile: set abstention threshold at the (1 − α + TV)-quantile of calibration scores, yielding formal certificate P(correct or abstain) ≥ 1 − α under k-poisoning.

**Calibration protocol:** Calibration set constructed on clean corpus (standard assumption per RPS, ICLR 2025), n_cal ≥ 500 per dataset. Sensitivity experiment evaluates coverage degradation when actual poisoning budget exceeds assumed k.

**Step 4: Abstention Decision.** At test time, if s > λ (calibrated threshold), abstain; otherwise, output the majority answer across groups.

## Experimental Design

**Datasets:** Primary: NQ, HotpotQA, MS-MARCO (standard RAG benchmarks, used by PoisonedRAG/RobustRAG). Secondary: PubMedQA (domain-specific, core metrics only, validating high-stakes scenario motivation).

**Attack methods:**
- PoisonedRAG (targeted, k ∈ {1, 3, 5, 10})
- CorruptRAG (single-document high-ASR)
- One DoS-type attack from RSB Benchmark (May 2025) taxonomy
- **Agreement-aware adaptive attack**: attacker knows K-partition structure and optimizes poisoned passage content to maximize cross-group NLI entailment (minimize s) while ensuring target wrong answer

**Models:** Three scales for model-agnosticism: (1) primary: Qwen3.5-7B (or Llama-3-8B); (2) medium: Qwen3.5-32B; (3) large: Qwen3.5-72B. NLI model: DeBERTa-v3-large.

**Baselines (8 methods):**
- Conformal: TRAQ (NAACL 2024), C-RAG (ICML 2024), Conformal-RAG (SIGIR 2025)
- Certified defense: RobustRAG (SaTML 2026), ReliabilityRAG (NeurIPS 2025)
- Partition-based: RAGPart (arXiv:2512.24268)—same partition, no conformal (ablation baseline)
- Compute-normalized: TRAQ + K× self-consistency voting
- Naive pipeline: RobustRAG + TRAQ (empirically validates the "Why not combine?" theoretical argument)

**Metrics:**
- Primary: Certified coverage rate, empirical coverage under attack, abstention rate
- Secondary: Clean accuracy (no attack), prediction set size, vacuousness rate (per Chen et al. 2026)
- Tradeoff: Coverage vs. abstention at varying α; coverage vs. poisoning budget k; certified vs. empirical gap
- Efficiency: Wall-clock time per query, token consumption

**Ablation matrix** (full ablation on 7B only; 32B/72B do core config only):
- K ∈ {1, 3, 5, 7, 10}: K=1 is the degenerate no-partition baseline proving partition necessity
- n ∈ {10, 20, 30}: retrieval depth vs. certificate tightness
- Score function: NLI entailment (primary) vs. ROUGE-L vs. exact match
- Calibration: CRC + TV inflation (full method) vs. CRC without inflation (isolates TV contribution) vs. vanilla split conformal (isolates CRC contribution)
- Partition strategy: random vs. round-robin by retrieval score

**Diagnostic experiments:**
- **NLI reliability**: Collect clean-group and corrupted-group LLM outputs under attack; evaluate DeBERTa NLI entailment accuracy and calibration (reliability diagram) on these output pairs. If unreliable, evaluate ensemble NLI or temperature-scaled NLI as robustness enhancement. Motivated by The Semantic Illusion (arXiv:2512.15068) findings on NLI limitations.
- **TV bound tightness**: Empirically estimate actual TV distance between clean and poisoned score CDFs (bootstrap/KDE) vs. theoretical m/K bound. Report tightness ratio across attack settings.
- **k sensitivity**: Evaluate coverage degradation when actual poisoning exceeds assumed k upper bound.

**Scale:** 200-300 queries per dataset per setting (primary datasets); 200 queries for PubMedQA. 95% confidence intervals reported. Full ablation on 7B; 32B/72B validate core configuration only.

**Discussion items:** (1) Partition-induced reduction as a potential general principle for lifting point-estimate certified defenses to distributional guarantees (future work). (2) k-poisoning assumption validity across different attack types. (3) Gradient-based adaptive attacks (Semantic Chameleon) as future robustness evaluation.

## Key References

- TRAQ: Trustworthy Retrieval Augmented QA via Conformal Prediction (NAACL 2024)
- C-RAG: Certified Generation Risks for RAG (ICML 2024)
- Conformal Risk Control (ICLR 2024)
- Provably Reliable Conformal Prediction Sets under Poisoning (ICLR 2025 Spotlight)
- Certifiably Robust RAG against Retrieval Corruption (SaTML 2026)
- ReliabilityRAG (NeurIPS 2025)
- Is Conformal Factuality for RAG-based LLMs Robust? (arXiv:2603.16817, Mar 2026)
- Conformal-RAG: Conditional Conformal Factuality (SIGIR 2025)
- CorruptRAG: Practical Poisoning Attacks against RAG (arXiv 2025)
- PoisonedRAG (USENIX Security 2025)
- RSB Benchmark: Benchmarking Poisoning Attacks against RAG (May 2025)
- RAGPart & RAGMask (arXiv:2512.24268, Dec 2025)
- Conformal Prediction under Lévy-Prokhorov Distribution Shifts (arXiv:2502.14105)
- Semantic Chameleon (arXiv Mar 2026)
- Mitigating LLM Hallucinations via Conformal Abstention (arXiv:2405.01563)
- The Consensus Trap (arXiv:2604.17139, Apr 2026)
- The Semantic Illusion (arXiv:2512.15068)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "815a8749-b513-453f-8657-19f64f89c02b",
  "type": "user",
  "uuid": "8f7ddabb-30cd-4ff8-946a-f124a4ff00d4",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T07:47:47.392Z_

```json
{
  "parentUuid": "8f7ddabb-30cd-4ff8-946a-f124a4ff00d4",
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
  "uuid": "760c0a06-b5e0-46a7-bc2d-9733fb332e10",
  "timestamp": "2026-05-30T07:47:47.392Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T07:47:47.392Z_

```json
{
  "parentUuid": "760c0a06-b5e0-46a7-bc2d-9733fb332e10",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "96530cb8-f6b9-4e86-81dd-cf8b0a8d42b9",
  "timestamp": "2026-05-30T07:47:47.392Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
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
  "aiTitle": "Evaluate poisoning-robust conformal RAG abstention",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867"
}
```

---

### Assistant

_source line 7 · 2026-05-30T07:47:55.296Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for AAAI 2026. The proposal is about "Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores" (PRCA). 

Before I can give a proper evaluation, I need to do thorough research on the field. Let me start by searching for the key related works and understanding the current landscape.

Let me search for:
1. Recent work on conformal prediction for RAG systems
2. Corpus poisoning attacks on RAG
3. Robust conformal prediction methods
4. The specific papers mentioned in the proposal to verify claims


I'll run several searches simultaneously to gather information on conformal prediction methods for RAG systems, poisoning attacks in retrieval-augmented generation, and robust prediction techniques.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96530cb8-f6b9-4e86-81dd-cf8b0a8d42b9",
  "isSidechain": false,
  "requestId": "req_011CbYPFaXRp55TrDf3QsvsB",
  "type": "assistant",
  "uuid": "d4a629e5-363e-4502-8a84-4ce96bd0575c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bxwPDxtjRt1rUojDdevpG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7566,
      "cache_read_input_tokens": 11014,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7566,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 271,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 7566,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7566
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

_source line 8 · 2026-05-30T07:47:55.379Z_

I'll start by conducting thorough research on the field before making any evaluation. Let me search for the key related works and current landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4a629e5-363e-4502-8a84-4ce96bd0575c",
  "isSidechain": false,
  "requestId": "req_011CbYPFaXRp55TrDf3QsvsB",
  "type": "assistant",
  "uuid": "bc1f6d14-21e1-49b2-9f03-e56387e16349",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bxwPDxtjRt1rUojDdevpG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7566,
      "cache_read_input_tokens": 11014,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7566,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 271,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 7566,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7566
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

_source line 9 · 2026-05-30T07:47:55.550Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MG8fUupShUe6iySecJK3Hw`</summary>

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
  "parentUuid": "bc1f6d14-21e1-49b2-9f03-e56387e16349",
  "isSidechain": false,
  "requestId": "req_011CbYPFaXRp55TrDf3QsvsB",
  "type": "assistant",
  "uuid": "86cbeed6-1ec7-4ee4-b121-8c4c4efcffdb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015bxwPDxtjRt1rUojDdevpG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7566,
      "cache_read_input_tokens": 11014,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7566,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 271,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 7566,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7566
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

_source line 10 · 2026-05-30T07:47:55.557Z_

<details><summary>↩ Tool result · `toolu_01MG8fUupShUe6iySecJK3Hw`</summary>

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
  "parentUuid": "86cbeed6-1ec7-4ee4-b121-8c4c4efcffdb",
  "isSidechain": false,
  "promptId": "815a8749-b513-453f-8657-19f64f89c02b",
  "type": "user",
  "uuid": "28cba60e-c78e-4b6e-891f-6f11274fe20b",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "86cbeed6-1ec7-4ee4-b121-8c4c4efcffdb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores  ## Core Problem  RAG systems in ad…",
  "leafUuid": "28cba60e-c78e-4b6e-891f-6f11274fe20b",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate poisoning-robust conformal RAG abstention",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867"
}
```

---

### Assistant

_source line 13 · 2026-05-30T07:47:58.116Z_

Now let me conduct multiple parallel searches to understand the field landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28cba60e-c78e-4b6e-891f-6f11274fe20b",
  "isSidechain": false,
  "requestId": "req_011CbYPGAY52fTVyBCXkeQyv",
  "type": "assistant",
  "uuid": "38cf9cdc-4db3-4e95-a88f-13af3ec0441d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016GdvJBedR5yMzhfaHvESvk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 799,
      "cache_read_input_tokens": 18580,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 799,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 246,
          "cache_read_input_tokens": 18580,
          "cache_creation_input_tokens": 799,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 799
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

_source line 14 · 2026-05-30T07:47:58.654Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015TngjQYDVwFMEU55zNYrjM`</summary>

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
  "parentUuid": "38cf9cdc-4db3-4e95-a88f-13af3ec0441d",
  "isSidechain": false,
  "requestId": "req_011CbYPGAY52fTVyBCXkeQyv",
  "type": "assistant",
  "uuid": "1424de80-9d79-46a3-b0ab-2a1dab817274",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016GdvJBedR5yMzhfaHvESvk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 799,
      "cache_read_input_tokens": 18580,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 799,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 246,
          "cache_read_input_tokens": 18580,
          "cache_creation_input_tokens": 799,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 799
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

_source line 15 · 2026-05-30T07:47:59.613Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KGmujiPYrzqLh1KqPnebgm`</summary>

```json
{
  "query": "corpus poisoning attack RAG PoisonedRAG CorruptRAG 2025 defense"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1424de80-9d79-46a3-b0ab-2a1dab817274",
  "isSidechain": false,
  "requestId": "req_011CbYPGAY52fTVyBCXkeQyv",
  "type": "assistant",
  "uuid": "a8786e2d-47ca-4cc8-ba7d-435b001957b8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016GdvJBedR5yMzhfaHvESvk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 799,
      "cache_read_input_tokens": 18580,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 799,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 246,
          "cache_read_input_tokens": 18580,
          "cache_creation_input_tokens": 799,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 799
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

_source line 16 · 2026-05-30T07:48:00.065Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015C1xT2voMxTV3faCFEKRWC`</summary>

```json
{
  "query": "RobustRAG certified defense retrieval corruption SaTML 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8786e2d-47ca-4cc8-ba7d-435b001957b8",
  "isSidechain": false,
  "requestId": "req_011CbYPGAY52fTVyBCXkeQyv",
  "type": "assistant",
  "uuid": "9846d4fa-9f26-432a-a4fa-a5e981ee24e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016GdvJBedR5yMzhfaHvESvk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 799,
      "cache_read_input_tokens": 18580,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 799,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 246,
          "cache_read_input_tokens": 18580,
          "cache_creation_input_tokens": 799,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 799
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

_source line 17 · 2026-05-30T07:48:00.742Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ck8KN9yQVyVgwFkFCTmyQi`</summary>

```json
{
  "query": "poisoning robust conformal prediction RPS ICLR 2025 spotlight"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9846d4fa-9f26-432a-a4fa-a5e981ee24e7",
  "isSidechain": false,
  "requestId": "req_011CbYPGAY52fTVyBCXkeQyv",
  "type": "assistant",
  "uuid": "5f51bb9d-610e-43cc-bcba-2e4e72527c71",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016GdvJBedR5yMzhfaHvESvk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 799,
      "cache_read_input_tokens": 18580,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 799,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 246,
          "cache_read_input_tokens": 18580,
          "cache_creation_input_tokens": 799,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 799
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

_source line 18 · 2026-05-30T07:48:06.335Z_

<details><summary>↩ Tool result · `toolu_015TngjQYDVwFMEU55zNYrjM`</summary>

```text
Web search results for query: "conformal prediction RAG retrieval augmented generation TRAQ C-RAG 2024 2025"

Links: [{"title":"GitHub - Arstanley/Awesome-Trustworthy-RAG · GitHub","url":"https://github.com/Arstanley/Awesome-Trustworthy-RAG"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal   Prediction","url":"https://arxiv.org/pdf/2307.04642"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.210/"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction","url":"https://arxiv.org/html/2307.04642v2"},{"title":"Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-21300-6_45"},{"title":"Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/html/2506.20978"}]

Based on the search results, I found relevant information about your query:

## Key Findings:

**TRAQ (Trustworthy Retrieval Augmented Question Answering)**

TRAQ provides the first end-to-end statistical correctness guarantee for RAG. TRAQ uses conformal prediction, a statistical technique for constructing prediction sets that are guaranteed to contain the semantically correct response with high probability. This work was published at NAACL 2024 (June 2024).

**C-RAG (Certified Generation Risks for Retrieval-Augmented Language Models)**

C-RAG was accepted to ICML and focuses on certified generation risks for retrieval-augmented language models, published in 2024.02.

**Related Work in Conformal Prediction for RAG**

The search results also reveal other related recent work:
- CONFLARE: CONFormal LArge language model REtrieval (2024.04)
- Response quality assessment for retrieval-augmented generation via conditional conformal factuality (2025)

These papers represent an emerging research direction combining conformal prediction with RAG systems to provide statistical guarantees about correctness and trustworthiness in retrieval-augmented language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1424de80-9d79-46a3-b0ab-2a1dab817274",
  "isSidechain": false,
  "promptId": "815a8749-b513-453f-8657-19f64f89c02b",
  "type": "user",
  "uuid": "c6f482a8-4def-4487-9916-32ace7cf40b2",
  "toolUseResult": {
    "query": "conformal prediction RAG retrieval augmented generation TRAQ C-RAG 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QKfPUU9vAmJt2JvpqfqeTK",
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
      "Based on the search results, I found relevant information about your query:\n\n## Key Findings:\n\n**TRAQ (Trustworthy Retrieval Augmented Question Answering)**\n\nTRAQ provides the first end-to-end statistical correctness guarantee for RAG. TRAQ uses conformal prediction, a statistical technique for constructing prediction sets that are guaranteed to contain the semantically correct response with high probability. This work was published at NAACL 2024 (June 2024).\n\n**C-RAG (Certified Generation Risks for Retrieval-Augmented Language Models)**\n\nC-RAG was accepted to ICML and focuses on certified generation risks for retrieval-augmented language models, published in 2024.02.\n\n**Related Work in Conformal Prediction for RAG**\n\nThe search results also reveal other related recent work:\n- CONFLARE: CONFormal LArge language model REtrieval (2024.04)\n- Response quality assessment for retrieval-augmented generation via conditional conformal factuality (2025)\n\nThese papers represent an emerging research direction combining conformal prediction with RAG systems to provide statistical guarantees about correctness and trustworthiness in retrieval-augmented language models."
    ],
    "durationSeconds": 7.6758049370000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1424de80-9d79-46a3-b0ab-2a1dab817274",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-30T07:48:07.235Z_

<details><summary>↩ Tool result · `toolu_01KGmujiPYrzqLh1KqPnebgm`</summary>

```text
Web search results for query: "corpus poisoning attack RAG PoisonedRAG CorruptRAG 2025 defense"

Links: [{"title":"RAG Poisoning: Contaminating the AI’s “Source of Truth” | by InstaTunnel | Medium","url":"https://medium.com/@instatunnel/rag-poisoning-contaminating-the-ais-source-of-truth-082dcbdeea7c"},{"title":"RAG Poisoning: How Attackers Corrupt Your AI's Knowledge Base | Amine Raji, PhD","url":"https://aminrj.com/posts/rag-document-poisoning/"},{"title":"RAG Poisoning: Threats and Defenses","url":"https://www.emergentmind.com/topics/retrieval-augmented-generation-rag-poisoning"},{"title":"Practical Poisoning Attacks against Retrieval-Augmented Generation","url":"https://arxiv.org/html/2504.03957v2"},{"title":"Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems","url":"https://arxiv.org/html/2603.18034v1"},{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"GitHub - sleeepeer/PoisonedRAG: [USENIX Security 2025] PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models · GitHub","url":"https://github.com/sleeepeer/PoisonedRAG"},{"title":"Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems","url":"https://arxiv.org/pdf/2603.18034"},{"title":"Addressing Corpus Knowledge Poisoning Attacks on RAG Using Sparse Attention","url":"https://arxiv.org/pdf/2602.04711"}]

Based on the search results, here's what I found about corpus poisoning attacks on RAG systems:

## Key Attacks

PoisonedRAG, accepted to USENIX Security 2025, represents the first knowledge database corruption attack specifically designed against RAG systems. For attacks to succeed, injected documents must satisfy two conditions: they must score higher cosine similarity to the target query than legitimate documents, and once retrieved, the poisoned content must cause the LLM to produce the attacker's desired answer.

CorruptRAG achieves high attack success with a single adversarial document per query. This represents a practical improvement over earlier approaches, as CorruptRAG constrains the attacker to injecting only one poisoned text per query, making attacks more stealthy and scalable.

## Attack Effectiveness

The attacks are remarkably effective: injecting just five malicious texts into a knowledge database containing millions of documents can achieve a 90% attack success rate. Poisoning merely 0.04% of a corpus can lead to a 98.2% attack success rate and 74.6% system failure.

## Defense Mechanisms

Several defense strategies have been proposed:

- Knowledge expansion was introduced as a defense against PoisonedRAG, where the defender retrieves a larger set of top relevant texts to enhance the chances of retrieving benign documents.

- RAGPart leverages document partitioning to mitigate poisoned points, while RAGMask identifies suspicious tokens based on significant similarity shifts under targeted token masking.

- Sparse Document Attention RAG (SDAG) enforces block-sparse-attention over retrieved documents, where tokens in a retrieved document attend only to previous tokens in the same document.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8786e2d-47ca-4cc8-ba7d-435b001957b8",
  "isSidechain": false,
  "promptId": "815a8749-b513-453f-8657-19f64f89c02b",
  "type": "user",
  "uuid": "8c0d2d78-05db-4f96-8470-04e17347db42",
  "toolUseResult": {
    "query": "corpus poisoning attack RAG PoisonedRAG CorruptRAG 2025 defense",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GVW1GjVrR68YoXBtku5wJU",
        "content": [
          {
            "title": "RAG Poisoning: Contaminating the AI’s “Source of Truth” | by InstaTunnel | Medium",
            "url": "https://medium.com/@instatunnel/rag-poisoning-contaminating-the-ais-source-of-truth-082dcbdeea7c"
          },
          {
            "title": "RAG Poisoning: How Attackers Corrupt Your AI's Knowledge Base | Amine Raji, PhD",
            "url": "https://aminrj.com/posts/rag-document-poisoning/"
          },
          {
            "title": "RAG Poisoning: Threats and Defenses",
            "url": "https://www.emergentmind.com/topics/retrieval-augmented-generation-rag-poisoning"
          },
          {
            "title": "Practical Poisoning Attacks against Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2504.03957v2"
          },
          {
            "title": "Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems",
            "url": "https://arxiv.org/html/2603.18034v1"
          },
          {
            "title": "RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2512.24268"
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
            "title": "Addressing Corpus Knowledge Poisoning Attacks on RAG Using Sparse Attention",
            "url": "https://arxiv.org/pdf/2602.04711"
          }
        ]
      },
      "Based on the search results, here's what I found about corpus poisoning attacks on RAG systems:\n\n## Key Attacks\n\nPoisonedRAG, accepted to USENIX Security 2025, represents the first knowledge database corruption attack specifically designed against RAG systems. For attacks to succeed, injected documents must satisfy two conditions: they must score higher cosine similarity to the target query than legitimate documents, and once retrieved, the poisoned content must cause the LLM to produce the attacker's desired answer.\n\nCorruptRAG achieves high attack success with a single adversarial document per query. This represents a practical improvement over earlier approaches, as CorruptRAG constrains the attacker to injecting only one poisoned text per query, making attacks more stealthy and scalable.\n\n## Attack Effectiveness\n\nThe attacks are remarkably effective: injecting just five malicious texts into a knowledge database containing millions of documents can achieve a 90% attack success rate. Poisoning merely 0.04% of a corpus can lead to a 98.2% attack success rate and 74.6% system failure.\n\n## Defense Mechanisms\n\nSeveral defense strategies have been proposed:\n\n- Knowledge expansion was introduced as a defense against PoisonedRAG, where the defender retrieves a larger set of top relevant texts to enhance the chances of retrieving benign documents.\n\n- RAGPart leverages document partitioning to mitigate poisoned points, while RAGMask identifies suspicious tokens based on significant similarity shifts under targeted token masking.\n\n- Sparse Document Attention RAG (SDAG) enforces block-sparse-attention over retrieved documents, where tokens in a retrieved document attend only to previous tokens in the same document."
    ],
    "durationSeconds": 7.618421992,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a8786e2d-47ca-4cc8-ba7d-435b001957b8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-30T07:48:07.361Z_

<details><summary>↩ Tool result · `toolu_01Ck8KN9yQVyVgwFkFCTmyQi`</summary>

```text
Web search results for query: "poisoning robust conformal prediction RPS ICLR 2025 spotlight"

Links: [{"title":"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning | OpenReview","url":"https://openreview.net/forum?id=ofuLWn8DFZ"},{"title":"Nine papers accepted at ICLR 2025, one at KAIS 2025 - Data Analytics and Machine Learning","url":"https://www.cs.cit.tum.de/en/daml/all-news/article/nine-papers-accepted-at-iclr-2025/"},{"title":"GitHub - yascho/reliable_conformal_prediction: Implementation of the reliable conformal prediction sets introduced in the paper: \"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning\" accepted at ICLR 2025 (Spotlight).","url":"https://github.com/yascho/reliable_conformal_prediction"},{"title":"Published as a conference paper at ICLR 2025","url":"https://yascho.github.io/assets/pdf/scholten2025provably.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4d21a4b33361c40c2142db9511c126-Paper-Conference.pdf"},{"title":"Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning","url":"https://arxiv.org/pdf/2410.09878"},{"title":"ICLR Poster Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning","url":"https://iclr.cc/virtual/2025/poster/28340"},{"title":"Robust Yet Efficient Conformal Prediction Sets","url":"https://arxiv.org/pdf/2407.09165"}]

Based on the search results, I found information about the paper matching your query. Here's what I found:

## Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning

This paper was accepted as an ICLR 2025 Spotlight presentation, authored by Yan Scholten and Stephan Günnemann.

**Overview:**
Conformal prediction provides model-agnostic and distribution-free uncertainty quantification through prediction sets guaranteed to include the ground truth with any user-specified probability, yet it is not reliable under poisoning attacks where adversaries manipulate both training and calibration data.

**Proposed Solution:**
The paper proposes Reliable Prediction Sets (RPS): the first efficient method for constructing conformal prediction sets with provable reliability guarantees under poisoning. By introducing smoothed score functions and majority-voting prediction sets calibrated on distinct data subsets, RPS ensures reliability even under malicious poisoning manipulations.

**Key Contributions:**
The paper derives novel certificates that guarantee the reliability of RPS under worst-case data poisoning attacks, including guarantees against label flipping attacks.

The paper has been published and a reference implementation is available on GitHub with demo notebooks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f51bb9d-610e-43cc-bcba-2e4e72527c71",
  "isSidechain": false,
  "promptId": "815a8749-b513-453f-8657-19f64f89c02b",
  "type": "user",
  "uuid": "efc7b136-6937-4f3d-b1bd-d071dc54d9f0",
  "toolUseResult": {
    "query": "poisoning robust conformal prediction RPS ICLR 2025 spotlight",
    "results": [
      {
        "tool_use_id": "srvtoolu_019hxpwEUNB9VeJGNycMLBCA",
        "content": [
          {
            "title": "Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning | OpenReview",
            "url": "https://openreview.net/forum?id=ofuLWn8DFZ"
          },
          {
            "title": "Nine papers accepted at ICLR 2025, one at KAIS 2025 - Data Analytics and Machine Learning",
            "url": "https://www.cs.cit.tum.de/en/daml/all-news/article/nine-papers-accepted-at-iclr-2025/"
          },
          {
            "title": "GitHub - yascho/reliable_conformal_prediction: Implementation of the reliable conformal prediction sets introduced in the paper: \"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning\" accepted at ICLR 2025 (Spotlight).",
            "url": "https://github.com/yascho/reliable_conformal_prediction"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://yascho.github.io/assets/pdf/scholten2025provably.pdf"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4d21a4b33361c40c2142db9511c126-Paper-Conference.pdf"
          },
          {
            "title": "Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning",
            "url": "https://arxiv.org/pdf/2410.09878"
          },
          {
            "title": "ICLR Poster Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning",
            "url": "https://iclr.cc/virtual/2025/poster/28340"
          },
          {
            "title": "Robust Yet Efficient Conformal Prediction Sets",
            "url": "https://arxiv.org/pdf/2407.09165"
          }
        ]
      },
      "Based on the search results, I found information about the paper matching your query. Here's what I found:\n\n## Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning\n\nThis paper was accepted as an ICLR 2025 Spotlight presentation, authored by Yan Scholten and Stephan Günnemann.\n\n**Overview:**\nConformal prediction provides model-agnostic and distribution-free uncertainty quantification through prediction sets guaranteed to include the ground truth with any user-specified probability, yet it is not reliable under poisoning attacks where adversaries manipulate both training and calibration data.\n\n**Proposed Solution:**\nThe paper proposes Reliable Prediction Sets (RPS): the first efficient method for constructing conformal prediction sets with provable reliability guarantees under poisoning. By introducing smoothed score functions and majority-voting prediction sets calibrated on distinct data subsets, RPS ensures reliability even under malicious poisoning manipulations.\n\n**Key Contributions:**\nThe paper derives novel certificates that guarantee the reliability of RPS under worst-case data poisoning attacks, including guarantees against label flipping attacks.\n\nThe paper has been published and a reference implementation is available on GitHub with demo notebooks."
    ],
    "durationSeconds": 6.6168967190000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5f51bb9d-610e-43cc-bcba-2e4e72527c71",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-30T07:48:07.468Z_

<details><summary>↩ Tool result · `toolu_015C1xT2voMxTV3faCFEKRWC`</summary>

```text
Web search results for query: "RobustRAG certified defense retrieval corruption SaTML 2026"

Links: [{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://goatstack.ai/topics/certifiably-robust-rag-against-retrieval-corruption-yclugx"},{"title":"IEEE SaTML 2026 · Program","url":"https://satml.org/program/"},{"title":"IEEE SaTML 2026 · Accepted Papers","url":"https://satml.org/accepted-papers/"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/pdf/2405.15556"},{"title":"Certifiably Robust RAG against Retrieval Corruption | Request PDF","url":"https://www.researchgate.net/publication/380895542_Certifiably_Robust_RAG_against_Retrieval_Corruption"},{"title":"[Literature Review] Certifiably Robust RAG against Retrieval Corruption","url":"https://www.themoonlight.io/en/review/certifiably-robust-rag-against-retrieval-corruption"},{"title":"Certifiably Robust RAG against Retrieval Corruption Attacks | OpenReview","url":"https://openreview.net/forum?id=cU6ZdN87p3"},{"title":"[2405.15556] Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/abs/2405.15556"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://openreview.net/pdf?id=qsEeACAJjD"}]

Based on the search results, here's what I found about RobustRAG at SaTML 2026:

RobustRAG is the first defense framework with certifiable robustness against retrieval corruption attacks. Retrieval-augmented generation (RAG) is susceptible to retrieval corruption attacks, where malicious passages injected into retrieval results can lead to inaccurate model responses.

The key insight of RobustRAG is an isolate-then-aggregate strategy: we isolate passages into disjoint groups, generate LLM responses based on the concatenated passages from each isolated group, and then securely aggregate these responses for a robust output. To instantiate RobustRAG, we design keyword-based and decoding-based algorithms for securely aggregating unstructured text responses.

The authors of this work are Chong Xiang (NVIDIA), Tong Wu, Zexuan Zhong (Princeton University), David Wagner (University of California, Berkeley), Danqi Chen and Prateek Mittal (Princeton University).

The framework is effective in open-domain QA and text generation tasks, showcasing its resilience and generalizability in various scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9846d4fa-9f26-432a-a4fa-a5e981ee24e7",
  "isSidechain": false,
  "promptId": "815a8749-b513-453f-8657-19f64f89c02b",
  "type": "user",
  "uuid": "eae53a8f-e9c9-4f26-a9cf-9cf528b30e15",
  "toolUseResult": {
    "query": "RobustRAG certified defense retrieval corruption SaTML 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_017cNL13coCZAaLjv3fHBuox",
        "content": [
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://goatstack.ai/topics/certifiably-robust-rag-against-retrieval-corruption-yclugx"
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
            "title": "Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://arxiv.org/pdf/2405.15556"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption | Request PDF",
            "url": "https://www.researchgate.net/publication/380895542_Certifiably_Robust_RAG_against_Retrieval_Corruption"
          },
          {
            "title": "[Literature Review] Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://www.themoonlight.io/en/review/certifiably-robust-rag-against-retrieval-corruption"
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
            "title": "Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://openreview.net/pdf?id=qsEeACAJjD"
          }
        ]
      },
      "Based on the search results, here's what I found about RobustRAG at SaTML 2026:\n\nRobustRAG is the first defense framework with certifiable robustness against retrieval corruption attacks. Retrieval-augmented generation (RAG) is susceptible to retrieval corruption attacks, where malicious passages injected into retrieval results can lead to inaccurate model responses.\n\nThe key insight of RobustRAG is an isolate-then-aggregate strategy: we isolate passages into disjoint groups, generate LLM responses based on the concatenated passages from each isolated group, and then securely aggregate these responses for a robust output. To instantiate RobustRAG, we design keyword-based and decoding-based algorithms for securely aggregating unstructured text responses.\n\nThe authors of this work are Chong Xiang (NVIDIA), Tong Wu, Zexuan Zhong (Princeton University), David Wagner (University of California, Berkeley), Danqi Chen and Prateek Mittal (Princeton University).\n\nThe framework is effective in open-domain QA and text generation tasks, showcasing its resilience and generalizability in various scenarios."
    ],
    "durationSeconds": 7.400258978000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9846d4fa-9f26-432a-a4fa-a5e981ee24e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-30T07:48:09.877Z_

Good, now let me do additional targeted searches to verify specific claims and understand the competitive landscape better.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eae53a8f-e9c9-4f26-a9cf-9cf528b30e15",
  "isSidechain": false,
  "requestId": "req_011CbYPH3BagBQ9CMB5GsEnw",
  "type": "assistant",
  "uuid": "a59cde93-4ecf-44a9-ad88-efefc01a0423",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016wtMoL52zcQVeBZEC23ZSQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 791,
      "cache_creation_input_tokens": 2561,
      "cache_read_input_tokens": 19379,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2561,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 791,
          "output_tokens": 205,
          "cache_read_input_tokens": 19379,
          "cache_creation_input_tokens": 2561,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2561
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

_source line 23 · 2026-05-30T07:48:10.898Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U8RFM4yETTwBmGsnN5TFat`</summary>

```json
{
  "query": "conformal prediction distribution shift robust RAG vacuous prediction sets 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a59cde93-4ecf-44a9-ad88-efefc01a0423",
  "isSidechain": false,
  "requestId": "req_011CbYPH3BagBQ9CMB5GsEnw",
  "type": "assistant",
  "uuid": "7eeb1341-0b65-4d9b-8501-f8f430052b8e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016wtMoL52zcQVeBZEC23ZSQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 791,
      "cache_creation_input_tokens": 2561,
      "cache_read_input_tokens": 19379,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2561,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 791,
          "output_tokens": 205,
          "cache_read_input_tokens": 19379,
          "cache_creation_input_tokens": 2561,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2561
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

_source line 24 · 2026-05-30T07:48:11.819Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DxJTuFddYBmE4Vu1B7Z46X`</summary>

```json
{
  "query": "ReliabilityRAG graph-theoretic NLI robust document filtering NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7eeb1341-0b65-4d9b-8501-f8f430052b8e",
  "isSidechain": false,
  "requestId": "req_011CbYPH3BagBQ9CMB5GsEnw",
  "type": "assistant",
  "uuid": "0862d968-177e-4eab-a87f-3c6cfb35e476",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016wtMoL52zcQVeBZEC23ZSQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 791,
      "cache_creation_input_tokens": 2561,
      "cache_read_input_tokens": 19379,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2561,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 791,
          "output_tokens": 205,
          "cache_read_input_tokens": 19379,
          "cache_creation_input_tokens": 2561,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2561
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

_source line 25 · 2026-05-30T07:48:12.499Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013ojcvcupbuUdJhmpNxZa4P`</summary>

```json
{
  "query": "conformal risk control CRC ICLR 2024 Angelopoulos TV distance distribution shift"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0862d968-177e-4eab-a87f-3c6cfb35e476",
  "isSidechain": false,
  "requestId": "req_011CbYPH3BagBQ9CMB5GsEnw",
  "type": "assistant",
  "uuid": "e1220a47-4093-46f6-b8ec-0fa4165f1b34",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016wtMoL52zcQVeBZEC23ZSQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 791,
      "cache_creation_input_tokens": 2561,
      "cache_read_input_tokens": 19379,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2561,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 791,
          "output_tokens": 205,
          "cache_read_input_tokens": 19379,
          "cache_creation_input_tokens": 2561,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2561
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

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores  ## Core Problem  RAG systems in ad…",
  "leafUuid": "e1220a47-4093-46f6-b8ec-0fa4165f1b34",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate poisoning-robust conformal RAG abstention",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867"
}
```

---

### Tool result

_source line 28 · 2026-05-30T07:48:19.006Z_

<details><summary>↩ Tool result · `toolu_013ojcvcupbuUdJhmpNxZa4P`</summary>

```text
Web search results for query: "conformal risk control CRC ICLR 2024 Angelopoulos TV distance distribution shift"

Links: [{"title":"Anytime-Valid Conformal Risk Control","url":"https://arxiv.org/html/2602.04364v1"},{"title":"Published as a conference paper at ICLR 2024 CONFORMAL RISK CONTROL","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/f3549ef9b5ff520a7e41ff3cc306ab2b-Paper-Conference.pdf"},{"title":"[PDF] Conformal Risk Control | Semantic Scholar","url":"https://www.semanticscholar.org/paper/af2fba1911f0d0977c731e3918c51428e08741da"},{"title":"Published as a conference paper at ICLR 2024 CONFORMAL RISK CONTROL","url":"https://openreview.net/pdf?id=33XGfHLtZg"},{"title":"Conformal Policy Control","url":"https://arxiv.org/html/2603.02196v1"},{"title":"Conformal Risk Control","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/f3549ef9b5ff520a7e41ff3cc306ab2b-Abstract-Conference.html"},{"title":"[2208.02814] Conformal Risk Control","url":"https://arxiv.org/abs/2208.02814"}]

Based on the search results, I found relevant information about the paper you're looking for:

The paper "Conformal Risk Control" by Angelopoulos, A.N., Bates, S., Fisch, A., Lei, L., and Schuster, T. was published at the International Conference on Learning Representations (ICLR) in 2024.

The paper extends conformal prediction to control the expected value of any monotone loss function. The work introduces extensions of the idea to distribution shift, quantile risk control, multiple and adversarial risk control, and expectations of U-statistics.

Like conformal prediction, the conformal risk control procedure is tight up to an O(1/n) factor. Worked examples from computer vision and natural language processing demonstrate the usage of the algorithm to bound the false negative rate, graph distance, and token-level F1-score.

The paper addresses distribution shift scenarios and provides theoretical guarantees for risk control under these conditions. The full paper is available through the ICLR proceedings and on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1220a47-4093-46f6-b8ec-0fa4165f1b34",
  "isSidechain": false,
  "promptId": "815a8749-b513-453f-8657-19f64f89c02b",
  "type": "user",
  "uuid": "e34e3ac2-81f2-4b9e-a052-fd4933a1c518",
  "toolUseResult": {
    "query": "conformal risk control CRC ICLR 2024 Angelopoulos TV distance distribution shift",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AYAXaBJSNFz5jGyHosFkYw",
        "content": [
          {
            "title": "Anytime-Valid Conformal Risk Control",
            "url": "https://arxiv.org/html/2602.04364v1"
          },
          {
            "title": "Published as a conference paper at ICLR 2024 CONFORMAL RISK CONTROL",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2024/file/f3549ef9b5ff520a7e41ff3cc306ab2b-Paper-Conference.pdf"
          },
          {
            "title": "[PDF] Conformal Risk Control | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/af2fba1911f0d0977c731e3918c51428e08741da"
          },
          {
            "title": "Published as a conference paper at ICLR 2024 CONFORMAL RISK CONTROL",
            "url": "https://openreview.net/pdf?id=33XGfHLtZg"
          },
          {
            "title": "Conformal Policy Control",
            "url": "https://arxiv.org/html/2603.02196v1"
          },
          {
            "title": "Conformal Risk Control",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2024/hash/f3549ef9b5ff520a7e41ff3cc306ab2b-Abstract-Conference.html"
          },
          {
            "title": "[2208.02814] Conformal Risk Control",
            "url": "https://arxiv.org/abs/2208.02814"
          }
        ]
      },
      "Based on the search results, I found relevant information about the paper you're looking for:\n\nThe paper \"Conformal Risk Control\" by Angelopoulos, A.N., Bates, S., Fisch, A., Lei, L., and Schuster, T. was published at the International Conference on Learning Representations (ICLR) in 2024.\n\nThe paper extends conformal prediction to control the expected value of any monotone loss function. The work introduces extensions of the idea to distribution shift, quantile risk control, multiple and adversarial risk control, and expectations of U-statistics.\n\nLike conformal prediction, the conformal risk control procedure is tight up to an O(1/n) factor. Worked examples from computer vision and natural language processing demonstrate the usage of the algorithm to bound the false negative rate, graph distance, and token-level F1-score.\n\nThe paper addresses distribution shift scenarios and provides theoretical guarantees for risk control under these conditions. The full paper is available through the ICLR proceedings and on arXiv."
    ],
    "durationSeconds": 6.504040712999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e1220a47-4093-46f6-b8ec-0fa4165f1b34",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-30T07:48:20.779Z_

<details><summary>↩ Tool result · `toolu_01DxJTuFddYBmE4Vu1B7Z46X`</summary>

```text
Web search results for query: "ReliabilityRAG graph-theoretic NLI robust document filtering NeurIPS 2025"

Links: [{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://neurips.cc/media/neurips-2025/Slides/119236.pdf"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/pdf/2509.23519"},{"title":"NeurIPS Poster ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://neurips.cc/virtual/2025/poster/119236"},{"title":"[2509.23519] ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/abs/2509.23519"},{"title":"Tackling the Inherent Difficulty of Noise Filtering in RAG","url":"https://arxiv.org/pdf/2601.01896"},{"title":"ChunkRAG: Novel LLM-Chunk Filtering Method for RAG Systems","url":"https://arxiv.org/pdf/2410.19572"},{"title":"Document filtering via directed acyclic graphs","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5873081"},{"title":"Rethinking Graph-Based Document Classification: Learning Data-Driven Structures Beyond Heuristic Approaches","url":"https://arxiv.org/pdf/2508.00864"}]

I found relevant information about ReliabilityRAG. Here are the search results:

ReliabilityRAG is a novel framework designed to make RAG-based systems robust by finding a "consistent majority" over a set of retrieved documents using a graph-theoretic perspective.

**Key Technical Approach:**

The framework constructs a graph where each document is a vertex, drawing edges between contradictory documents (determined using an NLI model), and then finds a maximum independent set (MIS) in the graph.

**Features and Contributions:**

The approach incorporates reliability signals from the retriever—such as document rank or explicit reliability scores—to guide more robust generation. The MIS variant explicitly prioritizes higher-reliability documents and provides provable robustness guarantees against bounded adversarial corruption under natural assumptions.

A scalable weighted sample and aggregate framework was developed to handle the computational cost of exact MIS for large retrieval sets while preserving robustness guarantees.

**Performance:**

ReliabilityRAG provides superior robustness against adversarial attacks compared to prior methods, maintains high benign accuracy, and excels in long-form generation tasks.

For more details, you can access the paper at https://arxiv.org/abs/2509.23519.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0862d968-177e-4eab-a87f-3c6cfb35e476",
  "isSidechain": false,
  "promptId": "815a8749-b513-453f-8657-19f64f89c02b",
  "type": "user",
  "uuid": "e4d743ea-0ab5-49a3-8f40-a04201a3259c",
  "toolUseResult": {
    "query": "ReliabilityRAG graph-theoretic NLI robust document filtering NeurIPS 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Vkjt8TmTpUhTYuqyCAXaRW",
        "content": [
          {
            "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://neurips.cc/media/neurips-2025/Slides/119236.pdf"
          },
          {
            "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://arxiv.org/pdf/2509.23519"
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
            "title": "Tackling the Inherent Difficulty of Noise Filtering in RAG",
            "url": "https://arxiv.org/pdf/2601.01896"
          },
          {
            "title": "ChunkRAG: Novel LLM-Chunk Filtering Method for RAG Systems",
            "url": "https://arxiv.org/pdf/2410.19572"
          },
          {
            "title": "Document filtering via directed acyclic graphs",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5873081"
          },
          {
            "title": "Rethinking Graph-Based Document Classification: Learning Data-Driven Structures Beyond Heuristic Approaches",
            "url": "https://arxiv.org/pdf/2508.00864"
          }
        ]
      },
      "I found relevant information about ReliabilityRAG. Here are the search results:\n\nReliabilityRAG is a novel framework designed to make RAG-based systems robust by finding a \"consistent majority\" over a set of retrieved documents using a graph-theoretic perspective.\n\n**Key Technical Approach:**\n\nThe framework constructs a graph where each document is a vertex, drawing edges between contradictory documents (determined using an NLI model), and then finds a maximum independent set (MIS) in the graph.\n\n**Features and Contributions:**\n\nThe approach incorporates reliability signals from the retriever—such as document rank or explicit reliability scores—to guide more robust generation. The MIS variant explicitly prioritizes higher-reliability documents and provides provable robustness guarantees against bounded adversarial corruption under natural assumptions.\n\nA scalable weighted sample and aggregate framework was developed to handle the computational cost of exact MIS for large retrieval sets while preserving robustness guarantees.\n\n**Performance:**\n\nReliabilityRAG provides superior robustness against adversarial attacks compared to prior methods, maintains high benign accuracy, and excels in long-form generation tasks.\n\nFor more details, you can access the paper at https://arxiv.org/abs/2509.23519."
    ],
    "durationSeconds": 8.955979964000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0862d968-177e-4eab-a87f-3c6cfb35e476",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-30T07:48:24.594Z_

<details><summary>↩ Tool result · `toolu_01U8RFM4yETTwBmGsnN5TFat`</summary>

```text
Web search results for query: "conformal prediction distribution shift robust RAG vacuous prediction sets 2026 arXiv"

Links: [{"title":"[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/abs/2603.16817"},{"title":"[2602.19483] Making Conformal Predictors Robust in Healthcare Settings: a Case Study on EEG Classification","url":"https://arxiv.org/abs/2602.19483"},{"title":"Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/pdf/2502.14105"},{"title":"[2604.16217] Beyond Surface Statistics: Robust Conformal Prediction for LLMs via Internal Representations","url":"https://arxiv.org/abs/2604.16217"},{"title":"[2602.12616] When Environments Shift: Safe Planning with Generative Priors and Robust Conformal Prediction","url":"https://arxiv.org/abs/2602.12616"},{"title":"Not all distributional shifts are equal: Fine-grained robust conformal inference","url":"https://arxiv.org/pdf/2402.13042"},{"title":"[2601.02998] Multi-Distribution Robust Conformal Prediction","url":"https://arxiv.org/abs/2601.02998"}]

I found several relevant arXiv papers from 2026 on conformal prediction with distribution shift robustness. Here are the key results:

**Most Relevant Match:**

A paper titled "Is Conformal Factuality for RAG-based LLMs Robust?" finds that conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, and the conformal factuality guarantee is not robust to distribution shifts and distractors, highlighting the need for new approaches for reliability with robustness and usefulness as key metrics. This paper (arXiv:2603.16817) was published in March 2026.

**Other Related Papers:**

- A paper on robust conformal prediction for LLMs notes that conformal prediction provides finite-sample validity under exchangeability, and internal representations can provide more informative conformal scores when surface-level uncertainty is unstable under distribution shift (arXiv:2604.16217, April 2026).

- Another paper addresses conformal prediction under Lévy-Prokhorov distribution shifts by reducing complex high-dimensional distribution shifts to one-dimensional shifts, and constructs robust conformal prediction intervals that remain valid under distribution shifts (arXiv:2502.14105).

- A paper on multi-distribution robust conformal prediction shows their method delivers valid worst-case coverage across multiple distributions while greatly reducing set size compared to standard approaches (arXiv:2601.02998, January 2026).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7eeb1341-0b65-4d9b-8501-f8f430052b8e",
  "isSidechain": false,
  "promptId": "815a8749-b513-453f-8657-19f64f89c02b",
  "type": "user",
  "uuid": "755624ae-2152-44fd-a03a-677d4d29f35d",
  "toolUseResult": {
    "query": "conformal prediction distribution shift robust RAG vacuous prediction sets 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_016e3MqZjLz5HzPWxMTPozZv",
        "content": [
          {
            "title": "[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights",
            "url": "https://arxiv.org/abs/2603.16817"
          },
          {
            "title": "[2602.19483] Making Conformal Predictors Robust in Healthcare Settings: a Case Study on EEG Classification",
            "url": "https://arxiv.org/abs/2602.19483"
          },
          {
            "title": "Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/pdf/2502.14105"
          },
          {
            "title": "[2604.16217] Beyond Surface Statistics: Robust Conformal Prediction for LLMs via Internal Representations",
            "url": "https://arxiv.org/abs/2604.16217"
          },
          {
            "title": "[2602.12616] When Environments Shift: Safe Planning with Generative Priors and Robust Conformal Prediction",
            "url": "https://arxiv.org/abs/2602.12616"
          },
          {
            "title": "Not all distributional shifts are equal: Fine-grained robust conformal inference",
            "url": "https://arxiv.org/pdf/2402.13042"
          },
          {
            "title": "[2601.02998] Multi-Distribution Robust Conformal Prediction",
            "url": "https://arxiv.org/abs/2601.02998"
          }
        ]
      },
      "I found several relevant arXiv papers from 2026 on conformal prediction with distribution shift robustness. Here are the key results:\n\n**Most Relevant Match:**\n\nA paper titled \"Is Conformal Factuality for RAG-based LLMs Robust?\" finds that conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, and the conformal factuality guarantee is not robust to distribution shifts and distractors, highlighting the need for new approaches for reliability with robustness and usefulness as key metrics. This paper (arXiv:2603.16817) was published in March 2026.\n\n**Other Related Papers:**\n\n- A paper on robust conformal prediction for LLMs notes that conformal prediction provides finite-sample validity under exchangeability, and internal representations can provide more informative conformal scores when surface-level uncertainty is unstable under distribution shift (arXiv:2604.16217, April 2026).\n\n- Another paper addresses conformal prediction under Lévy-Prokhorov distribution shifts by reducing complex high-dimensional distribution shifts to one-dimensional shifts, and constructs robust conformal prediction intervals that remain valid under distribution shifts (arXiv:2502.14105).\n\n- A paper on multi-distribution robust conformal prediction shows their method delivers valid worst-case coverage across multiple distributions while greatly reducing set size compared to standard approaches (arXiv:2601.02998, January 2026)."
    ],
    "durationSeconds": 13.691665137,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7eeb1341-0b65-4d9b-8501-f8f430052b8e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-30T07:48:24.601Z_

```json
{
  "parentUuid": "755624ae-2152-44fd-a03a-677d4d29f35d",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "33fc381d-9747-401b-bbb1-4f3b2143399c",
  "timestamp": "2026-05-30T07:48:24.601Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 32 · 2026-05-30T07:48:28.638Z_

<details><summary>Logged reasoning block</summary>

```text
Let me do one more round of searches to check for any directly competing work that combines conformal prediction with adversarial robustness in RAG, and to verify the "Consensus Trap" and other recent papers mentioned.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33fc381d-9747-401b-bbb1-4f3b2143399c",
  "isSidechain": false,
  "requestId": "req_011CbYPJL6r9sa1rsGVxgsta",
  "type": "assistant",
  "uuid": "32e2a0bf-25b1-4e59-8f1a-7c7ad4cf13b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WUdXqvsPHFAgq26CzwLcvR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1377,
      "cache_creation_input_tokens": 1824,
      "cache_read_input_tokens": 21940,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1824,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1377,
          "output_tokens": 211,
          "cache_read_input_tokens": 21940,
          "cache_creation_input_tokens": 1824,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1824
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

_source line 33 · 2026-05-30T07:48:29.141Z_

Let me do one final round of searches to check for any directly competing work and verify additional claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32e2a0bf-25b1-4e59-8f1a-7c7ad4cf13b0",
  "isSidechain": false,
  "requestId": "req_011CbYPJL6r9sa1rsGVxgsta",
  "type": "assistant",
  "uuid": "8d3717c6-9470-4b70-88ea-e48e929d3458",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WUdXqvsPHFAgq26CzwLcvR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1377,
      "cache_creation_input_tokens": 1824,
      "cache_read_input_tokens": 21940,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1824,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1377,
          "output_tokens": 211,
          "cache_read_input_tokens": 21940,
          "cache_creation_input_tokens": 1824,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1824
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

_source line 34 · 2026-05-30T07:48:30.087Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017GZZBbBXDngF2tuY3A4h9n`</summary>

```json
{
  "query": "\"conformal abstention\" OR \"conformal prediction\" adversarial poisoning RAG abstention 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d3717c6-9470-4b70-88ea-e48e929d3458",
  "isSidechain": false,
  "requestId": "req_011CbYPJL6r9sa1rsGVxgsta",
  "type": "assistant",
  "uuid": "163446d4-6239-42e0-b88f-b03ca7567d9f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WUdXqvsPHFAgq26CzwLcvR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1377,
      "cache_creation_input_tokens": 1824,
      "cache_read_input_tokens": 21940,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1824,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1377,
          "output_tokens": 211,
          "cache_read_input_tokens": 21940,
          "cache_creation_input_tokens": 1824,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1824
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

_source line 35 · 2026-05-30T07:48:30.650Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RooT3V2aM2M7Wsh5cf6zM7`</summary>

```json
{
  "query": "consensus trap adversarial majority voting multi-agent arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "163446d4-6239-42e0-b88f-b03ca7567d9f",
  "isSidechain": false,
  "requestId": "req_011CbYPJL6r9sa1rsGVxgsta",
  "type": "assistant",
  "uuid": "02d64a63-aabc-470c-b989-49c69c6c712b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WUdXqvsPHFAgq26CzwLcvR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1377,
      "cache_creation_input_tokens": 1824,
      "cache_read_input_tokens": 21940,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1824,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1377,
          "output_tokens": 211,
          "cache_read_input_tokens": 21940,
          "cache_creation_input_tokens": 1824,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1824
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

_source line 36 · 2026-05-30T07:48:36.807Z_

<details><summary>↩ Tool result · `toolu_017GZZBbBXDngF2tuY3A4h9n`</summary>

```text
Web search results for query: ""conformal abstention" OR "conformal prediction" adversarial poisoning RAG abstention 2025 2026"

Links: [{"title":"Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks","url":"https://arxiv.org/html/2412.16708v2"},{"title":"Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks - King's College London","url":"https://kclpure.kcl.ac.uk/portal/en/publications/verifiably-robust-conformal-prediction-for-probabilistic-guarante"},{"title":"Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0031320325007113"},{"title":"Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning","url":"https://arxiv.org/pdf/2410.09878"},{"title":"Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://arxiv.org/html/2506.07804v1"},{"title":"GitHub - Arstanley/Awesome-Trustworthy-RAG · GitHub","url":"https://github.com/Arstanley/Awesome-Trustworthy-RAG"},{"title":"Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks","url":"https://arxiv.org/pdf/2412.16708"}]

Based on the search results, here are the key findings on conformal prediction/abstention and adversarial poisoning in RAG systems from 2025-2026:

## Conformal Prediction and Adversarial Attacks

VRCP (Verifiably Robust Conformal Prediction) leverages neural network verification methods to recover coverage guarantees under adversarial attacks. VRCP can be used to mitigate poisoning attacks. This 2026 paper represents a significant advancement, as VRCP is automatically robust to feature poisoning attacks and supports both classification and regression with all widely-used norms on adversarial perturbation bounds.

Another recent work addresses reliable prediction sets (RPS), the first scalable and efficient method for making conformal prediction more reliable under training and calibration poisoning.

## RAG Under Adversarial Poisoning

RAG systems are vulnerable to adversarial poisoning attacks where attackers inject adversarial data into the underlying RAG database to manipulate retriever output and reduce model accuracy. Recent research evaluates RAG robustness using F1 scores and abstentions (the proportion that LLMs didn't answer) under adversarial, guiding and untouched contexts.

The research suggests that **conformal prediction methods with abstention mechanisms** are emerging as promising approaches for improving RAG robustness against adversarial poisoning attacks in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "163446d4-6239-42e0-b88f-b03ca7567d9f",
  "isSidechain": false,
  "promptId": "815a8749-b513-453f-8657-19f64f89c02b",
  "type": "user",
  "uuid": "c104f19e-5bac-48b8-badd-d72424a83153",
  "toolUseResult": {
    "query": "\"conformal abstention\" OR \"conformal prediction\" adversarial poisoning RAG abstention 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FQo8P11Uq6QVryAP4cv54X",
        "content": [
          {
            "title": "Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks",
            "url": "https://arxiv.org/html/2412.16708v2"
          },
          {
            "title": "Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks - King's College London",
            "url": "https://kclpure.kcl.ac.uk/portal/en/publications/verifiably-robust-conformal-prediction-for-probabilistic-guarante"
          },
          {
            "title": "Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S0031320325007113"
          },
          {
            "title": "Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning",
            "url": "https://arxiv.org/pdf/2410.09878"
          },
          {
            "title": "Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability",
            "url": "https://arxiv.org/html/2506.07804v1"
          },
          {
            "title": "GitHub - Arstanley/Awesome-Trustworthy-RAG · GitHub",
            "url": "https://github.com/Arstanley/Awesome-Trustworthy-RAG"
          },
          {
            "title": "Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks",
            "url": "https://arxiv.org/pdf/2412.16708"
          }
        ]
      },
      "Based on the search results, here are the key findings on conformal prediction/abstention and adversarial poisoning in RAG systems from 2025-2026:\n\n## Conformal Prediction and Adversarial Attacks\n\nVRCP (Verifiably Robust Conformal Prediction) leverages neural network verification methods to recover coverage guarantees under adversarial attacks. VRCP can be used to mitigate poisoning attacks. This 2026 paper represents a significant advancement, as VRCP is automatically robust to feature poisoning attacks and supports both classification and regression with all widely-used norms on adversarial perturbation bounds.\n\nAnother recent work addresses reliable prediction sets (RPS), the first scalable and efficient method for making conformal prediction more reliable under training and calibration poisoning.\n\n## RAG Under Adversarial Poisoning\n\nRAG systems are vulnerable to adversarial poisoning attacks where attackers inject adversarial data into the underlying RAG database to manipulate retriever output and reduce model accuracy. Recent research evaluates RAG robustness using F1 scores and abstentions (the proportion that LLMs didn't answer) under adversarial, guiding and untouched contexts.\n\nThe research suggests that **conformal prediction methods with abstention mechanisms** are emerging as promising approaches for improving RAG robustness against adversarial poisoning attacks in 2025-2026."
    ],
    "durationSeconds": 6.715368234000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "163446d4-6239-42e0-b88f-b03ca7567d9f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-30T07:48:41.926Z_

<details><summary>↩ Tool result · `toolu_01RooT3V2aM2M7Wsh5cf6zM7`</summary>

```text
Web search results for query: "consensus trap adversarial majority voting multi-agent arXiv 2026"

Links: [{"title":"[2604.17139] The Consensus Trap: Rescuing Multi-Agent LLMs from Adversarial Majorities via Token-Level Collaboration","url":"https://arxiv.org/abs/2604.17139"},{"title":"The Consensus Trap: Rescuing Multi-Agent LLMs from Adversarial Majorities via Token-Level Collaboration","url":"https://arxiv.org/html/2604.17139"},{"title":"Many-to-One Adversarial Consensus: Exposing Multi-Agent Collusion Risks in AI-Based Healthcare","url":"https://arxiv.org/html/2512.03097"},{"title":"Resilient Consensus for Multi-Agent Systems under Adversarial Spreading   Processes","url":"https://arxiv.org/pdf/2012.13757"},{"title":"Many-to-One Adversarial Consensus: Exposing Multi-Agent Collusion Risks in AI-Based Healthcare","url":"https://arxiv.org/pdf/2512.03097"},{"title":"[2602.09341] Auditing Multi-Agent LLM Reasoning Trees Outperforms Majority Vote and LLM-as-Judge","url":"https://arxiv.org/abs/2602.09341"}]

Based on the search results, I found highly relevant research on this topic. Here's what I discovered:

## Primary Result: "The Consensus Trap" Paper

The main paper matching your query is "The Consensus Trap: Rescuing Multi-Agent LLMs from Adversarial Majorities via Token-Level Collaboration," which addresses how multi-agent large language model architectures increasingly rely on response-level aggregation, such as Majority Voting (MAJ), to raise reasoning ceilings.

### Key Findings

The paper reveals a critical structural vulnerability in current multi-agent systems: response-level aggregation collapses when corrupted agents form a local majority, because voting aggregates fully-formed conclusions and is blind to flawed intermediate logic.

### Proposed Solution

The authors propose Token-Level Round-Robin (RR) Collaboration, where agents sequentially interleave generation within a shared auto-regressive context, formalizing this as a discrete-time dynamical system that transitions aggregation from a brittle counting of final votes (a linear sum) to a dynamic, interwoven chain of logic (a non-linear operator product).

They prove that the honest model's restorative pull can overpower adversarial corruptions even when corrupted agents form a majority, and demonstrate through empirical evaluation that while MAJ collapses when corrupted agents reach a majority, RR maintains robust accuracy well beyond this critical threshold.

The paper was published on arXiv on April 18, 2026 (arxiv ID: 2604.17139).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02d64a63-aabc-470c-b989-49c69c6c712b",
  "isSidechain": false,
  "promptId": "815a8749-b513-453f-8657-19f64f89c02b",
  "type": "user",
  "uuid": "8c7d317e-84a9-4ff7-9321-39cbe9c3fe5c",
  "toolUseResult": {
    "query": "consensus trap adversarial majority voting multi-agent arXiv 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TqhHoMt5hf7LgWoLKJimF8",
        "content": [
          {
            "title": "[2604.17139] The Consensus Trap: Rescuing Multi-Agent LLMs from Adversarial Majorities via Token-Level Collaboration",
            "url": "https://arxiv.org/abs/2604.17139"
          },
          {
            "title": "The Consensus Trap: Rescuing Multi-Agent LLMs from Adversarial Majorities via Token-Level Collaboration",
            "url": "https://arxiv.org/html/2604.17139"
          },
          {
            "title": "Many-to-One Adversarial Consensus: Exposing Multi-Agent Collusion Risks in AI-Based Healthcare",
            "url": "https://arxiv.org/html/2512.03097"
          },
          {
            "title": "Resilient Consensus for Multi-Agent Systems under Adversarial Spreading   Processes",
            "url": "https://arxiv.org/pdf/2012.13757"
          },
          {
            "title": "Many-to-One Adversarial Consensus: Exposing Multi-Agent Collusion Risks in AI-Based Healthcare",
            "url": "https://arxiv.org/pdf/2512.03097"
          },
          {
            "title": "[2602.09341] Auditing Multi-Agent LLM Reasoning Trees Outperforms Majority Vote and LLM-as-Judge",
            "url": "https://arxiv.org/abs/2602.09341"
          }
        ]
      },
      "Based on the search results, I found highly relevant research on this topic. Here's what I discovered:\n\n## Primary Result: \"The Consensus Trap\" Paper\n\nThe main paper matching your query is \"The Consensus Trap: Rescuing Multi-Agent LLMs from Adversarial Majorities via Token-Level Collaboration,\" which addresses how multi-agent large language model architectures increasingly rely on response-level aggregation, such as Majority Voting (MAJ), to raise reasoning ceilings.\n\n### Key Findings\n\nThe paper reveals a critical structural vulnerability in current multi-agent systems: response-level aggregation collapses when corrupted agents form a local majority, because voting aggregates fully-formed conclusions and is blind to flawed intermediate logic.\n\n### Proposed Solution\n\nThe authors propose Token-Level Round-Robin (RR) Collaboration, where agents sequentially interleave generation within a shared auto-regressive context, formalizing this as a discrete-time dynamical system that transitions aggregation from a brittle counting of final votes (a linear sum) to a dynamic, interwoven chain of logic (a non-linear operator product).\n\nThey prove that the honest model's restorative pull can overpower adversarial corruptions even when corrupted agents form a majority, and demonstrate through empirical evaluation that while MAJ collapses when corrupted agents reach a majority, RR maintains robust accuracy well beyond this critical threshold.\n\nThe paper was published on arXiv on April 18, 2026 (arxiv ID: 2604.17139)."
    ],
    "durationSeconds": 11.272516623000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "02d64a63-aabc-470c-b989-49c69c6c712b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores  ## Core Problem  RAG systems in ad…",
  "leafUuid": "8c7d317e-84a9-4ff7-9321-39cbe9c3fe5c",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate poisoning-robust conformal RAG abstention",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867"
}
```

---

### Assistant

_source line 40 · 2026-05-30T07:49:45.107Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the field. Let me synthesize all the information and provide a comprehensive evaluation.

Key findings from my research:

1. **Conformal Prediction for RAG**: TRAQ (NAACL 2024) and C-RAG (ICML 2024) are well-established. Chen et al. (arXiv:2603.16817, Mar 2026) showed these methods produce vacuous outputs under distribution shift. This gap is real and well-documented.

2. **Corpus Poisoning Attacks**: PoisonedRAG (USENIX Security 2025), CorruptRAG (2025) are real threats with high ASR. The attack landscape is well-characterized.


3. **RobustRAG** uses an isolate-then-aggregate certified defense approach from SaTML 2026, but it only provides point estimates without coverage guarantees or abstention options. **ReliabilityRAG** (NeurIPS 2025) applies graph-theoretic methods with natural language inference for robust filtering, though it similarly lacks conformal guarantees. **RPS** (ICLR 2025 Spotlight) tackles calibration-set poisoning rather than test-time retrieval corruption, which is a distinct problem. I'm also seeing references to "The Consensus Trap" paper (arXiv:2604.17139) that appears relevant to this discussion.

The key finding is that no existing work combines conformal abstention with retrieval-poisoning robustness—the gap the proposal identifies seems legitimate. Looking at the research problem itself, the gap is well-motivated and genuine. The threat model of corpus poisoning is practical and well-studied, and the application domains like medical, legal, and financial contexts make this genuinely important. The method's core insight is elegant: reducing high-dimensional adversarial corruption to a bounded total variation shift in the 1D nonconformity score space is a clever theoretical contribution.

The approach builds naturally on prior work, grounding itself in the LP-shift framework and extending CRC with TV-inflated quantiles. The three arguments for why simpler combinations don't work are well-reasoned and preemptively address obvious reviewer concerns. Using NLI-based agreement scoring follows established approaches reasonably. There are two concerns worth noting: the TV bound could be loose, potentially causing excessive abstention, though the proposal plans to measure this empirically; and the clean-condition variance issue where different passage groups might inflate disagreement scores even without poisoning, which the proposal acknowledges as a potential limitation. The experimental design includes eight baselines and appears comprehensive.

The evaluation covers standard RAG benchmarks like NQ, HotpotQA, and MS-MARCO alongside domain-specific datasets like PubMedQA. The attack surface is well-considered with PoisonedRAG, CorruptRAG, DoS-type attacks, and notably an agreement-aware adaptive attack that demonstrates serious thinking about adversarial robustness. The ablation matrix systematically varies K and n values, score functions, calibration and partition strategies. Diagnostic experiments probe NLI reliability, TV bound tightness, and sensitivity to k. Testing across three model scales provides additional robustness to the findings.

On feasibility, the K separate LLM calls per query is computationally intensive but workable, especially with 7B models. The approach avoids retraining by leveraging off-the-shelf components like DeBERTa-v3-large for NLI scoring. The experimental scale of 200-300 queries per setting is reasonable for conformal prediction work, and the practical compromise of full ablation on 7B with selective testing on larger models is sensible. The writing is exceptionally clear and well-structured.

The proposal stands out because it genuinely addresses an unexplored intersection of conformal prediction, RAG, and adversarial robustness. The theoretical contribution—reducing high-dimensional adversarial corruption to a bounded 1D TV shift through partition-induced reduction—is elegant and principled. The experimental design is comprehensive, with 8 baselines, 4 attack methods including adaptive ones, and a thorough ablation matrix that demonstrates real rigor.

The main risks center on whether the TV bound will be tight enough in practice to avoid excessive abstention, and whether DeBERTa's NLI reliability holds up under adversarial conditions—if it doesn't, the entire agreement-based validation mechanism could fail. For AAAI specifically, the venue's focus on AI safety and trustworthy AI aligns well with this work, and the theoretical contribution feels fresh enough. But acceptance rates hover around 20-25%, so even a well-executed proposal faces steep odds—I'm settling on roughly 40-45% as my estimate, acknowledging that while this is clearly above-average work with genuine novelty, top conferences demand an exceptionally high bar. The proposal's strengths—comprehensive experiments, thorough related work, and clear writing—are substantial, but the core method's simplicity and potential perception as an incremental combination of existing techniques create real uncertainty about acceptance. Balancing these factors, I'd estimate the acceptance probability at 40-42%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c7d317e-84a9-4ff7-9321-39cbe9c3fe5c",
  "isSidechain": false,
  "requestId": "req_011CbYPKaWYu9aGJH9M5ZD6n",
  "type": "assistant",
  "uuid": "f34b180c-0b98-41bc-8a3f-482e4087e5ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALrb8BkFDBeDWXN4PA6dH4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3080,
      "cache_read_input_tokens": 23764,
      "output_tokens": 8424,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3080,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8424,
          "cache_read_input_tokens": 23764,
          "cache_creation_input_tokens": 3080,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3080
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

_source line 41 · 2026-05-30T07:51:58.967Z_

Now I have sufficient research to conduct a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:

- TRAQ (NAACL 2024): 首个为 RAG 提供端到端统计正确性保证的方法，基于 conformal prediction 构建语义等价预测集。PRCA 的直接前驱，作为 baseline 之一。
- C-RAG (ICML 2024): 为 RAG 建立 certified generation risk 框架。同样假设 benign retrieval，是 PRCA 的另一直接前驱/baseline。
- Conformal Risk Control / CRC (ICLR 2024, Angelopoulos et al.): PRCA 核心理论依赖——CRC 将 conformal prediction 扩展到控制任意单调损失函数的期望值，并提供 distribution shift 下的扩展。PRCA 利用其 TV-inflated quantile 机制吸收对抗性扰动。
- RPS: Provably Reliable Conformal Prediction Sets (ICLR 2025 Spotlight, Scholten & Günnemann): 首个在数据投毒下仍可靠的 conformal prediction 方法，通过 smoothed score + majority voting。但仅处理 calibration-set poisoning，不处理 test-time retrieval corruption。PRCA 正确区分了自己与 RPS 的适用场景。
- RobustRAG (SaTML 2026, Xiang et al., Princeton/NVIDIA): 首个 certifiably robust RAG 防御，采用 isolate-then-aggregate。提供 robust point estimates 但无 coverage certificates 或 abstention 机制。PRCA 的 partition 思路与 RobustRAG 有继承关系，但目标不同（abstention + coverage certificate vs. robust answer）。
- ReliabilityRAG (NeurIPS 2025): 基于图论 MIS + NLI contradiction detection 的 provably robust document filtering。PRCA 借鉴了其 NLI-based 方法，但同样指出 ReliabilityRAG 缺乏 abstention/coverage guarantee。
- Chen et al. (arXiv:2603.16817, Mar 2026): 实证证明 TRAQ/C-RAG 等 conformal factuality 方法在 distribution shift 和 retrieval corruption 下产生 vacuous prediction sets。直接验证了 PRCA 所要填补的 gap。
- PoisonedRAG (USENIX Security 2025): 5 个恶意文档即可达 90%+ ASR，验证 corpus poisoning 的现实威胁。
- CorruptRAG (arXiv 2025): 单文档即可实现高 ASR，使 poisoning 攻击更具隐蔽性。
- RAGPart & RAGMask (arXiv:2512.24268, Dec 2025): 在 retrieval 阶段使用 document partitioning 稀释 poisoning。与 PRCA 互补——RAGPart 在 retrieval 阶段操作，PRCA 在 generation/calibration 阶段操作。
- The Consensus Trap (arXiv:2604.17139, Apr 2026): 证明 response-level majority voting 在 corrupted agents 形成 local majority 时失败。PRCA 承认此风险但论证在 k < n/2 威胁模型下 honest majority 得以保留。
- Conformal Prediction under Lévy-Prokhorov Shifts (arXiv:2502.14105): 将高维分布偏移归约到一维 score 偏移。PRCA 的 partition-induced TV bound 是这一思路在对抗性 retrieval corruption 场景下的具体实例化。
- Semantic Chameleon (arXiv Mar 2026): 基于梯度的 corpus-dependent 攻击，能让 poisoned passages 看起来 authoritative。解释了为何 logprob-based confidence 在对抗环境下失效。
- VRCP: Verifiably Robust Conformal Prediction (2026): 利用神经网络验证方法在对抗攻击下恢复 coverage guarantees，但针对的是 input-space perturbation 而非 retrieval corpus poisoning。

- 调研总结: 该领域在"conformal prediction for RAG"和"certified RAG defense"两条线上分别有成熟工作，但两者的交叉——即在 adversarial retrieval corruption 下提供 distribution-free abstention guarantees——确实是一个未被填补的真实 gap。PRCA 精准定位了这一交叉空白，且 Chen et al. (Mar 2026) 的实证结果直接验证了此 gap 的存在和重要性。

【整体印象】:

作为审稿人，我的第一反应是：这是一篇研究问题定义极其精准、理论架构清晰、实验设计异常完备的 proposal。它识别出了一个**真实且经过验证的研究空白**——conformal prediction for RAG 的所有现有方法在 retrieval corruption 下失效（Chen et al. 2026 直接证实），而 certified RAG defense 提供 robust answers 但无 coverage certificate 或 abstention 机制。Proposal 的 partition-induced reduction 思想（将高维对抗性 corruption 归约为一维 bounded TV shift）是一个优雅的理论贡献，不是对已有方法的简单拼接。

我的整体倾向是 **weak accept**。理由：问题真实且重要，理论贡献清晰（partition → TV bound → CRC absorption），实验方案极其周全（8 baselines, 4 attack methods including adaptive, comprehensive ablation），且 proactive 地回答了"为什么不能简单组合现有方法"这个最可能的 reviewer 质疑。主要顾虑在于：(a) TV bound m/K 的 tightness 可能不够，导致实际 abstention rate 过高；(b) 方法一旦被拆解，可能被视为 RobustRAG partition + CRC + ReliabilityRAG NLI 的"理论包装"；(c) 核心贡献偏理论整合而非算法创新。

【核心贡献】:

核心贡献是 **partition-induced reduction**：通过将 retrieved passages 分割为 disjoint groups 并计算 inter-group agreement，将任意 test-time adversarial retrieval corruption 确定性地归约为 nonconformity score 分布上的 bounded TV shift，继而被 CRC 的 inflated quantile 吸收，产出形式化 coverage certificate。

这一贡献的价值在于：
1. **理论桥梁**：首次连接了 certified RAG defense 和 conformal abstention 两个独立的研究方向，且给出了数学上可证的 coverage guarantee。
2. **实用性**：在医疗、法律、金融等高风险场景中，"知道自己不知道"（abstention）比"给出可能错误的 robust answer"更安全。
3. **通用性**：partition-induced reduction 思想可能推广到其他需要从 point-estimate defense 提升到 distributional guarantee 的场景（proposal 在 Discussion 中有提及）。

对领域的价值：中等偏高。这不是一个"改变整个领域方向"的贡献，但它填补了一个真实的、被明确证实的 gap，且理论机制清晰。

【方法合理性】:

方法整体合理，各组件有明确的理论动机：

1. **Partition-and-Generate**: 直接继承 RobustRAG 的 isolate-then-aggregate 思想，将 partition 从"产出 robust answer"重新定位为"产出 bounded TV shift"。合理。
2. **Agreement Nonconformity Score**: 使用 NLI entailment 的 pairwise agreement 作为 nonconformity score，满足 CRC 的 monotone-loss 要求。比 exact match 更鲁棒（处理 surface variation），比 logprob 更抗对抗性攻击。合理。
3. **TV-Bounded Calibration**: 利用 CRC 框架处理 TV-bounded shift。理论上直接、正确。
4. **"Why not simply combine" 分析**: 三个 alternative 的失败分析（RobustRAG+CP、full-context self-consistency+CP、logprob+CP）是 proposal 的一大亮点，精准预判并回应了最可能的 reviewer 质疑。

**更简单的替代方案？** 
- 最自然的替代是 "RobustRAG + standard CP"（proposal 已分析为何失败——exchangeability 被打破且 shift 未被 bound）。
- 另一个替代是直接用 self-consistency voting + conformal（proposal 也分析了为何在 poisoning 下失败——所有 samples 共享同一 poisoned context）。
- Proposal 已系统性地排除了这些 shortcuts，且将 naive pipeline (RobustRAG + TRAQ) 纳入 baseline 做实证验证。这是非常成熟的方法论。

**潜在问题**:
- TV bound m/K 是 worst-case combinatorial bound，可能过于保守。Proposal 承认这一点并计划 empirically 评估 tightness ratio，但如果 gap 太大，实际效用存疑。
- NLI model (DeBERTa-v3-large) 在 adversarial outputs 上的可靠性未被验证。Proposal 设计了 diagnostic experiment 来评估，但如果 NLI 不可靠，整个 agreement score 机制的基础被动摇。
- K 个独立 LLM 调用的计算开销可能被 reviewer 质疑，但 proposal 已纳入 efficiency metrics。

【5 维度打分】:

1. 研究问题: 【强】 — 
   问题定义精准，填补了经验证的真实 gap：Chen et al. (arXiv:2603.16817) 直接证明现有 conformal RAG 方法在 retrieval corruption 下失效，RobustRAG/ReliabilityRAG 提供 robust point estimates 但无 abstention/coverage certificate。在医疗、法律等高风险场景中，distribution-free abstention guarantee 有明确的实用价值。问题的两个"父领域"（conformal prediction for RAG 和 certified RAG defense）都有成熟的顶会工作，说明研究社区对两个方向都有兴趣，交叉点有天然受众。

2. 方法与创新: 【中偏强】 — 
   Partition-induced reduction 是一个清晰且优雅的理论贡献，将 RobustRAG 的 partition 思想从"产出 robust answer"重新诠释为"产出 bounded TV shift"，并与 CRC (ICLR 2024) 对接。这不是简单的工具拼接——proposal 清晰论证了三种 naive combination 为何失败，且 LP-shift framework (arXiv:2502.14105) 提供了理论类比支撑。但坦率地说，一旦 insight 被揭示，方法本身（partition → pairwise NLI agreement → TV-inflated CRC threshold）相对 straightforward。创新主要在"理论整合与重新诠释"而非"全新算法设计"。与 RobustRAG (SaTML 2026) 的 partition 策略、ReliabilityRAG (NeurIPS 2025) 的 NLI scoring 有明显的技术继承关系，可能被部分 reviewer 视为 incremental。

3. 实验设计: 【强】 — 
   这是整篇 proposal 的最大亮点之一。8 个 baselines 覆盖了所有主要竞争者（TRAQ, C-RAG, Conformal-RAG, RobustRAG, ReliabilityRAG, RAGPart），且特别包含了 compute-normalized baseline (TRAQ + K× self-consistency) 和 naive pipeline (RobustRAG + TRAQ) 来实证验证理论论证——这是非常成熟的实验设计。4 种 attack methods 包括 adaptive attack（agreement-aware，攻击者知道 partition 结构）。ablation matrix 全面且务实（full ablation on 7B, core config on 32B/72B）。3 个 diagnostic experiments（NLI reliability, TV bound tightness, k sensitivity）针对方法的核心假设做验证。达到甚至超过了该领域的实验标准（PoisonedRAG, RobustRAG 的实验规模和 baseline 数量）。

4. 可行性: 【中偏强】 — 
   方法不需要训练新模型，使用 off-the-shelf LLM + DeBERTa NLI。主要计算瓶颈是 K 次独立 LLM 调用（K ∈ {3-10}），对 7B 模型尚可接受，但 72B 模型在多 setting × 多 dataset × 多 attack 的全矩阵实验下计算需求显著。Calibration 需要 clean corpus (n_cal ≥ 500)，这是标准假设。200-300 queries per setting 的规模对 conformal prediction 实验合理。唯一的不确定性在于 adaptive attack 的实现复杂度和 TV bound tightness 的实验结果——如果 bound 太松或 NLI 不可靠，可能需要调整方法。

5. 写作与呈现: 【强】 — 
   Proposal 结构清晰，逻辑流畅。Research landscape 部分几乎是一篇小型 survey，精准定位每个相关工作并说明差异。"Why not simply combine?" 部分是出色的预防性论证，直接堵住了最可能的 reviewer 质疑。实验设计的组织（datasets → attacks → models → baselines → metrics → ablation → diagnostics）层次分明。理论论述（partition → TV bound → CRC absorption）的逻辑链条简洁有力。唯一可改进的是：对 TV bound tightness 的讨论还可以更深入，以及对 K 的选择是否存在理论最优值的分析。

【概率估计】: [33% - 48%] 中位 40%

【估计理由】:

拉高因素：
(a) 研究问题定义精准，gap 真实且有 2026 年新论文直接验证（Chen et al.），reviewer 难以否认问题的存在性；
(b) 理论贡献清晰——partition-induced reduction 不是 trivial combination，proposal 已系统性论证了 naive combination 为何失败；
(c) 实验设计在同领域中属于上乘水平，8 baselines + adaptive attack + full ablation 达到甚至超过了 RobustRAG/PoisonedRAG 的实验标准；
(d) 时效性极好——2025-2026 年大量相关工作涌现（RobustRAG SaTML'26, ReliabilityRAG NeurIPS'25, Chen et al. Mar'26, Consensus Trap Apr'26），说明社区正在积极探索这个交叉方向，PRCA 踩准了时间窗口。

压低因素：
(a) 核心创新可能被部分 reviewer 视为"对已有工具的巧妙重组"而非"全新方法论"——partition 来自 RobustRAG，NLI scoring 来自 ReliabilityRAG，TV-inflation 来自 CRC，虽然 proposal 论证了为何简单组合不work，但这种"理论整合"类贡献在 AAAI 可能面临 novelty 质疑；
(b) TV bound m/K 的 tightness 是核心风险——如果 bound 太松，abstention rate 会过高，方法的实际效用存疑（虽然 theoretical guarantee 仍成立），这可能导致 "theoretically sound but practically useless" 的 reviewer 评价；
(c) 方法实质上是一个 uncertainty quantification/abstention 框架，贡献边界相对窄——不直接提升 RAG 的 accuracy 或 robustness，而是提供"何时应该 abstain"的 certificate，这在 reviewer 眼中可能价值偏低；
(d) AAAI 整体接收率约 20-25%，高质量但非 breakthrough 的 solid work 面临激烈竞争。

综合来看，这是一篇**高质量的 solid work**，在研究问题定义、理论贡献和实验设计三方面都超过了 AAAI 的平均接收线。主要的不确定性在于 reviewer 对 novelty 的判断——是 "elegant theoretical bridge" 还是 "smart but incremental recombination"。中位数 40% 反映了这种不确定性：如果遇到重视理论清晰度和实验完备度的 reviewer，很可能获得 accept；如果遇到强调 algorithmic novelty 的 reviewer，可能被挑战。

【主要风险】:

1. **Novelty 认知风险**：最可能的拒稿理由是"这是 RobustRAG partition + CRC TV-inflation + ReliabilityRAG NLI 的理论包装，各组件分别已知，组合虽非 trivial 但创新幅度有限"。虽然 proposal 已通过 "Why not simply combine" 论证回应了这一点，但 unsympathetic reviewer 可能仍不买账。

2. **TV bound tightness / 实际效用风险**：如果 empirical 结果显示 TV bound m/K 过于保守（tightness ratio 很低），method 在实践中会过度 abstain，reviewer 可能判定"theoretical guarantee 成立但方法不 practical"——这会直接削弱论文的 significance。

【实施评估】:
  - 计算资源: 中等偏高。每个 query 需要 K 次独立 LLM 调用（K=3-10），对 7B 模型约 3-10× 单次推理成本。3 个 model scales × 4 datasets × 4+ attack methods × 多个 K 值的全矩阵实验需要数百 GPU-hours。估计需要 4-8 张 A100 运行 1-2 周。
  - 数据需求: 低。使用现有公开数据集（NQ, HotpotQA, MS-MARCO, PubMedQA），attack 代码多数已开源（PoisonedRAG on GitHub）。Calibration set (500+ clean queries) 可从现有数据中抽取。
  - 人工介入: 低。无需人工标注。主要人工投入在 adaptive attack 的设计与实现、实验 pipeline 搭建。
  - 训练需求: 无。使用 off-the-shelf LLM（Qwen3.5 系列或 Llama-3-8B）和预训练 NLI 模型（DeBERTa-v3-large）。
  - 新 Benchmark: 无。使用现有 benchmark + 现有攻击方法。
  - 预估周期: 8-12 周。分解：实验 pipeline 搭建 + 攻击实现（2-3 周）→ 核心实验（7B full ablation, 3-4 周）→ 32B/72B 验证（1-2 周）→ 论文撰写（2-3 周）。关键路径在 adaptive attack 实现和 TV bound tightness 实验。
```

Sources:
- [TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction](https://aclanthology.org/2024.naacl-long.210/)
- [C-RAG: Certified Generation Risks for RAG](https://arxiv.org/pdf/2307.04642)
- [Conformal Risk Control (ICLR 2024)](https://proceedings.iclr.cc/paper_files/paper/2024/file/f3549ef9b5ff520a7e41ff3cc306ab2b-Paper-Conference.pdf)
- [RPS: Provably Reliable Conformal Prediction Sets (ICLR 2025 Spotlight)](https://openreview.net/forum?id=ofuLWn8DFZ)
- [RobustRAG: Certifiably Robust RAG against Retrieval Corruption](https://arxiv.org/abs/2405.15556)
- [ReliabilityRAG (NeurIPS 2025)](https://arxiv.org/abs/2509.23519)
- [Chen et al.: Is Conformal Factuality for RAG-based LLMs Robust?](https://arxiv.org/abs/2603.16817)
- [PoisonedRAG (USENIX Security 2025)](https://github.com/sleeepeer/PoisonedRAG)
- [CorruptRAG: Practical Poisoning Attacks against RAG](https://arxiv.org/html/2504.03957v2)
- [RAGPart & RAGMask](https://arxiv.org/pdf/2512.24268)
- [The Consensus Trap (arXiv:2604.17139)](https://arxiv.org/abs/2604.17139)
- [Conformal Prediction under Lévy-Prokhorov Distribution Shifts](https://arxiv.org/pdf/2502.14105)
- [Semantic Chameleon](https://arxiv.org/html/2603.18034v1)
- [VRCP: Verifiably Robust Conformal Prediction](https://www.sciencedirect.com/science/article/pii/S0031320325007113)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f34b180c-0b98-41bc-8a3f-482e4087e5ac",
  "isSidechain": false,
  "requestId": "req_011CbYPKaWYu9aGJH9M5ZD6n",
  "type": "assistant",
  "uuid": "225809d4-6cd2-4bc3-9cd2-cc57bc8ea6c5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALrb8BkFDBeDWXN4PA6dH4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3080,
      "cache_read_input_tokens": 23764,
      "output_tokens": 8424,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3080,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8424,
          "cache_read_input_tokens": 23764,
          "cache_creation_input_tokens": 3080,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3080
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

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores  ## Core Problem  RAG systems in ad…",
  "leafUuid": "225809d4-6cd2-4bc3-9cd2-cc57bc8ea6c5",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate poisoning-robust conformal RAG abstention",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores  ## Core Problem  RAG systems in ad…",
  "leafUuid": "225809d4-6cd2-4bc3-9cd2-cc57bc8ea6c5",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate poisoning-robust conformal RAG abstention",
  "sessionId": "8c716a8b-ada0-4852-9192-47e334d69867"
}
```

---
