# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Poisoning-Robust Conformal Absten

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/516d5c90-34b9-4908-b5ab-b6edba91ee8f.jsonl`
- **Structured JSON:** [`8734668f7e9495641de2.json`](../../sessions/87/8734668f7e9495641de2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T07:47:47.342Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T07:47:47.342Z",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores\n\n## Core Problem\n\nRAG systems in adversarial environments (medical QA, legal retrieval, financial compliance) need distribution-free abstention guarantees when the retrieval corpus is poisoned. Corpus poisoning is a practical threat: CorruptRAG (arXiv 2025) achieves high attack success with a single injected document; PoisonedRAG (USENIX Security 2025) reaches 90%+ ASR with 5 documents. Existing conformal prediction methods for RAG (TRAQ, NAACL 2024; C-RAG, ICML 2024; Conformal-RAG, SIGIR 2025) assume benign retrieval—Chen et al. (arXiv:2603.16817, Mar 2026) demonstrated these guarantees break under distribution shift, producing vacuous outputs. Poisoning-robust CP (RPS, ICLR 2025 Spotlight) addresses calibration-set poisoning, not test-time retrieval corruption. Certified RAG defenses (RobustRAG, SaTML 2026; ReliabilityRAG, NeurIPS 2025) provide robust point estimates but no abstention mechanism or coverage certificates. The gap: no method provides distribution-free abstention guarantees for RAG under adversarial retrieval corruption.\n\n## Core Contribution and Theoretical Insight\n\nPRCA's central contribution is a **partition-induced reduction**: partitioning retrieved passages into disjoint groups and computing inter-group agreement deterministically reduces arbitrary test-time retrieval corruption to a bounded TV shift in the one-dimensional nonconformity score distribution. This bounded shift is absorbed by CRC (ICLR 2024) via inflated quantiles, yielding formal coverage certificates. This reduction—from high-dimensional adversarial corruption to one-dimensional bounded distributional shift—parallels the approach of Conformal Prediction under Lévy-Prokhorov Distribution Shifts (arXiv:2502.14105), which reduces high-dimensional shifts to one-dimensional score shifts via ambiguity sets.\n\n**Why not simply combine existing methods?** Three natural alternatives fail:\n\n(1) **RobustRAG + standard CP**: Running RobustRAG's isolate-then-aggregate to obtain a robust answer, then applying TRAQ/C-RAG for conformal abstention, fails because RobustRAG's aggregation transforms the output distribution in a poisoning-dependent manner. Nonconformity scores from clean calibration are no longer exchangeable with test-time scores under attack, and the magnitude of distributional shift is uncharacterized. PRCA explicitly bounds this shift via partition structure.\n\n(2) **Full-context self-consistency + CP**: Generating K answers from the same full retrieval set and using agreement as a conformal score (the approach of Conformal Abstention, arXiv:2405.01563) fails under poisoning because all K samples share the same poisoned context. The model may produce consistently wrong answers with high agreement, making the score blind to corruption. Partition isolates poisoned passages into a bounded number of groups, enabling detection.\n\n(3) **Logprob-based confidence + CP**: Using LLM token-level logprobabilities as nonconformity scores fails because adversarially crafted passages (e.g., via Semantic Chameleon's gradient-guided attacks, arXiv Mar 2026) are designed to appear authoritative, inflating model confidence on wrong answers. Logprob monotonicity with respect to correctness breaks under adversarial retrieval.\n\n**Partition is a theoretical necessity, not a design choice**: it is the structural mechanism that transforms uncharacterizable adversarial corruption into a bounded, quantifiable distributional shift that CRC can absorb.\n\n## Research Landscape\n\n**Conformal prediction for RAG:** TRAQ (NAACL 2024) and C-RAG (ICML 2024) established conformal prediction for RAG under benign retrieval. Conformal-RAG (SIGIR 2025) extends to group-conditional coverage. Chen et al. (arXiv:2603.16817, Mar 2026) showed all such methods produce vacuous prediction sets under distribution shift and retrieval corruption, but proposed no solution.\n\n**Certified RAG defenses:** RobustRAG (SaTML 2026) provides certified defense via isolate-then-aggregate, achieving certified robust accuracy on RealtimeQA/NQ. ReliabilityRAG (NeurIPS 2025) uses graph-theoretic MIS with NLI-based contradiction detection for provably robust document filtering. Both provide robust point estimates but no coverage certificates or abstention mechanism.\n\n**Poisoning-robust CP:** RPS (ICLR 2025 Spotlight) achieves poisoning-robust CP via smoothed scores and majority voting but assumes calibration-set poisoning—certificates do not transfer to test-time retrieval corruption.\n\n**Partition-based defenses:** RAGPart (arXiv:2512.24268, Dec 2025) uses document partitioning at the retrieval stage (fragment embeddings) to dilute poisoning. Three key differences from PRCA: (1) RAGPart operates at retrieval/embedding stage, PRCA at generation/calibration stage; (2) RAGPart outputs filtered retrieval sets, PRCA outputs {answer, abstain} decisions with coverage certificates; (3) they are complementary—RAGPart can preprocess retrieval before PRCA's certified abstention.\n\n**Adversarial aggregation:** The Consensus Trap (arXiv:2604.17139, Apr 2026) proves response-level majority voting fails when corrupted agents form a local majority. PRCA's majority answer output could face this risk, but: (a) PRCA's primary guarantee is the coverage certificate on the abstention decision, not the majority answer's correctness; (b) under the standard threat model k < n/2, the number of corrupted groups m = ceil(k/floor(n/K)) < K/2, so the honest majority is preserved.\n\n**Attack landscape:** PoisonedRAG (USENIX Security 2025), CorruptRAG (arXiv 2025), RSB Benchmark (May 2025, 13 attack methods × 7 defenses), Semantic Chameleon (arXiv Mar 2026, gradient-guided corpus-dependent attacks).\n\n**Distribution-shift-robust CP:** LP-shift framework (arXiv:2502.14105) reduces high-dimensional shifts to one-dimensional score shifts. PRCA's partition-induced TV bound is a specific instantiation for adversarial retrieval corruption.\n\nNo existing work combines conformal abstention with retrieval-poisoning robustness.\n\n## Proposed Approach\n\n**Step 1: Partition-and-Generate.** Partition top-n retrieved passages into K disjoint groups (random assignment). Generate a per-group answer via isolated LLM calls.\n\n**Step 2: Agreement Nonconformity Score.** For each group pair (i, j), compute NLI entailment probability e(i,j) = P(answer_i entails answer_j) using DeBERTa-v3-large (following ReliabilityRAG's NLI approach). Define:\n\ns = 1 − mean({e(i,j)} over all pairs)\n\nCritical properties: (1) **Monotonicity**: s increases with disagreement; higher s → more likely to abstain, satisfying CRC's monotone-loss requirement. (2) **Corruption-boundedness**: under k-poisoning, at most m = ceil(k/floor(n/K)) groups are corrupted, affecting at most m(K−1) of C(K,2) pairwise comparisons, yielding bounded perturbation to s.\n\n**Toward tighter bounds:** The worst-case TV ≤ m/K is a combinatorial upper bound. Because s is a mean of bounded pairwise scores, the actual perturbation from m corrupted groups may be dampened. We will empirically estimate the actual TV distance between clean and poisoned score CDFs (via bootstrap) and compare against the theoretical bound, reporting the tightness ratio. Exploring concentration-based bounds (leveraging the mean structure) is a concrete research direction.\n\n**Clean-condition variance mitigation:** If different passage groups cover different answer facets, clean-condition agreement variance inflates s and may cause excessive abstention. NLI-based semantic entailment (rather than exact match) is robust to surface variation. Calibration on clean data naturally accounts for residual clean-condition variance in the score distribution.\n\n**Step 3: TV-Bounded Calibration.** Under k-poisoning with K groups, corruption bound m determines maximal TV distance: TV ≤ m/K. Using CRC (ICLR 2024) with TV-inflated quantile: set abstention threshold at the (1 − α + TV)-quantile of calibration scores, yielding formal certificate P(correct or abstain) ≥ 1 − α under k-poisoning.\n\n**Calibration protocol:** Calibration set constructed on clean corpus (standard assumption per RPS, ICLR 2025), n_cal ≥ 500 per dataset. Sensitivity experiment evaluates coverage degradation when actual poisoning budget exceeds assumed k.\n\n**Step 4: Abstention Decision.** At test time, if s > λ (calibrated threshold), abstain; otherwise, output the majority answer across groups.\n\n## Experimental Design\n\n**Datasets:** Primary: NQ, HotpotQA, MS-MARCO (standard RAG benchmarks, used by PoisonedRAG/RobustRAG). Secondary: PubMedQA (domain-specific, core metrics only, validating high-stakes scenario motivation).\n\n**Attack methods:**\n- PoisonedRAG (targeted, k ∈ {1, 3, 5, 10})\n- CorruptRAG (single-document high-ASR)\n- One DoS-type attack from RSB Benchmark (May 2025) taxonomy\n- **Agreement-aware adaptive attack**: attacker knows K-partition structure and optimizes poisoned passage content to maximize cross-group NLI entailment (minimize s) while ensuring target wrong answer\n\n**Models:** Three scales for model-agnosticism: (1) primary: Qwen3.5-7B (or Llama-3-8B); (2) medium: Qwen3.5-32B; (3) large: Qwen3.5-72B. NLI model: DeBERTa-v3-large.\n\n**Baselines (8 methods):**\n- Conformal: TRAQ (NAACL 2024), C-RAG (ICML 2024), Conformal-RAG (SIGIR 2025)\n- Certified defense: RobustRAG (SaTML 2026), ReliabilityRAG (NeurIPS 2025)\n- Partition-based: RAGPart (arXiv:2512.24268)—same partition, no conformal (ablation baseline)\n- Compute-normalized: TRAQ + K× self-consistency voting\n- Naive pipeline: RobustRAG + TRAQ (empirically validates the \"Why not combine?\" theoretical argument)\n\n**Metrics:**\n- Primary: Certified coverage rate, empirical coverage under attack, abstention rate\n- Secondary: Clean accuracy (no attack), prediction set size, vacuousness rate (per Chen et al. 2026)\n- Tradeoff: Coverage vs. abstention at varying α; coverage vs. poisoning budget k; certified vs. empirical gap\n- Efficiency: Wall-clock time per query, token consumption\n\n**Ablation matrix** (full ablation on 7B only; 32B/72B do core config only):\n- K ∈ {1, 3, 5, 7, 10}: K=1 is the degenerate no-partition baseline proving partition necessity\n- n ∈ {10, 20, 30}: retrieval depth vs. certificate tightness\n- Score function: NLI entailment (primary) vs. ROUGE-L vs. exact match\n- Calibration: CRC + TV inflation (full method) vs. CRC without inflation (isolates TV contribution) vs. vanilla split conformal (isolates CRC contribution)\n- Partition strategy: random vs. round-robin by retrieval score\n\n**Diagnostic experiments:**\n- **NLI reliability**: Collect clean-group and corrupted-group LLM outputs under attack; evaluate DeBERTa NLI entailment accuracy and calibration (reliability diagram) on these output pairs. If unreliable, evaluate ensemble NLI or temperature-scaled NLI as robustness enhancement. Motivated by The Semantic Illusion (arXiv:2512.15068) findings on NLI limitations.\n- **TV bound tightness**: Empirically estimate actual TV distance between clean and poisoned score CDFs (bootstrap/KDE) vs. theoretical m/K bound. Report tightness ratio across attack settings.\n- **k sensitivity**: Evaluate coverage degradation when actual poisoning exceeds assumed k upper bound.\n\n**Scale:** 200-300 queries per dataset per setting (primary datasets); 200 queries for PubMedQA. 95% confidence intervals reported. Full ablation on 7B; 32B/72B validate core configuration only.\n\n**Discussion items:** (1) Partition-induced reduction as a potential general principle for lifting point-estimate certified defenses to distributional guarantees (future work). (2) k-poisoning assumption validity across different attack types. (3) Gradient-based adaptive attacks (Semantic Chameleon) as future robustness evaluation.\n\n## Key References\n\n- TRAQ: Trustworthy Retrieval Augmented QA via Conformal Prediction (NAACL 2024)\n- C-RAG: Certified Generation Risks for RAG (ICML 2024)\n- Conformal Risk Control (ICLR 2024)\n- Provably Reliable Conformal Prediction Sets under Poisoning (ICLR 2025 Spotlight)\n- Certifiably Robust RAG against Retrieval Corruption (SaTML 2026)\n- ReliabilityRAG (NeurIPS 2025)\n- Is Conformal Factuality for RAG-based LLMs Robust? (arXiv:2603.16817, Mar 2026)\n- Conformal-RAG: Conditional Conformal Factuality (SIGIR 2025)\n- CorruptRAG: Practical Poisoning Attacks against RAG (arXiv 2025)\n- PoisonedRAG (USENIX Security 2025)\n- RSB Benchmark: Benchmarking Poisoning Attacks against RAG (May 2025)\n- RAGPart & RAGMask (arXiv:2512.24268, Dec 2025)\n- Conformal Prediction under Lévy-Prokhorov Distribution Shifts (arXiv:2502.14105)\n- Semantic Chameleon (arXiv Mar 2026)\n- Mitigating LLM Hallucinations via Conformal Abstention (arXiv:2405.01563)\n- The Consensus Trap (arXiv:2604.17139, Apr 2026)\n- The Semantic Illusion (arXiv:2512.15068)"
}
```

---

### Runtime record

_source line 2 · 2026-05-30T07:47:47.347Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T07:47:47.347Z",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f"
}
```

---

## Round 1

44 recorded events

### User

_source line 3 · 2026-05-30T07:47:47.366Z_

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
  "promptId": "e65aaf3a-f0d3-47c4-8e26-56b5561aafba",
  "type": "user",
  "uuid": "74bf3767-5053-45ad-9f02-14c46325a6a9",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T07:47:47.364Z_

```json
{
  "parentUuid": "74bf3767-5053-45ad-9f02-14c46325a6a9",
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
  "uuid": "b6415fb1-28d1-452f-afda-426ca9c539dd",
  "timestamp": "2026-05-30T07:47:47.364Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T07:47:47.364Z_

```json
{
  "parentUuid": "b6415fb1-28d1-452f-afda-426ca9c539dd",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c5d1051c-cbd3-4432-adba-d81d62011677",
  "timestamp": "2026-05-30T07:47:47.364Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
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
  "aiTitle": "Poisoning-robust conformal abstention for RAG systems",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f"
}
```

---

### Assistant

_source line 7 · 2026-05-30T07:47:55.802Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for AAAI 2026 as the "出口评审 agent" (exit review agent). I need to:

1. First do web searches to understand the research landscape
2. Then evaluate the proposal across 5 dimensions
3. Give a probability estimate

Let me start by doing targeted web searches to understand the current state of the field. The proposal is about "Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores" - combining conformal prediction with robustness against retrieval poisoning in RAG systems.


I'm searching for recent work on conformal prediction applied to RAG systems, corpus poisoning attacks, certified defenses, and poisoning-robust approaches to understand where this proposal sits in the research landscape.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5d1051c-cbd3-4432-adba-d81d62011677",
  "isSidechain": false,
  "requestId": "req_011CbYPFZQTphoxPAfynwL4L",
  "type": "assistant",
  "uuid": "f6689d21-f115-4c89-9822-0645f0459c80",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Msosuf6bHHHPsrcCDM7CLd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7566,
      "cache_read_input_tokens": 11014,
      "output_tokens": 312,
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
          "output_tokens": 312,
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

_source line 8 · 2026-05-30T07:47:55.898Z_

I'll start by conducting thorough web searches to understand the research landscape before making any evaluation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6689d21-f115-4c89-9822-0645f0459c80",
  "isSidechain": false,
  "requestId": "req_011CbYPFZQTphoxPAfynwL4L",
  "type": "assistant",
  "uuid": "1b522e4a-85c7-4e09-8b2f-9fac82789fb7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Msosuf6bHHHPsrcCDM7CLd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7566,
      "cache_read_input_tokens": 11014,
      "output_tokens": 312,
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
          "output_tokens": 312,
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

_source line 9 · 2026-05-30T07:47:55.901Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017fMtotUShgxRyKccVG4Cvb`</summary>

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
  "parentUuid": "1b522e4a-85c7-4e09-8b2f-9fac82789fb7",
  "isSidechain": false,
  "requestId": "req_011CbYPFZQTphoxPAfynwL4L",
  "type": "assistant",
  "uuid": "3abffe9b-583d-4740-a75b-28d66a740a59",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Msosuf6bHHHPsrcCDM7CLd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7566,
      "cache_read_input_tokens": 11014,
      "output_tokens": 312,
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
          "output_tokens": 312,
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

_source line 10 · 2026-05-30T07:47:55.911Z_

<details><summary>↩ Tool result · `toolu_017fMtotUShgxRyKccVG4Cvb`</summary>

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
  "parentUuid": "3abffe9b-583d-4740-a75b-28d66a740a59",
  "isSidechain": false,
  "promptId": "e65aaf3a-f0d3-47c4-8e26-56b5561aafba",
  "type": "user",
  "uuid": "bf67c29a-31fb-41bc-ab45-700240e3ca2a",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "3abffe9b-583d-4740-a75b-28d66a740a59",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
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
  "leafUuid": "bf67c29a-31fb-41bc-ab45-700240e3ca2a",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Poisoning-robust conformal abstention for RAG systems",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f"
}
```

---

### Assistant

_source line 13 · 2026-05-30T07:48:02.533Z_

Now let me conduct the targeted searches. I'll run multiple searches in parallel to cover the key aspects of this proposal's research landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf67c29a-31fb-41bc-ab45-700240e3ca2a",
  "isSidechain": false,
  "requestId": "req_011CbYPGC2cRacrTgozgpmPf",
  "type": "assistant",
  "uuid": "7103119d-c326-4d9d-b9e3-48a8de59302a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lqy8nK2qYw6Sj92ABRaaqF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 840,
      "cache_read_input_tokens": 18580,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 840,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 261,
          "cache_read_input_tokens": 18580,
          "cache_creation_input_tokens": 840,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 840
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

_source line 14 · 2026-05-30T07:48:03.538Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RrDh22EjHbHSCvb4UUNqmt`</summary>

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
  "parentUuid": "7103119d-c326-4d9d-b9e3-48a8de59302a",
  "isSidechain": false,
  "requestId": "req_011CbYPGC2cRacrTgozgpmPf",
  "type": "assistant",
  "uuid": "f3a4fb0b-eeb2-408b-8db6-d1fd85b9e858",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lqy8nK2qYw6Sj92ABRaaqF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 840,
      "cache_read_input_tokens": 18580,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 840,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 261,
          "cache_read_input_tokens": 18580,
          "cache_creation_input_tokens": 840,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 840
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

_source line 15 · 2026-05-30T07:48:04.479Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RTjTNxonxMMmEkjbrmWNxh`</summary>

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
  "parentUuid": "f3a4fb0b-eeb2-408b-8db6-d1fd85b9e858",
  "isSidechain": false,
  "requestId": "req_011CbYPGC2cRacrTgozgpmPf",
  "type": "assistant",
  "uuid": "05b06bf0-3185-448b-ac66-427765de3618",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lqy8nK2qYw6Sj92ABRaaqF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 840,
      "cache_read_input_tokens": 18580,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 840,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 261,
          "cache_read_input_tokens": 18580,
          "cache_creation_input_tokens": 840,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 840
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

_source line 16 · 2026-05-30T07:48:05.610Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015SMu4rrFSF7gHUy8jbT6rL`</summary>

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
  "parentUuid": "05b06bf0-3185-448b-ac66-427765de3618",
  "isSidechain": false,
  "requestId": "req_011CbYPGC2cRacrTgozgpmPf",
  "type": "assistant",
  "uuid": "646b443b-b6cd-4214-a0f4-5ac52c94e7b7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lqy8nK2qYw6Sj92ABRaaqF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 840,
      "cache_read_input_tokens": 18580,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 840,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 261,
          "cache_read_input_tokens": 18580,
          "cache_creation_input_tokens": 840,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 840
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

_source line 17 · 2026-05-30T07:48:05.968Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0197uYB7bEqFGQ8i7nmmjCuZ`</summary>

```json
{
  "query": "poisoning robust conformal prediction RPS ICLR 2025 distribution shift"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "646b443b-b6cd-4214-a0f4-5ac52c94e7b7",
  "isSidechain": false,
  "requestId": "req_011CbYPGC2cRacrTgozgpmPf",
  "type": "assistant",
  "uuid": "a31d102d-3268-40fa-ac8a-d9daf0649302",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lqy8nK2qYw6Sj92ABRaaqF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 840,
      "cache_read_input_tokens": 18580,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 840,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 261,
          "cache_read_input_tokens": 18580,
          "cache_creation_input_tokens": 840,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 840
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

_source line 18 · 2026-05-30T07:48:10.144Z_

<details><summary>↩ Tool result · `toolu_01RrDh22EjHbHSCvb4UUNqmt`</summary>

```text
Web search results for query: "conformal prediction RAG retrieval augmented generation TRAQ C-RAG 2024 2025"

Links: [{"title":"Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction","url":"https://arxiv.org/html/2511.17908"},{"title":"Towards Trustworthy Retrieval Augmented Generation for ...","url":"https://arxiv.org/pdf/2502.06872"},{"title":"[2307.04642] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction","url":"https://arxiv.org/abs/2307.04642"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal   Prediction","url":"https://arxiv.org/pdf/2307.04642"},{"title":"Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-21300-6_45"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction","url":"https://arxiv.org/html/2307.04642v2"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.210/"},{"title":"C-RAG: Certified Generation Risks for Retrieval-Augmented Language   Models","url":"https://arxiv.org/pdf/2402.03181"},{"title":"C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models","url":"https://arxiv.org/html/2402.03181v5"}]

Based on the search results, here's what I found about conformal prediction applications in RAG systems:

## Key Methods

**TRAQ (Trustworthy Retrieval Augmented Question Answering)**: TRAQ provides the first end-to-end statistical correctness guarantee for RAG, using conformal prediction to construct prediction sets guaranteed to contain the semantically correct response with high probability. TRAQ also leverages Bayesian optimization to minimize the size of the constructed sets.

**C-RAG (Certified Generation Risks for Retrieval-Augmented Language Models)**: C-RAG is the first framework to certify generation risks for RAG models, providing conformal risk analysis and certifying an upper confidence bound of generation risks. RAG achieves a lower conformal generation risk than that of a single LLM when the quality of the retrieval model and transformer is non-trivial.

## Recent Research

Recent studies extend conformal prediction to RAG systems, including Conformal-RAG which improves group-conditional coverage for claim verification, CONFLARE which calibrates similarity cutoffs to control retrieval uncertainty, and TRAQ which provides end-to-end correctness guarantees.

Research also demonstrates context engineering through conformal prediction as a coverage-controlled filtering framework that removes irrelevant content while preserving recall of supporting evidence.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3a4fb0b-eeb2-408b-8db6-d1fd85b9e858",
  "isSidechain": false,
  "promptId": "e65aaf3a-f0d3-47c4-8e26-56b5561aafba",
  "type": "user",
  "uuid": "dd4ee388-6420-4c6b-b544-79f2f471d44b",
  "toolUseResult": {
    "query": "conformal prediction RAG retrieval augmented generation TRAQ C-RAG 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_0118Sb3SqW8zU9cbzGbVRKAc",
        "content": [
          {
            "title": "Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction",
            "url": "https://arxiv.org/html/2511.17908"
          },
          {
            "title": "Towards Trustworthy Retrieval Augmented Generation for ...",
            "url": "https://arxiv.org/pdf/2502.06872"
          },
          {
            "title": "[2307.04642] TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction",
            "url": "https://arxiv.org/abs/2307.04642"
          },
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal   Prediction",
            "url": "https://arxiv.org/pdf/2307.04642"
          },
          {
            "title": "Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-3-032-21300-6_45"
          },
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction",
            "url": "https://arxiv.org/html/2307.04642v2"
          },
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction - ACL Anthology",
            "url": "https://aclanthology.org/2024.naacl-long.210/"
          },
          {
            "title": "C-RAG: Certified Generation Risks for Retrieval-Augmented Language   Models",
            "url": "https://arxiv.org/pdf/2402.03181"
          },
          {
            "title": "C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models",
            "url": "https://arxiv.org/html/2402.03181v5"
          }
        ]
      },
      "Based on the search results, here's what I found about conformal prediction applications in RAG systems:\n\n## Key Methods\n\n**TRAQ (Trustworthy Retrieval Augmented Question Answering)**: TRAQ provides the first end-to-end statistical correctness guarantee for RAG, using conformal prediction to construct prediction sets guaranteed to contain the semantically correct response with high probability. TRAQ also leverages Bayesian optimization to minimize the size of the constructed sets.\n\n**C-RAG (Certified Generation Risks for Retrieval-Augmented Language Models)**: C-RAG is the first framework to certify generation risks for RAG models, providing conformal risk analysis and certifying an upper confidence bound of generation risks. RAG achieves a lower conformal generation risk than that of a single LLM when the quality of the retrieval model and transformer is non-trivial.\n\n## Recent Research\n\nRecent studies extend conformal prediction to RAG systems, including Conformal-RAG which improves group-conditional coverage for claim verification, CONFLARE which calibrates similarity cutoffs to control retrieval uncertainty, and TRAQ which provides end-to-end correctness guarantees.\n\nResearch also demonstrates context engineering through conformal prediction as a coverage-controlled filtering framework that removes irrelevant content while preserving recall of supporting evidence."
    ],
    "durationSeconds": 6.600983069999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f3a4fb0b-eeb2-408b-8db6-d1fd85b9e858",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-30T07:48:11.932Z_

<details><summary>↩ Tool result · `toolu_0197uYB7bEqFGQ8i7nmmjCuZ`</summary>

```text
Web search results for query: "poisoning robust conformal prediction RPS ICLR 2025 distribution shift"

Links: [{"title":"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning | OpenReview","url":"https://openreview.net/forum?id=ofuLWn8DFZ"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4d21a4b33361c40c2142db9511c126-Paper-Conference.pdf"},{"title":"Nine papers accepted at ICLR 2025, one at KAIS 2025 - Data Analytics and Machine Learning","url":"https://www.cs.cit.tum.de/en/daml/all-news/article/nine-papers-accepted-at-iclr-2025/"},{"title":"Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning","url":"https://arxiv.org/pdf/2410.09878"},{"title":"GitHub - yascho/reliable_conformal_prediction: Implementation of the reliable conformal prediction sets introduced in the paper: \"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning\" accepted at ICLR 2025 (Spotlight).","url":"https://github.com/yascho/reliable_conformal_prediction"},{"title":"[2410.09878] Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning","url":"https://arxiv.org/abs/2410.09878"},{"title":"ICLR Poster Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning","url":"https://iclr.cc/virtual/2025/poster/28340"},{"title":"Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/pdf/2502.14105"}]

Based on the search results, I found the paper you're looking for:

## Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning

This is an ICLR 2025 Spotlight paper that proposes the first efficient method for making conformal prediction sets more reliable against data poisoning and label flipping attacks.

**Key Contributions:**

The paper proposes Reliable Prediction Sets (RPS): the first efficient method for constructing conformal prediction sets with provable reliability guarantees under poisoning.

To ensure reliability under training poisoning, the approach introduces smoothed score functions that reliably aggregate predictions of classifiers trained on distinct partitions of the training data. Additionally, by introducing smoothed score functions and majority-voting prediction sets calibrated on distinct data subsets, RPS ensures reliability even under malicious poisoning manipulations.

**Problem Addressed:**

Conformal prediction is not reliable under poisoning attacks where adversaries manipulate both training and calibration data, which can significantly alter prediction sets in practice.

**Authors and Implementation:**

The paper is authored by Yan Scholten and Stephan Günnemann. A reference implementation of the reliable conformal prediction sets (RPS) is available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a31d102d-3268-40fa-ac8a-d9daf0649302",
  "isSidechain": false,
  "promptId": "e65aaf3a-f0d3-47c4-8e26-56b5561aafba",
  "type": "user",
  "uuid": "172ef523-85ee-4f10-9356-592f813c1492",
  "toolUseResult": {
    "query": "poisoning robust conformal prediction RPS ICLR 2025 distribution shift",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JT4sExADBmfaiXpGrK8a1c",
        "content": [
          {
            "title": "Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning | OpenReview",
            "url": "https://openreview.net/forum?id=ofuLWn8DFZ"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4d21a4b33361c40c2142db9511c126-Paper-Conference.pdf"
          },
          {
            "title": "Nine papers accepted at ICLR 2025, one at KAIS 2025 - Data Analytics and Machine Learning",
            "url": "https://www.cs.cit.tum.de/en/daml/all-news/article/nine-papers-accepted-at-iclr-2025/"
          },
          {
            "title": "Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning",
            "url": "https://arxiv.org/pdf/2410.09878"
          },
          {
            "title": "GitHub - yascho/reliable_conformal_prediction: Implementation of the reliable conformal prediction sets introduced in the paper: \"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning\" accepted at ICLR 2025 (Spotlight).",
            "url": "https://github.com/yascho/reliable_conformal_prediction"
          },
          {
            "title": "[2410.09878] Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning",
            "url": "https://arxiv.org/abs/2410.09878"
          },
          {
            "title": "ICLR Poster Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning",
            "url": "https://iclr.cc/virtual/2025/poster/28340"
          },
          {
            "title": "Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/pdf/2502.14105"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n## Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning\n\nThis is an ICLR 2025 Spotlight paper that proposes the first efficient method for making conformal prediction sets more reliable against data poisoning and label flipping attacks.\n\n**Key Contributions:**\n\nThe paper proposes Reliable Prediction Sets (RPS): the first efficient method for constructing conformal prediction sets with provable reliability guarantees under poisoning.\n\nTo ensure reliability under training poisoning, the approach introduces smoothed score functions that reliably aggregate predictions of classifiers trained on distinct partitions of the training data. Additionally, by introducing smoothed score functions and majority-voting prediction sets calibrated on distinct data subsets, RPS ensures reliability even under malicious poisoning manipulations.\n\n**Problem Addressed:**\n\nConformal prediction is not reliable under poisoning attacks where adversaries manipulate both training and calibration data, which can significantly alter prediction sets in practice.\n\n**Authors and Implementation:**\n\nThe paper is authored by Yan Scholten and Stephan Günnemann. A reference implementation of the reliable conformal prediction sets (RPS) is available."
    ],
    "durationSeconds": 5.960680591,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a31d102d-3268-40fa-ac8a-d9daf0649302",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-30T07:48:13.483Z_

<details><summary>↩ Tool result · `toolu_015SMu4rrFSF7gHUy8jbT6rL`</summary>

```text
Web search results for query: "RobustRAG certified defense retrieval corruption SaTML 2026"

Links: [{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://goatstack.ai/topics/certifiably-robust-rag-against-retrieval-corruption-yclugx"},{"title":"IEEE SaTML 2026 · Program","url":"https://satml.org/program/"},{"title":"IEEE SaTML 2026 · Accepted Papers","url":"https://satml.org/accepted-papers/"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/pdf/2405.15556"},{"title":"Certifiably Robust RAG against Retrieval Corruption | Request PDF","url":"https://www.researchgate.net/publication/380895542_Certifiably_Robust_RAG_against_Retrieval_Corruption"},{"title":"[Literature Review] Certifiably Robust RAG against Retrieval Corruption","url":"https://www.themoonlight.io/en/review/certifiably-robust-rag-against-retrieval-corruption"},{"title":"Certifiably Robust RAG against Retrieval Corruption Attacks | OpenReview","url":"https://openreview.net/forum?id=cU6ZdN87p3"},{"title":"[2405.15556] Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/abs/2405.15556"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://openreview.net/pdf?id=qsEeACAJjD"}]

Based on the search results, here's information about RobustRAG and its presentation at SaTML 2026:

## RobustRAG Overview

RobustRAG is the first defense framework with certifiable robustness against retrieval corruption attacks. Retrieval-augmented generation (RAG) is susceptible to retrieval corruption attacks, where malicious passages injected into retrieval results can lead to inaccurate model responses.

## Core Defense Strategy

The key insight of RobustRAG is an isolate-then-aggregate strategy: passages are isolated into disjoint groups, LLM responses are generated based on the concatenated passages from each isolated group, and then these responses are securely aggregated for a robust output. To instantiate RobustRAG, keyword-based and decoding-based algorithms are designed for securely aggregating unstructured text responses.

## Certifiable Robustness

RobustRAG can achieve certifiable robustness: it can formally prove and certify that, for certain queries, RobustRAG can always return accurate responses, even when an adaptive attacker has full knowledge of the defense and can arbitrarily inject a small number of malicious passages.

## Authors and SaTML 2026 Presentation

The paper is authored by Chong Xiang (NVIDIA), Tong Wu, Zexuan Zhong (Princeton University), David Wagner (University of California, Berkeley), Danqi Chen and Prateek Mittal (Princeton University). The work was accepted to the IEEE SaTML 2026 conference program.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "646b443b-b6cd-4214-a0f4-5ac52c94e7b7",
  "isSidechain": false,
  "promptId": "e65aaf3a-f0d3-47c4-8e26-56b5561aafba",
  "type": "user",
  "uuid": "8018460a-52b5-4656-92aa-ac991ca3d4b6",
  "toolUseResult": {
    "query": "RobustRAG certified defense retrieval corruption SaTML 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SmTV5cqPfqLFxwyGU4tN5C",
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
      "Based on the search results, here's information about RobustRAG and its presentation at SaTML 2026:\n\n## RobustRAG Overview\n\nRobustRAG is the first defense framework with certifiable robustness against retrieval corruption attacks. Retrieval-augmented generation (RAG) is susceptible to retrieval corruption attacks, where malicious passages injected into retrieval results can lead to inaccurate model responses.\n\n## Core Defense Strategy\n\nThe key insight of RobustRAG is an isolate-then-aggregate strategy: passages are isolated into disjoint groups, LLM responses are generated based on the concatenated passages from each isolated group, and then these responses are securely aggregated for a robust output. To instantiate RobustRAG, keyword-based and decoding-based algorithms are designed for securely aggregating unstructured text responses.\n\n## Certifiable Robustness\n\nRobustRAG can achieve certifiable robustness: it can formally prove and certify that, for certain queries, RobustRAG can always return accurate responses, even when an adaptive attacker has full knowledge of the defense and can arbitrarily inject a small number of malicious passages.\n\n## Authors and SaTML 2026 Presentation\n\nThe paper is authored by Chong Xiang (NVIDIA), Tong Wu, Zexuan Zhong (Princeton University), David Wagner (University of California, Berkeley), Danqi Chen and Prateek Mittal (Princeton University). The work was accepted to the IEEE SaTML 2026 conference program."
    ],
    "durationSeconds": 7.870823024999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "646b443b-b6cd-4214-a0f4-5ac52c94e7b7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-30T07:48:13.590Z_

<details><summary>↩ Tool result · `toolu_01RTjTNxonxMMmEkjbrmWNxh`</summary>

```text
Web search results for query: "corpus poisoning attack RAG PoisonedRAG CorruptRAG 2025 defense"

Links: [{"title":"RAG Poisoning: Contaminating the AI’s “Source of Truth” | by InstaTunnel | Medium","url":"https://medium.com/@instatunnel/rag-poisoning-contaminating-the-ais-source-of-truth-082dcbdeea7c"},{"title":"RAG Poisoning: How Attackers Corrupt Your AI's Knowledge Base | Amine Raji, PhD","url":"https://aminrj.com/posts/rag-document-poisoning/"},{"title":"RAG Poisoning: Threats and Defenses","url":"https://www.emergentmind.com/topics/retrieval-augmented-generation-rag-poisoning"},{"title":"Practical Poisoning Attacks against Retrieval-Augmented Generation","url":"https://arxiv.org/html/2504.03957v2"},{"title":"Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems","url":"https://arxiv.org/html/2603.18034v1"},{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"GitHub - sleeepeer/PoisonedRAG: [USENIX Security 2025] PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models · GitHub","url":"https://github.com/sleeepeer/PoisonedRAG"},{"title":"Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems","url":"https://arxiv.org/pdf/2603.18034"},{"title":"Addressing Corpus Knowledge Poisoning Attacks on RAG Using Sparse Attention","url":"https://arxiv.org/pdf/2602.04711"}]

Based on the search results, here's what I found about corpus poisoning attacks on RAG systems and defense mechanisms in 2025:

## Key Attack Methods

PoisonedRAG, accepted to USENIX Security 2025, represents the first knowledge database corruption attack specifically designed against RAG systems. For an attack to succeed, injected documents must satisfy two conditions: the poisoned document must score higher cosine similarity to the target query than the legitimate document, and once retrieved, the poisoned content must cause the LLM to produce the attacker's desired answer.

Injecting just five malicious texts into a knowledge database containing millions of documents can achieve a 90% attack success rate, and poisoning merely 0.04% of a corpus can lead to a 98.2% attack success rate and 74.6% system failure.

Recent methodologies, such as CorruptRAG and AuthChain, achieve high attack success with a single adversarial document per query. CorruptRAG is a practical poisoning attack against RAG systems that constrains the attacker to injecting only one poisoned text per query.

## Defense Mechanisms

RAGPart leverages the inherent training dynamics of dense retrievers to mitigate the effect of poisoned points, while RAGMask identifies suspicious tokens based on significant similarity shifts under targeted token masking, and across benchmarks these defenses consistently reduce attack success rates while preserving utility under benign conditions.

A defense method termed Sparse Document Attention RAG (SDAG) enforces block-sparse-attention over retrieved documents, where tokens in a retrieved document attend only to previous tokens in the same document.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05b06bf0-3185-448b-ac66-427765de3618",
  "isSidechain": false,
  "promptId": "e65aaf3a-f0d3-47c4-8e26-56b5561aafba",
  "type": "user",
  "uuid": "153067f2-4c2e-432a-86e7-6fe376a6fea0",
  "toolUseResult": {
    "query": "corpus poisoning attack RAG PoisonedRAG CorruptRAG 2025 defense",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PTtztFXqNDx2TwPDDj8N91",
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
      "Based on the search results, here's what I found about corpus poisoning attacks on RAG systems and defense mechanisms in 2025:\n\n## Key Attack Methods\n\nPoisonedRAG, accepted to USENIX Security 2025, represents the first knowledge database corruption attack specifically designed against RAG systems. For an attack to succeed, injected documents must satisfy two conditions: the poisoned document must score higher cosine similarity to the target query than the legitimate document, and once retrieved, the poisoned content must cause the LLM to produce the attacker's desired answer.\n\nInjecting just five malicious texts into a knowledge database containing millions of documents can achieve a 90% attack success rate, and poisoning merely 0.04% of a corpus can lead to a 98.2% attack success rate and 74.6% system failure.\n\nRecent methodologies, such as CorruptRAG and AuthChain, achieve high attack success with a single adversarial document per query. CorruptRAG is a practical poisoning attack against RAG systems that constrains the attacker to injecting only one poisoned text per query.\n\n## Defense Mechanisms\n\nRAGPart leverages the inherent training dynamics of dense retrievers to mitigate the effect of poisoned points, while RAGMask identifies suspicious tokens based on significant similarity shifts under targeted token masking, and across benchmarks these defenses consistently reduce attack success rates while preserving utility under benign conditions.\n\nA defense method termed Sparse Document Attention RAG (SDAG) enforces block-sparse-attention over retrieved documents, where tokens in a retrieved document attend only to previous tokens in the same document."
    ],
    "durationSeconds": 9.107806211,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "05b06bf0-3185-448b-ac66-427765de3618",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores  ## Core Problem  RAG systems in ad…",
  "leafUuid": "153067f2-4c2e-432a-86e7-6fe376a6fea0",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Poisoning-robust conformal abstention for RAG systems",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f"
}
```

---

### Assistant

_source line 24 · 2026-05-30T07:48:16.309Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the initial search results. Let me now search for more specific papers mentioned in the proposal to verify their existence and relevance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "153067f2-4c2e-432a-86e7-6fe376a6fea0",
  "isSidechain": false,
  "requestId": "req_011CbYPHVLhGh2tUCpRdvr49",
  "type": "assistant",
  "uuid": "9b0364bb-bece-4c5a-b6e6-8e78ccad1bf7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012PoMrHAmQoMpou9nyRBHTe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1634,
      "cache_creation_input_tokens": 1973,
      "cache_read_input_tokens": 19420,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1973,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1634,
          "output_tokens": 247,
          "cache_read_input_tokens": 19420,
          "cache_creation_input_tokens": 1973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1973
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

_source line 25 · 2026-05-30T07:48:17.268Z_

Let me do a few more targeted searches on key papers and concepts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b0364bb-bece-4c5a-b6e6-8e78ccad1bf7",
  "isSidechain": false,
  "requestId": "req_011CbYPHVLhGh2tUCpRdvr49",
  "type": "assistant",
  "uuid": "71c2c147-95d3-4df6-9c3b-63ff1a7fd7ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012PoMrHAmQoMpou9nyRBHTe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1634,
      "cache_creation_input_tokens": 1973,
      "cache_read_input_tokens": 19420,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1973,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1634,
          "output_tokens": 247,
          "cache_read_input_tokens": 19420,
          "cache_creation_input_tokens": 1973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1973
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

_source line 26 · 2026-05-30T07:48:18.226Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019MQu8ek83NwcDMPSENoCF8`</summary>

```json
{
  "query": "ReliabilityRAG graph-theoretic NLI contradiction detection NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71c2c147-95d3-4df6-9c3b-63ff1a7fd7ac",
  "isSidechain": false,
  "requestId": "req_011CbYPHVLhGh2tUCpRdvr49",
  "type": "assistant",
  "uuid": "6bcf7b3c-6eb8-4e54-aa59-a00dcce8ad53",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012PoMrHAmQoMpou9nyRBHTe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1634,
      "cache_creation_input_tokens": 1973,
      "cache_read_input_tokens": 19420,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1973,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1634,
          "output_tokens": 247,
          "cache_read_input_tokens": 19420,
          "cache_creation_input_tokens": 1973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1973
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

_source line 27 · 2026-05-30T07:48:19.234Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KjpdbhR1jF8hZNU65KiUsm`</summary>

```json
{
  "query": "\"conformal prediction\" \"distribution shift\" RAG robustness 2026 arXiv vacuous prediction sets"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6bcf7b3c-6eb8-4e54-aa59-a00dcce8ad53",
  "isSidechain": false,
  "requestId": "req_011CbYPHVLhGh2tUCpRdvr49",
  "type": "assistant",
  "uuid": "d312a0d7-5df8-436a-8da1-646e0bc39d4d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012PoMrHAmQoMpou9nyRBHTe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1634,
      "cache_creation_input_tokens": 1973,
      "cache_read_input_tokens": 19420,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1973,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1634,
          "output_tokens": 247,
          "cache_read_input_tokens": 19420,
          "cache_creation_input_tokens": 1973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1973
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

_source line 28 · 2026-05-30T07:48:19.690Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GqF4SuWsMddsCJxohKc8jx`</summary>

```json
{
  "query": "conformal risk control Angelopoulos ICLR 2024 TV distance distributional shift"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d312a0d7-5df8-436a-8da1-646e0bc39d4d",
  "isSidechain": false,
  "requestId": "req_011CbYPHVLhGh2tUCpRdvr49",
  "type": "assistant",
  "uuid": "02abde49-f4f7-42fc-9064-2a07414e1303",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012PoMrHAmQoMpou9nyRBHTe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1634,
      "cache_creation_input_tokens": 1973,
      "cache_read_input_tokens": 19420,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1973,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1634,
          "output_tokens": 247,
          "cache_read_input_tokens": 19420,
          "cache_creation_input_tokens": 1973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1973
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

_source line 29 · 2026-05-30T07:48:25.516Z_

<details><summary>↩ Tool result · `toolu_01GqF4SuWsMddsCJxohKc8jx`</summary>

```text
Web search results for query: "conformal risk control Angelopoulos ICLR 2024 TV distance distributional shift"

Links: [{"title":"Conformal Risk Control","url":"https://research.google/pubs/conformal-risk-control/"},{"title":"Published as a conference paper at ICLR 2024 CONFORMAL RISK CONTROL","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/f3549ef9b5ff520a7e41ff3cc306ab2b-Paper-Conference.pdf"},{"title":"Conformal Risk Control","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/f3549ef9b5ff520a7e41ff3cc306ab2b-Abstract-Conference.html"},{"title":"Published as a conference paper at ICLR 2024 CONFORMAL LANGUAGE MODELING","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/31421b112e5f7faf4fc577b74e45dab2-Paper-Conference.pdf"},{"title":"Publications - Anastasios Angelopoulos","url":"https://people.eecs.berkeley.edu/~angelopoulos/publications/"},{"title":"[2208.02814] Conformal Risk Control","url":"https://arxiv.org/abs/2208.02814"},{"title":"Conformal Risk Control","url":"https://people.eecs.berkeley.edu/~angelopoulos/publications/downloads/conformal-risk.pdf"},{"title":"arXiv:2208.02814v4 [stat.ME] 13 Jun 2025 Conformal Risk Control","url":"https://arxiv.org/pdf/2208.02814"}]

Based on the search results, I found information about the Conformal Risk Control paper by Angelopoulos and colleagues at ICLR 2024.

The paper extends conformal prediction to control the expected value of any monotone loss function, authored by Anastasios N. Angelopoulos, Stephen Bates, Adam Fisch, Lihua Lei, and Tal Schuster, and published at ICLR 2024. The algorithm generalizes split conformal prediction together with its coverage guarantee, and like conformal prediction, the conformal risk control procedure is tight up to an O(1/n) factor.

Worked examples from computer vision and natural language processing demonstrate the usage of their algorithm to bound the false negative rate, graph distance, and token-level F1-score. Additionally, the paper includes extensions of the idea to distribution shift, quantile risk control, multiple and adversarial risk control, and expectations of U-statistics.

However, the search results don't contain specific details about TV distance or distributional shift bounds in the paper. If you're looking for more technical details about the distributional shift guarantees or TV distance-based bounds, you may want to consult the full paper directly, which is available at the ICLR proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02abde49-f4f7-42fc-9064-2a07414e1303",
  "isSidechain": false,
  "promptId": "e65aaf3a-f0d3-47c4-8e26-56b5561aafba",
  "type": "user",
  "uuid": "ae36b32d-bfd1-4440-8245-822fc3cdaeb1",
  "toolUseResult": {
    "query": "conformal risk control Angelopoulos ICLR 2024 TV distance distributional shift",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UUN6HkfPEU9DT9aTDhtNmm",
        "content": [
          {
            "title": "Conformal Risk Control",
            "url": "https://research.google/pubs/conformal-risk-control/"
          },
          {
            "title": "Published as a conference paper at ICLR 2024 CONFORMAL RISK CONTROL",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2024/file/f3549ef9b5ff520a7e41ff3cc306ab2b-Paper-Conference.pdf"
          },
          {
            "title": "Conformal Risk Control",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2024/hash/f3549ef9b5ff520a7e41ff3cc306ab2b-Abstract-Conference.html"
          },
          {
            "title": "Published as a conference paper at ICLR 2024 CONFORMAL LANGUAGE MODELING",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2024/file/31421b112e5f7faf4fc577b74e45dab2-Paper-Conference.pdf"
          },
          {
            "title": "Publications - Anastasios Angelopoulos",
            "url": "https://people.eecs.berkeley.edu/~angelopoulos/publications/"
          },
          {
            "title": "[2208.02814] Conformal Risk Control",
            "url": "https://arxiv.org/abs/2208.02814"
          },
          {
            "title": "Conformal Risk Control",
            "url": "https://people.eecs.berkeley.edu/~angelopoulos/publications/downloads/conformal-risk.pdf"
          },
          {
            "title": "arXiv:2208.02814v4 [stat.ME] 13 Jun 2025 Conformal Risk Control",
            "url": "https://arxiv.org/pdf/2208.02814"
          }
        ]
      },
      "Based on the search results, I found information about the Conformal Risk Control paper by Angelopoulos and colleagues at ICLR 2024.\n\nThe paper extends conformal prediction to control the expected value of any monotone loss function, authored by Anastasios N. Angelopoulos, Stephen Bates, Adam Fisch, Lihua Lei, and Tal Schuster, and published at ICLR 2024. The algorithm generalizes split conformal prediction together with its coverage guarantee, and like conformal prediction, the conformal risk control procedure is tight up to an O(1/n) factor.\n\nWorked examples from computer vision and natural language processing demonstrate the usage of their algorithm to bound the false negative rate, graph distance, and token-level F1-score. Additionally, the paper includes extensions of the idea to distribution shift, quantile risk control, multiple and adversarial risk control, and expectations of U-statistics.\n\nHowever, the search results don't contain specific details about TV distance or distributional shift bounds in the paper. If you're looking for more technical details about the distributional shift guarantees or TV distance-based bounds, you may want to consult the full paper directly, which is available at the ICLR proceedings."
    ],
    "durationSeconds": 5.821208674000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "02abde49-f4f7-42fc-9064-2a07414e1303",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-30T07:48:26.046Z_

<details><summary>↩ Tool result · `toolu_01KjpdbhR1jF8hZNU65KiUsm`</summary>

```text
Web search results for query: ""conformal prediction" "distribution shift" RAG robustness 2026 arXiv vacuous prediction sets"

Links: [{"title":"[2601.02998] Multi-Distribution Robust Conformal Prediction","url":"https://arxiv.org/abs/2601.02998"},{"title":"Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/pdf/2502.14105"},{"title":"[2502.14105] Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/abs/2502.14105"},{"title":"Robust Conformal Prediction under Distribution Shift via   Physics-Informed Structural Causal Model","url":"https://arxiv.org/pdf/2403.15025"},{"title":"[2403.15025] Robust Conformal Prediction under Distribution Shift via Physics-Informed Structural Causal Model","url":"https://arxiv.org/abs/2403.15025"}]

Based on the web search results, I found several relevant papers on arXiv about conformal prediction and distribution shifts from 2026:

## Key Results:

**Multi-Distribution Robust Conformal Prediction (January 2026)**

A max-p aggregation scheme that delivers finite-sample, multi-distribution coverage given any conformity scores associated with each distribution has been proposed. The method delivers valid worst-case coverage across multiple distributions while greatly reducing the set size compared with naively applying max-p aggregation to single-source conformity scores.

**Conformal Prediction under Lévy-Prokhorov Distribution Shifts (May 2025)**

Another recent paper addresses robustness concerns. It models distribution shifts using Lévy-Prokhorov (LP) ambiguity sets, which capture both local and global perturbations. By propagating the LP ambiguity set through the scoring function, complex high-dimensional distribution shifts are reduced to manageable one-dimensional distribution shifts, enabling exact quantification of worst-case quantiles and coverage.

However, the search results did not specifically return papers addressing vacuous prediction sets or RAG (Retrieval-Augmented Generation) robustness in this context. The results focus more broadly on conformal prediction's robustness to distribution shifts through various theoretical frameworks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d312a0d7-5df8-436a-8da1-646e0bc39d4d",
  "isSidechain": false,
  "promptId": "e65aaf3a-f0d3-47c4-8e26-56b5561aafba",
  "type": "user",
  "uuid": "c5889755-cb6d-42aa-81da-4b42fbcd7a75",
  "toolUseResult": {
    "query": "\"conformal prediction\" \"distribution shift\" RAG robustness 2026 arXiv vacuous prediction sets",
    "results": [
      {
        "tool_use_id": "srvtoolu_014uoLhHaxceT5hVfnzFQNwt",
        "content": [
          {
            "title": "[2601.02998] Multi-Distribution Robust Conformal Prediction",
            "url": "https://arxiv.org/abs/2601.02998"
          },
          {
            "title": "Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/pdf/2502.14105"
          },
          {
            "title": "[2502.14105] Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/abs/2502.14105"
          },
          {
            "title": "Robust Conformal Prediction under Distribution Shift via   Physics-Informed Structural Causal Model",
            "url": "https://arxiv.org/pdf/2403.15025"
          },
          {
            "title": "[2403.15025] Robust Conformal Prediction under Distribution Shift via Physics-Informed Structural Causal Model",
            "url": "https://arxiv.org/abs/2403.15025"
          }
        ]
      },
      "Based on the web search results, I found several relevant papers on arXiv about conformal prediction and distribution shifts from 2026:\n\n## Key Results:\n\n**Multi-Distribution Robust Conformal Prediction (January 2026)**\n\nA max-p aggregation scheme that delivers finite-sample, multi-distribution coverage given any conformity scores associated with each distribution has been proposed. The method delivers valid worst-case coverage across multiple distributions while greatly reducing the set size compared with naively applying max-p aggregation to single-source conformity scores.\n\n**Conformal Prediction under Lévy-Prokhorov Distribution Shifts (May 2025)**\n\nAnother recent paper addresses robustness concerns. It models distribution shifts using Lévy-Prokhorov (LP) ambiguity sets, which capture both local and global perturbations. By propagating the LP ambiguity set through the scoring function, complex high-dimensional distribution shifts are reduced to manageable one-dimensional distribution shifts, enabling exact quantification of worst-case quantiles and coverage.\n\nHowever, the search results did not specifically return papers addressing vacuous prediction sets or RAG (Retrieval-Augmented Generation) robustness in this context. The results focus more broadly on conformal prediction's robustness to distribution shifts through various theoretical frameworks."
    ],
    "durationSeconds": 6.806618983,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d312a0d7-5df8-436a-8da1-646e0bc39d4d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-30T07:48:27.589Z_

<details><summary>↩ Tool result · `toolu_019MQu8ek83NwcDMPSENoCF8`</summary>

```text
Web search results for query: "ReliabilityRAG graph-theoretic NLI contradiction detection NeurIPS 2025"

Links: [{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/pdf/2509.23519"},{"title":"NeurIPS Poster ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/119236"},{"title":"Contradiction Detection Guide 2025 - Practical Steps & Best | ShadeCoder","url":"https://www.shadecoder.com/topics/contradiction-detection-a-comprehensive-guide-for-2025"},{"title":"Contradiction Detection in RAG Systems: Evaluating LLMs as Context   Validators for Improved Information Consistency","url":"https://arxiv.org/pdf/2504.00180"},{"title":"Using contradictions improves question answering systems","url":"https://arxiv.org/pdf/2211.05598"},{"title":"With a Little Push, NLI Models can Robustly and Efficiently Predict   Faithfulness","url":"https://arxiv.org/pdf/2305.16819"}]

Based on the search results, I found information about ReliabilityRAG presented at NeurIPS 2025:

ReliabilityRAG is a framework for adversarial robustness that explicitly leverages reliability information of retrieved documents. The framework adopts a graph-theoretic perspective to identify a "consistent majority" among retrieved documents to filter out malicious ones, using a novel algorithm based on finding a Maximum Independent Set (MIS) on a document graph where edges encode contradiction.

The approach aims to identify the largest possible subset of mutually consistent documents, where documents are considered contradictory by a Natural Language Inference (NLI) model. When multiple such sets exist, the method prioritizes the set containing higher-ranked (i.e., more reliable) documents.

The work was presented as a poster at NeurIPS 2025 and addresses vulnerabilities in RAG-based systems, particularly those used in web search applications like Google's Search AI Overview.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6bcf7b3c-6eb8-4e54-aa59-a00dcce8ad53",
  "isSidechain": false,
  "promptId": "e65aaf3a-f0d3-47c4-8e26-56b5561aafba",
  "type": "user",
  "uuid": "5f3868f9-8d83-4767-8efc-4b9cb75dea7d",
  "toolUseResult": {
    "query": "ReliabilityRAG graph-theoretic NLI contradiction detection NeurIPS 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VdWKhW2M2Diaf2o2Waxho8",
        "content": [
          {
            "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://arxiv.org/pdf/2509.23519"
          },
          {
            "title": "NeurIPS Poster ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://neurips.cc/virtual/2025/loc/san-diego/poster/119236"
          },
          {
            "title": "Contradiction Detection Guide 2025 - Practical Steps & Best | ShadeCoder",
            "url": "https://www.shadecoder.com/topics/contradiction-detection-a-comprehensive-guide-for-2025"
          },
          {
            "title": "Contradiction Detection in RAG Systems: Evaluating LLMs as Context   Validators for Improved Information Consistency",
            "url": "https://arxiv.org/pdf/2504.00180"
          },
          {
            "title": "Using contradictions improves question answering systems",
            "url": "https://arxiv.org/pdf/2211.05598"
          },
          {
            "title": "With a Little Push, NLI Models can Robustly and Efficiently Predict   Faithfulness",
            "url": "https://arxiv.org/pdf/2305.16819"
          }
        ]
      },
      "Based on the search results, I found information about ReliabilityRAG presented at NeurIPS 2025:\n\nReliabilityRAG is a framework for adversarial robustness that explicitly leverages reliability information of retrieved documents. The framework adopts a graph-theoretic perspective to identify a \"consistent majority\" among retrieved documents to filter out malicious ones, using a novel algorithm based on finding a Maximum Independent Set (MIS) on a document graph where edges encode contradiction.\n\nThe approach aims to identify the largest possible subset of mutually consistent documents, where documents are considered contradictory by a Natural Language Inference (NLI) model. When multiple such sets exist, the method prioritizes the set containing higher-ranked (i.e., more reliable) documents.\n\nThe work was presented as a poster at NeurIPS 2025 and addresses vulnerabilities in RAG-based systems, particularly those used in web search applications like Google's Search AI Overview."
    ],
    "durationSeconds": 9.359974760000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6bcf7b3c-6eb8-4e54-aa59-a00dcce8ad53",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-30T07:48:27.594Z_

```json
{
  "parentUuid": "5f3868f9-8d83-4767-8efc-4b9cb75dea7d",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "2762eec1-0c31-4a52-9837-4bd86ea4754e",
  "timestamp": "2026-05-30T07:48:27.594Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 33 · 2026-05-30T07:48:32.294Z_

<details><summary>Logged reasoning block</summary>

```text
Let me search for a few more specific items to complete my picture of the research landscape, particularly around the Chen et al. 2026 paper about CP robustness for RAG, and the "Consensus Trap" paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2762eec1-0c31-4a52-9837-4bd86ea4754e",
  "isSidechain": false,
  "requestId": "req_011CbYPJXDLJ4kKSDpcfYeKq",
  "type": "assistant",
  "uuid": "c8ce78f0-8eeb-4740-8ce3-7b3f9c01eb8b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KW8qPRKGKfyNFEfKdcLTrX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1366,
      "cache_creation_input_tokens": 2551,
      "cache_read_input_tokens": 21393,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2551,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1366,
          "output_tokens": 206,
          "cache_read_input_tokens": 21393,
          "cache_creation_input_tokens": 2551,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2551
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

_source line 34 · 2026-05-30T07:48:32.801Z_

Let me search for a few more specific papers to complete my understanding.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8ce78f0-8eeb-4740-8ce3-7b3f9c01eb8b",
  "isSidechain": false,
  "requestId": "req_011CbYPJXDLJ4kKSDpcfYeKq",
  "type": "assistant",
  "uuid": "2096c093-244b-4b8a-9218-2a7b19621868",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KW8qPRKGKfyNFEfKdcLTrX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1366,
      "cache_creation_input_tokens": 2551,
      "cache_read_input_tokens": 21393,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2551,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1366,
          "output_tokens": 206,
          "cache_read_input_tokens": 21393,
          "cache_creation_input_tokens": 2551,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2551
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

_source line 35 · 2026-05-30T07:48:33.803Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019txiFPBqAcMEoEnRmcxexq`</summary>

```json
{
  "query": "arXiv 2603.16817 conformal factuality RAG robust 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2096c093-244b-4b8a-9218-2a7b19621868",
  "isSidechain": false,
  "requestId": "req_011CbYPJXDLJ4kKSDpcfYeKq",
  "type": "assistant",
  "uuid": "c82f5597-027c-48f7-b078-45cbfbc10574",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KW8qPRKGKfyNFEfKdcLTrX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1366,
      "cache_creation_input_tokens": 2551,
      "cache_read_input_tokens": 21393,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2551,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1366,
          "output_tokens": 206,
          "cache_read_input_tokens": 21393,
          "cache_creation_input_tokens": 2551,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2551
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

_source line 36 · 2026-05-30T07:48:34.467Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LQByvo2fzJjjVzABx9UyRV`</summary>

```json
{
  "query": "\"consensus trap\" arXiv 2604.17139 majority voting corrupted agents 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c82f5597-027c-48f7-b078-45cbfbc10574",
  "isSidechain": false,
  "requestId": "req_011CbYPJXDLJ4kKSDpcfYeKq",
  "type": "assistant",
  "uuid": "49731e71-041d-4556-862c-51e0b0e127ce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KW8qPRKGKfyNFEfKdcLTrX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1366,
      "cache_creation_input_tokens": 2551,
      "cache_read_input_tokens": 21393,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2551,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1366,
          "output_tokens": 206,
          "cache_read_input_tokens": 21393,
          "cache_creation_input_tokens": 2551,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2551
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

_source line 37 · 2026-05-30T07:48:40.582Z_

<details><summary>↩ Tool result · `toolu_019txiFPBqAcMEoEnRmcxexq`</summary>

```text
Web search results for query: "arXiv 2603.16817 conformal factuality RAG robust 2026"

Links: [{"title":"[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/abs/2603.16817"},{"title":"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/pdf/2603.16817"},{"title":"Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/html/2506.20978v1"},{"title":"[2506.20978v1] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/abs/2506.20978v1"},{"title":"[2506.20978] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/abs/2506.20978"}]

I found the arXiv paper you were looking for. Here are the key details about arXiv 2603.16817:

**Title:** "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights"

**Authors and Affiliation:** The paper is from University of Wisconsin-Madison, authored by Yi Chen, Daiwei Chen, Sukrut Madhay Chikodikar, Caitlyn Heqi Yin, and Ramya Korlakai Vinayak, posted on March 17, 2026

**Main Findings:** The study found that conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, conformal factuality guarantee is not robust to distribution shifts and distractors, and lightweight entailment-based verifiers match or outperform LLM-based model confidence scorers while requiring over 100× fewer FLOPs

**Core Contributions:** The researchers systematically analyze the reliability and usefulness of conformal factuality for RAG-based LLMs and propose novel informativeness-aware metrics that better reflect task utility under conformal filtering

The paper addresses important limitations in using conformal prediction to ensure factuality in retrieval-augmented generation systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c82f5597-027c-48f7-b078-45cbfbc10574",
  "isSidechain": false,
  "promptId": "e65aaf3a-f0d3-47c4-8e26-56b5561aafba",
  "type": "user",
  "uuid": "eb0b60ea-bcce-4470-bd57-2f9d46c66f27",
  "toolUseResult": {
    "query": "arXiv 2603.16817 conformal factuality RAG robust 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MYH3CDfubr7Qent1P6BjZk",
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
            "title": "Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality",
            "url": "https://arxiv.org/html/2506.20978v1"
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
      "I found the arXiv paper you were looking for. Here are the key details about arXiv 2603.16817:\n\n**Title:** \"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights\"\n\n**Authors and Affiliation:** The paper is from University of Wisconsin-Madison, authored by Yi Chen, Daiwei Chen, Sukrut Madhay Chikodikar, Caitlyn Heqi Yin, and Ramya Korlakai Vinayak, posted on March 17, 2026\n\n**Main Findings:** The study found that conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, conformal factuality guarantee is not robust to distribution shifts and distractors, and lightweight entailment-based verifiers match or outperform LLM-based model confidence scorers while requiring over 100× fewer FLOPs\n\n**Core Contributions:** The researchers systematically analyze the reliability and usefulness of conformal factuality for RAG-based LLMs and propose novel informativeness-aware metrics that better reflect task utility under conformal filtering\n\nThe paper addresses important limitations in using conformal prediction to ensure factuality in retrieval-augmented generation systems."
    ],
    "durationSeconds": 6.753322955999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c82f5597-027c-48f7-b078-45cbfbc10574",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
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
  "leafUuid": "eb0b60ea-bcce-4470-bd57-2f9d46c66f27",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Poisoning-robust conformal abstention for RAG systems",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f"
}
```

---

### Tool result

_source line 40 · 2026-05-30T07:48:41.570Z_

<details><summary>↩ Tool result · `toolu_01LQByvo2fzJjjVzABx9UyRV`</summary>

```text
Web search results for query: ""consensus trap" arXiv 2604.17139 majority voting corrupted agents 2026"

Links: [{"title":"[2604.17139] The Consensus Trap: Rescuing Multi-Agent LLMs from Adversarial Majorities via Token-Level Collaboration","url":"https://arxiv.org/abs/2604.17139"},{"title":"The Consensus Trap: Rescuing Multi-Agent LLMs from Adversarial Majorities via Token-Level Collaboration","url":"https://arxiv.org/html/2604.17139"},{"title":"Voter and Majority Dynamics with Biased and Stubborn Agents","url":"https://arxiv.org/pdf/2003.02885"},{"title":"Resilient Consensus Against Mobile Malicious Agents","url":"https://arxiv.org/pdf/2006.11711"},{"title":"Multi-Agent Trustworthy Consensus under Random Dynamic Attacks","url":"https://arxiv.org/pdf/2504.07189"},{"title":"Beyond Consensus: Trace-Level Synthesis in Mixture of Agents","url":"https://arxiv.org/html/2605.29116"},{"title":"Multi-Agent Resilient Consensus under Intermittent Faulty and Malicious   Transmissions (Extended Version)","url":"https://arxiv.org/pdf/2403.17907"}]

Based on the search results, here's what I found about the paper referenced by arXiv 2604.17139:

The paper reveals a critical structural vulnerability in current multi-agent systems: response-level aggregation collapses when corrupted agents form a local majority. Multi-agent large language model (LLM) architectures increasingly rely on response-level aggregation, such as Majority Voting (MAJ), to raise reasoning ceilings.

In open environments, agents are highly susceptible to stealthy contextual corruption, such as targeted prompt injections. Because voting aggregates fully-formed conclusions, it is blind to flawed intermediate logic.

To address this vulnerability, the paper proposes Token-Level Round-Robin (RR) Collaboration, where agents sequentially interleave generation within a shared auto-regressive context. This process is formalized as a discrete-time dynamical system, proving that token-level interleaving transitions aggregation from a brittle counting of final votes (a linear sum) to a dynamic, interwoven chain of logic (a non-linear operator product).

Through empirical evaluation across diverse reasoning benchmarks, the results demonstrate that while MAJ collapses when corrupted agents reach a majority, RR maintains robust accuracy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49731e71-041d-4556-862c-51e0b0e127ce",
  "isSidechain": false,
  "promptId": "e65aaf3a-f0d3-47c4-8e26-56b5561aafba",
  "type": "user",
  "uuid": "ca4daef7-4f0d-43a3-a863-232b0645a34f",
  "toolUseResult": {
    "query": "\"consensus trap\" arXiv 2604.17139 majority voting corrupted agents 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PbT9ycDosFvB3EX2YJLXKj",
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
            "title": "Voter and Majority Dynamics with Biased and Stubborn Agents",
            "url": "https://arxiv.org/pdf/2003.02885"
          },
          {
            "title": "Resilient Consensus Against Mobile Malicious Agents",
            "url": "https://arxiv.org/pdf/2006.11711"
          },
          {
            "title": "Multi-Agent Trustworthy Consensus under Random Dynamic Attacks",
            "url": "https://arxiv.org/pdf/2504.07189"
          },
          {
            "title": "Beyond Consensus: Trace-Level Synthesis in Mixture of Agents",
            "url": "https://arxiv.org/html/2605.29116"
          },
          {
            "title": "Multi-Agent Resilient Consensus under Intermittent Faulty and Malicious   Transmissions (Extended Version)",
            "url": "https://arxiv.org/pdf/2403.17907"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper referenced by arXiv 2604.17139:\n\nThe paper reveals a critical structural vulnerability in current multi-agent systems: response-level aggregation collapses when corrupted agents form a local majority. Multi-agent large language model (LLM) architectures increasingly rely on response-level aggregation, such as Majority Voting (MAJ), to raise reasoning ceilings.\n\nIn open environments, agents are highly susceptible to stealthy contextual corruption, such as targeted prompt injections. Because voting aggregates fully-formed conclusions, it is blind to flawed intermediate logic.\n\nTo address this vulnerability, the paper proposes Token-Level Round-Robin (RR) Collaboration, where agents sequentially interleave generation within a shared auto-regressive context. This process is formalized as a discrete-time dynamical system, proving that token-level interleaving transitions aggregation from a brittle counting of final votes (a linear sum) to a dynamic, interwoven chain of logic (a non-linear operator product).\n\nThrough empirical evaluation across diverse reasoning benchmarks, the results demonstrate that while MAJ collapses when corrupted agents reach a majority, RR maintains robust accuracy."
    ],
    "durationSeconds": 7.100227458000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "49731e71-041d-4556-862c-51e0b0e127ce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-30T07:49:33.514Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture of the research landscape. Let me compile my evaluation.

Let me summarize what I've found:

1. **TRAQ (NAACL 2024)** - First conformal prediction for RAG, providing end-to-end correctness guarantees. ✓ Confirmed.

2. **C-RAG (ICML 2024)** - Certified generation risks for RAG models. ✓ Confirmed.

3. **RobustRAG (SaTML 2026)** - Isolate-then-aggregate for certified robustness against retrieval corruption. 

4. **RPS (ICLR 2025 Spotlight)** - Poisoning-robust conformal prediction via smoothed scores and majority voting, though it addresses calibration-set poisoning rather than test-time retrieval corruption. ✓ Confirmed.

5. **ReliabilityRAG (NeurIPS 2025)** - Graph-theoretic MIS with NLI-based contradiction detection. ✓ Confirmed.

6. **Chen et al. (arXiv:2603.16817, Mar 2026)** - Demonstrates that conformal factuality for RAG lacks robustness to distribution shifts. ✓ Confirmed.

7. **PoisonedRAG** - Still reviewing... USENIX Security 2025)** - 90%+ ASR with 5 documents. ✓ Confirmed.

8. **CorruptRAG** - Single-document high-ASR. ✓ Confirmed.

9. **RAGPart** - Document partitioning at retrieval stage. ✓ Confirmed.

10. **Consensus Trap (arXiv:2604.17139, Apr 2026)** - Majority voting fails under corrupted agent majority. ✓ Confirmed.

11. **LP-shift framework (arXiv:2502.14105)** - Reduces high-dimensional shifts to 1D. ✓ Confirmed.

12. **CRC (ICLR 2024)** - Conformal Risk Control. ✓ Confirmed.

Now evaluating the proposal itself. The strengths are compelling: there's a genuine gap where no existing work combines conformal abstention with retrieval-poisoning robustness, the theoretical framing elegantly reduces adversarial corruption to bounded TV shift through partitioning, and the literature review shows deep field awareness across 17+ papers. The experimental plan is thorough with 8 baselines, 4 datasets, 3 model scales, and comprehensive ablations including adaptive attacks. The proposal also clearly articulates why three alternative approaches fail and grounds the work in practical applications like medical QA and legal retrieval.

But there's a significant concern emerging: PRCA's partition-and-generate step looks nearly identical to RobustRAG's approach. isolate-then-aggregate. The key difference is in the aggregation/scoring step—PRCA uses agreement scores for abstention rather than RobustRAG's keyword/decoding-based aggregation for answer generation. This needs to be very clearly distinguished.

2. **Theoretical tightness**: The TV bound of m/K is acknowledged as potentially loose. The proposal mentions empirical estimation and "exploring concentration-based bounds" as future work, but the theoretical contribution would be stronger with tighter bounds.

3. **NLI reliability under adversarial conditions**: The proposal acknowledges this concern (citing Semantic Illusion) and includes a diagnostic experiment, which is good. But if NLI is unreliable under adversarial conditions, the entire method's practical value is undermined.

4. **Clean-condition variance**: For complex questions like HotpotQA, different passage groups may cover different facets, resulting in low clean-condition agreement and high false abstention rates. The proposal addresses this through NLI-based semantic entailment and calibration, but this remains a potential practical bottleneck.

5. **Adaptive attack**: The agreement-aware adaptive attack is well-conceived but technically challenging—the attacker must craft passages producing consistent wrong answers across groups, which is conceptually sound but difficult to execute and may not fully stress-test the method.

6. **Computational cost**: With K separate LLM calls plus K(K-1)/2 NLI calls, the overhead is substantial. For K=5, that's 5 LLM and 10 NLI calls per query, making this significantly more expensive than standard RAG.

7. **The TV inflation approach**: Using CRC with TV-

inflated quantiles is straightforward once you have the TV bound, but the coverage guarantee is only as good as the bound itself—a loose bound leads to overly conservative predictions.

8. **Incremental novelty**: Reviewers might see this as combining RobustRAG's partitioning, CRC's TV inflation, and NLI scoring rather than a fundamentally new contribution. The partition-induced TV reduction is the core novelty and needs to be framed as a clean, general theorem.

The proposal tackles a genuine gap between conformal prediction and adversarial robustness for RAG, with a timely research question and comprehensive experimental design. But the novelty could be perceived as incremental—assembling existing techniques rather than introducing fundamentally new ideas—and several practical limitations (NLI reliability, clean-condition variance, computational cost) could limit real-world applicability.

What stands out is the thoroughness: the proposal preemptively addresses nearly every potential reviewer concern, from alternative approaches to adaptive attacks to computational overhead. That comprehensiveness itself is a meaningful strength. The method is sound, the theory is clean though potentially loose, and the experiments are well-designed, so I'd estimate this has a moderate-to-good chance of acceptance, with the main risks being perceived incremental novelty and whether the theoretical bounds prove tight enough in practice. The strengths are solid—the gap is clear, the theoretical insight is elegant, the experiments are comprehensive, and the motivation around adversarial RAG safety is compelling. But the weaknesses matter: the core technique combines existing components, the theoretical bound is a straightforward combinatorial result rather than something novel, NLI reliability under adversarial conditions is a real concern, and the computational overhead is significant. Weighing these factors, I'm settling on 30-42% with a median around 35-37%—it's a competent proposal with a genuine contribution, but the novelty question is the main risk factor.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca4daef7-4f0d-43a3-a863-232b0645a34f",
  "isSidechain": false,
  "requestId": "req_011CbYPKYxHQzzXXfZDELQFm",
  "type": "assistant",
  "uuid": "64f139c7-6b9f-4741-b948-931089015560",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FzuGdqADtADhVuHsDKGRRr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2845,
      "cache_read_input_tokens": 23944,
      "output_tokens": 7818,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2845,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7818,
          "cache_read_input_tokens": 23944,
          "cache_creation_input_tokens": 2845,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2845
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

_source line 42 · 2026-05-30T07:51:39.221Z_

Now I have a comprehensive picture of the research landscape. Let me compile my full evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [TRAQ](https://arxiv.org/abs/2307.04642) (NAACL 2024): 首个将 conformal prediction 应用于 RAG 的工作，提供端到端的语义正确性保证。本 proposal 的直接前驱之一；PRCA 的 baseline。
- [C-RAG](https://arxiv.org/abs/2402.03181) (ICML 2024): 为 RAG 模型建立 certified generation risk 上界的框架。与 TRAQ 一起构成 conformal-for-RAG 的基础，均假设 benign retrieval。
- [Conformal Risk Control (CRC)](https://arxiv.org/abs/2208.02814) (ICLR 2024): PRCA 的核心理论工具——将 conformal prediction 推广到任意单调损失函数的期望控制，包含 distribution shift 扩展。PRCA 的 TV-inflated quantile 直接依赖此工作。
- [RPS: Provably Reliable Conformal Prediction Sets under Poisoning](https://arxiv.org/abs/2410.09878) (ICLR 2025 Spotlight): 通过 smoothed scores + majority voting 实现 poisoning-robust CP，但假设的是 calibration-set poisoning，不适用于 test-time retrieval corruption。PRCA 正确指出了这一局限。
- [RobustRAG: Certifiably Robust RAG against Retrieval Corruption](https://arxiv.org/abs/2405.15556) (SaTML 2026): **与 PRCA 关系最密切的工作**。采用 isolate-then-aggregate 策略——将 passages 分成 disjoint groups、每组独立生成、安全聚合。PRCA 的 Step 1 (partition-and-generate) 本质上复用了此策略，差异在于 PRCA 用 agreement score + CRC 做 abstention，而非 RobustRAG 的 keyword/decoding-based 聚合做 point estimate。
- [ReliabilityRAG](https://arxiv.org/abs/2509.23519) (NeurIPS 2025): 用 NLI-based contradiction detection 构建文档图、通过 MIS 筛选一致性最大的文档子集。PRCA 借鉴了 NLI entailment 思路，但用于 inter-group agreement scoring 而非 document filtering。
- [Chen et al.: Is Conformal Factuality for RAG-based LLMs Robust?](https://arxiv.org/abs/2603.16817) (arXiv, Mar 2026): 实证表明 TRAQ/C-RAG 等 conformal 方法在 distribution shift 和 distractors 下产生 vacuous outputs，但未提出解决方案。PRCA 直接回应此问题。
- [PoisonedRAG](https://github.com/sleeepeer/PoisonedRAG) (USENIX Security 2025): 注入 5 篇恶意文档即达 90%+ ASR。确认了 corpus poisoning 的实际威胁性。
- [CorruptRAG](https://arxiv.org/abs/2504.03957) (arXiv 2025): 单文档即可达成高 ASR 的实用攻击。
- [RAGPart & RAGMask](https://arxiv.org/abs/2512.24268) (arXiv, Dec 2025): 在 retrieval stage 使用 document partitioning 来稀释毒化影响。与 PRCA 的 partition 在不同阶段（retrieval vs. generation/calibration）且目标不同（filtered retrieval vs. abstention with certificates），proposal 正确定位了互补关系。
- [Conformal Prediction under Lévy-Prokhorov Distribution Shifts](https://arxiv.org/abs/2502.14105) (arXiv, Feb 2025): 将高维 distribution shift 通过 ambiguity sets 归约到一维 score shift。PRCA 的 partition-induced TV reduction 可视为此框架在 adversarial retrieval corruption 下的具体实例化。
- [The Consensus Trap](https://arxiv.org/abs/2604.17139) (arXiv, Apr 2026): 证明 response-level majority voting 在 corrupted agents 形成局部多数时崩溃。PRCA 正确指出其主要保证在 abstention certificate 而非 majority answer correctness，且在 k < n/2 下 honest majority 得以保持。
- [Semantic Chameleon](https://arxiv.org/abs/2603.18034) (arXiv, Mar 2026): gradient-guided corpus-dependent 攻击，能让恶意 passages 看起来很权威。对 PRCA 的 logprob-based 替代方案构成挑战（proposal 已在 "Why not combine" 中分析了这一点）。

- **调研总结**: 该领域当前存在清晰的二分格局——conformal prediction for RAG (TRAQ, C-RAG, Conformal-RAG) 提供统计保证但假设 benign retrieval；certified RAG defenses (RobustRAG, ReliabilityRAG) 提供 adversarial robustness 但仅输出 point estimates 而无 coverage certificates。Chen et al. (Mar 2026) 实证确认了前者在 adversarial 条件下的脆弱性，但未提出解决方案。**PRCA 填补的 gap——将 conformal abstention 与 retrieval-poisoning robustness 结合——经调研确认是真实存在且尚无人解决的**。最接近的竞争者 RobustRAG 的 partition 策略与 PRCA Step 1 高度重叠，但缺少 abstention mechanism 和 coverage certificates，这一差异是实质性的。

【整体印象】:
如果我是审稿人，第一反应是**倾向 weak accept**。这是一篇研究问题定位精准、理论动机清晰、实验设计异常全面的 proposal。Gap 是真实的——conformal prediction for RAG 在 adversarial 条件下的脆弱性已被 Chen et al. (2026) 实证确认，而 certified RAG defenses 缺少 abstention mechanism，两个社区的交叉空白确实无人填补。Partition-induced TV reduction 的理论洞察干净优雅。但我会在两个方面犹豫：(1) 核心方法的组成部分（partitioning from RobustRAG, TV inflation from CRC, NLI scoring from ReliabilityRAG）均为已有技术，novelty 的深度取决于"组合的理论必然性"这一论证能否让审稿人信服；(2) TV ≤ m/K 的理论 bound 是直接的组合论上界，理论贡献本身偏轻量。

【核心贡献】:
PRCA 的核心贡献是一个 **partition-induced reduction**：通过将 retrieved passages 分成 disjoint groups 并计算 inter-group agreement，将高维的 arbitrary adversarial retrieval corruption 确定性地归约为一维 nonconformity score 分布上有界的 TV shift，然后通过 CRC 的 inflated quantile 吸收该 shift 以获得形式化的 coverage certificate。

这一贡献的价值在于：
- **概念清洁**：将 "adversarial robustness" 和 "conformal abstention" 两个独立的问题通过一个统一的理论机制连接起来
- **实用意义**：在 medical QA、legal retrieval 等高风险场景中，"不知道就说不知道"（abstention）比给出可能错误的答案更有价值，coverage certificate 提供了可审计的安全保证
- **理论定位**：可视为 LP-shift framework 在 adversarial RAG 下的具体实例化

但贡献的深度受限于：理论核心（TV bound）是一个直观的组合论论证，而非深层的概率论或信息论结果。

【方法合理性】:
方法在逻辑上是合理且自洽的。Partition → agreement score → TV bound → CRC inflation → coverage certificate 的推导链条每一步都有明确的理论支撑。

**更简单的替代方案分析**：
Proposal 已经系统性地分析了三种自然替代方案的失败模式（RobustRAG + standard CP, full-context self-consistency + CP, logprob-based confidence + CP），论证有说服力。特别是：
- RobustRAG + standard CP 的失败原因（aggregation 破坏 exchangeability、distributional shift 大小未刻画）是实质性的
- Full-context self-consistency 在 poisoning 下的 blindness（所有 K samples 共享同一 poisoned context）是正确的

但需要注意一个潜在的简化替代：**直接用 RobustRAG 的 certified robust accuracy 作为一个 proxy confidence score，然后基于该 score 做简单阈值 abstention**。这不是 conformal prediction，没有 distribution-free 保证，但在实际效果上可能接近。Proposal 的关键卖点是 distribution-free coverage certificate，而非经验性能——这需要在论文中非常清晰地传达。

**方法的一个隐忧**：partition 同时引入了两个效应——(1) 正面：隔离毒化 passages 以检测不一致；(2) 负面：每组只看到 n/K 个 passages，信息量下降，可能降低 clean accuracy 并增大 clean-condition score variance。这种 information-robustness tradeoff 在 ablation 中通过 K 的变化可以观察到，proposal 已规划了这一实验（K ∈ {1,3,5,7,10}），但需要确保分析的深度足够。

【5 维度打分】:

1. **研究问题: 强** — Gap 真实存在且经 Chen et al. (2026) 实证确认。Conformal prediction for RAG 在 adversarial 条件下的脆弱性是一个被明确识别但尚未解决的问题。RAG 在高风险领域的部署使得 adversarial robustness + abstention guarantee 具有实际意义。研究问题的时效性极强——相关论文密集发表于 2024-2026，表明社区高度关注。

2. **方法与创新: 中** — 方法合理、理论链条自洽，partition-induced TV reduction 的理论洞察有价值。但核心组件（partition: RobustRAG; TV inflation: CRC; NLI scoring: ReliabilityRAG）均为已有技术，TV ≤ m/K 的 bound 是直接的组合论上界而非深层理论结果。Novelty 主要体现在 **组合的理论必然性**和 **reduction 的概念框架**上，而非任何单一技术组件。这种 "principled assembly" 类型的 novelty 在 AAAI 是可以被接受的，但需要论证得非常有力。与 LP-shift framework (arXiv:2502.14105) 的类比有助于提升理论定位。Tighter bounds（concentration-based）目前仅作为 "future direction" 提及，若能给出至少一个 non-trivial refinement 将显著增强理论贡献。

3. **实验设计: 强** — 这是 proposal 最突出的优点之一。8 个 baselines 涵盖三个类别（conformal, certified defense, partition-based），包含一个 compute-normalized baseline（TRAQ + K× self-consistency）和一个 naive pipeline baseline（RobustRAG + TRAQ），后者直接验证 "Why not combine?" 的理论论证。Ablation matrix 设计全面（K, n, score function, calibration protocol, partition strategy），K=1 作为 degenerate no-partition baseline 的设计特别好。Diagnostic experiments（NLI reliability, TV bound tightness, k sensitivity）展现了对方法潜在弱点的深刻认识。Adaptive attack 的设计（agreement-aware, 知道 K-partition 结构）是负责任的 robustness evaluation。在 RAG 安全领域，PoisonedRAG/RobustRAG 使用的 NQ/HotpotQA/MS-MARCO 是标准 benchmark，dataset 选择合理。3 个 model scale（7B/32B/72B）验证 model-agnosticism。唯一的轻微不足是 scale 偏小（200-300 queries/setting），但对于 conformal 方法来说是标准的。

4. **可行性: 中** — 方案可执行，但计算成本较高。K=5 时每个 query 需要 5 次 LLM 调用 + 10 次 NLI 调用；在 72B 模型上做 full evaluation 需要相当的 GPU 资源。Proposal 明智地限制了 32B/72B 仅做 core config 验证。NLI reliability 是一个实际风险——如果 DeBERTa NLI 在 adversarial LLM outputs 上表现不佳（Semantic Illusion 已指出 NLI 的局限性），整个方法的实用性会受到质疑，但 proposal 已规划了 diagnostic experiment 和 fallback（ensemble NLI, temperature-scaled NLI）。Calibration 需要 clean corpus（per RPS 的标准假设），这在实际部署中可能不总是可行的。预计实验周期约 6-10 周，对单篇论文来说合理。

5. **写作与呈现: 强** — Proposal 的结构清晰、逻辑严密。问题定义 → gap 识别 → "Why not combine?" 三重论证 → 方法设计 → 实验设计的叙事流畅。对相关工作的定位极为精准——不仅列出论文，还明确指出每篇工作与 PRCA 的具体差异和关系。"Partition is a theoretical necessity, not a design choice" 的论述有力。Ablation 的 degenerate case 设计（K=1）展现了方法论的严谨性。对潜在弱点的坦诚讨论（TV bound tightness, NLI reliability, Consensus Trap 风险）增加了可信度。

【概率估计】: [30% - 42%] 中位 35%

【估计理由】:
- **上推因素**: (1) 研究问题定位精准，gap 真实且时效性强；(2) 实验设计异常全面，远超同级别 proposal 的标准；(3) 对领域的掌握深度和 "Why not combine?" 的系统分析显示了高水平的研究能力；(4) 应用动机明确（高风险领域的 RAG safety），符合 AAAI 对 impact 的重视；(5) 写作和呈现质量高。
- **下拉因素**: (1) 核心 novelty 是已有组件的 principled assembly，理论贡献（TV bound）偏轻量，部分审稿人可能认为 incremental；(2) TV ≤ m/K 的 bound 可能过于保守导致 excessive abstention，实际覆盖率 vs. abstention rate 的 tradeoff 可能不够吸引人；(3) 计算成本高（K 倍 LLM 调用）可能限制实用性；(4) NLI reliability under adversarial conditions 是一个未验证的假设。
- **中位 35% 的定位**: 这是一篇 solid、well-executed 的工作，但不是一篇 "exciting" 的工作。它更像是一篇 craftsmanship 精湛的论文——问题定义准确、方法合理、实验全面——但理论深度有限，且核心 insight 的 novelty 可能无法让所有审稿人信服。在 AAAI ~20-23% 的接受率下，这类论文的命运高度依赖审稿人分配：遇到重视 problem formulation 和 experimental rigor 的审稿人可能拿到 accept，遇到重视 theoretical depth 的审稿人可能被视为 incremental。

【主要风险】:
1. **Novelty 被判定为 incremental**: 审稿人可能认为 PRCA = RobustRAG partition + CRC TV inflation + ReliabilityRAG NLI scoring，各组件均为已知技术，组合虽 principled 但缺乏深层理论创新。TV ≤ m/K 的 bound 过于直观，不构成足够的理论贡献。
2. **NLI reliability 假设在 adversarial 条件下不成立**: 如果 DeBERTa NLI 在对抗性 LLM 输出上的 entailment 判断不可靠（false positives/negatives 率高），整个 agreement score 的基础被动摇，coverage certificate 形式上成立但实际保护价值有限。虽然 proposal 规划了 diagnostic experiment，但这更像是 "发现问题" 而非 "解决问题"。

【实施评估】:
  - 计算资源: **高**。K=5 配置下每 query 需 5 次 LLM 调用 + 10 次 NLI 调用。72B 模型的 full evaluation 需要多卡 GPU（~4×A100/H100）。估计总 GPU 时约 500-1000 小时（含所有 ablation 和 diagnostic experiments）。
  - 数据需求: **低-中**。使用公开 benchmark（NQ, HotpotQA, MS-MARCO, PubMedQA），无需私有数据。需要运行 PoisonedRAG/CorruptRAG 攻击代码生成 poisoned corpora。Calibration set 需要 500+ clean samples per dataset。
  - 人工介入: **低**。主要在 adaptive attack 设计和 NLI diagnostic 分析中需要人工判断。
  - 训练需求: **低**。无需训练新模型——LLM 用现有 checkpoint（Qwen/Llama），NLI 用 DeBERTa-v3-large 现有权重。可能需要 temperature scaling 微调 NLI。
  - 新 Benchmark: **否**。使用现有 benchmark 和攻击方法。
  - 预估周期: **8-12 周**。其中：环境搭建+攻击代码适配 1-2 周；核心方法实现 1-2 周；7B 全量实验 2-3 周；32B/72B 验证 1-2 周；diagnostic experiments 1-2 周；论文撰写 2-3 周。
```

Sources:
- [TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction](https://arxiv.org/abs/2307.04642)
- [C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models](https://arxiv.org/abs/2402.03181)
- [Conformal Risk Control (CRC)](https://arxiv.org/abs/2208.02814)
- [RPS: Provably Reliable Conformal Prediction Sets under Poisoning](https://arxiv.org/abs/2410.09878)
- [RobustRAG: Certifiably Robust RAG against Retrieval Corruption](https://arxiv.org/abs/2405.15556)
- [ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search](https://arxiv.org/abs/2509.23519)
- [Chen et al.: Is Conformal Factuality for RAG-based LLMs Robust?](https://arxiv.org/abs/2603.16817)
- [PoisonedRAG (USENIX Security 2025)](https://github.com/sleeepeer/PoisonedRAG)
- [CorruptRAG: Practical Poisoning Attacks against RAG](https://arxiv.org/abs/2504.03957)
- [RAGPart & RAGMask](https://arxiv.org/abs/2512.24268)
- [Conformal Prediction under Lévy-Prokhorov Distribution Shifts](https://arxiv.org/abs/2502.14105)
- [The Consensus Trap](https://arxiv.org/abs/2604.17139)
- [Semantic Chameleon](https://arxiv.org/abs/2603.18034)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64f139c7-6b9f-4741-b948-931089015560",
  "isSidechain": false,
  "requestId": "req_011CbYPKYxHQzzXXfZDELQFm",
  "type": "assistant",
  "uuid": "71d92a4f-611d-4afb-a0b3-e65f6c39ba5b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FzuGdqADtADhVuHsDKGRRr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2845,
      "cache_read_input_tokens": 23944,
      "output_tokens": 7818,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2845,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7818,
          "cache_read_input_tokens": 23944,
          "cache_creation_input_tokens": 2845,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2845
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

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores  ## Core Problem  RAG systems in ad…",
  "leafUuid": "71d92a4f-611d-4afb-a0b3-e65f6c39ba5b",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Poisoning-robust conformal abstention for RAG systems",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores  ## Core Problem  RAG systems in ad…",
  "leafUuid": "71d92a4f-611d-4afb-a0b3-e65f6c39ba5b",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Poisoning-robust conformal abstention for RAG systems",
  "sessionId": "516d5c90-34b9-4908-b5ab-b6edba91ee8f"
}
```

---
