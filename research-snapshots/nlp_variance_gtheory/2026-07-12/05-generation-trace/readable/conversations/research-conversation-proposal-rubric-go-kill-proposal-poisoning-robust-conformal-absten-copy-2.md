# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Poisoning-Robust Conformal Absten

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/bb91195a-8912-4b30-ae4d-3bedeba4fa30.jsonl`
- **Structured JSON:** [`4564661b05714aeb8a14.json`](../../sessions/45/4564661b05714aeb8a14.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T07:51:40.730Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T07:51:40.730Z",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores\n\n## Core Problem\n\nRAG systems in adversarial environments (medical QA, legal retrieval, financial compliance) need distribution-free abstention guarantees when the retrieval corpus is poisoned. Corpus poisoning is a practical threat: CorruptRAG (arXiv 2025) achieves high attack success with a single injected document; PoisonedRAG (USENIX Security 2025) reaches 90%+ ASR with 5 documents. Existing conformal prediction methods for RAG (TRAQ, NAACL 2024; C-RAG, ICML 2024; Conformal-RAG, SIGIR 2025) assume benign retrieval—Chen et al. (arXiv:2603.16817, Mar 2026) demonstrated these guarantees break under distribution shift, producing vacuous outputs. Poisoning-robust CP (RPS, ICLR 2025 Spotlight) addresses calibration-set poisoning, not test-time retrieval corruption. Certified RAG defenses (RobustRAG, SaTML 2026; ReliabilityRAG, NeurIPS 2025) provide robust point estimates but no abstention mechanism or coverage certificates. The gap: no method provides distribution-free abstention guarantees for RAG under adversarial retrieval corruption.\n\n## Core Contribution and Theoretical Insight\n\nPRCA's central contribution is a **partition-induced reduction**: partitioning retrieved passages into disjoint groups and computing inter-group agreement deterministically reduces arbitrary test-time retrieval corruption to a bounded TV shift in the one-dimensional nonconformity score distribution. This bounded shift is absorbed by CRC (ICLR 2024) via inflated quantiles, yielding formal coverage certificates. This reduction—from high-dimensional adversarial corruption to one-dimensional bounded distributional shift—parallels the approach of Conformal Prediction under Lévy-Prokhorov Distribution Shifts (arXiv:2502.14105), which reduces high-dimensional shifts to one-dimensional score shifts via ambiguity sets.\n\n**Why not simply combine existing methods?** Three natural alternatives fail:\n\n(1) **RobustRAG + standard CP**: Running RobustRAG's isolate-then-aggregate to obtain a robust answer, then applying TRAQ/C-RAG for conformal abstention, fails because RobustRAG's aggregation transforms the output distribution in a poisoning-dependent manner. Nonconformity scores from clean calibration are no longer exchangeable with test-time scores under attack, and the magnitude of distributional shift is uncharacterized. PRCA explicitly bounds this shift via partition structure.\n\n(2) **Full-context self-consistency + CP**: Generating K answers from the same full retrieval set and using agreement as a conformal score (the approach of Conformal Abstention, arXiv:2405.01563) fails under poisoning because all K samples share the same poisoned context. The model may produce consistently wrong answers with high agreement, making the score blind to corruption. Partition isolates poisoned passages into a bounded number of groups, enabling detection.\n\n(3) **Logprob-based confidence + CP**: Using LLM token-level logprobabilities as nonconformity scores fails because adversarially crafted passages (e.g., via Semantic Chameleon's gradient-guided attacks, arXiv Mar 2026) are designed to appear authoritative, inflating model confidence on wrong answers. Logprob monotonicity with respect to correctness breaks under adversarial retrieval.\n\n**Partition is a theoretical necessity, not a design choice**: it is the structural mechanism that transforms uncharacterizable adversarial corruption into a bounded, quantifiable distributional shift that CRC can absorb.\n\n## Research Landscape\n\n**Conformal prediction for RAG:** TRAQ (NAACL 2024) and C-RAG (ICML 2024) established conformal prediction for RAG under benign retrieval. Conformal-RAG (SIGIR 2025) extends to group-conditional coverage. Chen et al. (arXiv:2603.16817, Mar 2026) showed all such methods produce vacuous prediction sets under distribution shift and retrieval corruption, but proposed no solution.\n\n**Certified RAG defenses:** RobustRAG (SaTML 2026) provides certified defense via isolate-then-aggregate, achieving certified robust accuracy on RealtimeQA/NQ. ReliabilityRAG (NeurIPS 2025) uses graph-theoretic MIS with NLI-based contradiction detection for provably robust document filtering. Both provide robust point estimates but no coverage certificates or abstention mechanism.\n\n**Poisoning-robust CP:** RPS (ICLR 2025 Spotlight) achieves poisoning-robust CP via smoothed scores and majority voting but assumes calibration-set poisoning—certificates do not transfer to test-time retrieval corruption.\n\n**Partition-based defenses:** RAGPart (arXiv:2512.24268, Dec 2025) uses document partitioning at the retrieval stage (fragment embeddings) to dilute poisoning. Three key differences from PRCA: (1) RAGPart operates at retrieval/embedding stage, PRCA at generation/calibration stage; (2) RAGPart outputs filtered retrieval sets, PRCA outputs {answer, abstain} decisions with coverage certificates; (3) they are complementary—RAGPart can preprocess retrieval before PRCA's certified abstention.\n\n**Adversarial aggregation:** The Consensus Trap (arXiv:2604.17139, Apr 2026) proves response-level majority voting fails when corrupted agents form a local majority. PRCA's majority answer output could face this risk, but: (a) PRCA's primary guarantee is the coverage certificate on the abstention decision, not the majority answer's correctness; (b) under the standard threat model k < n/2, the number of corrupted groups m = ceil(k/floor(n/K)) < K/2, so the honest majority is preserved.\n\n**Attack landscape:** PoisonedRAG (USENIX Security 2025), CorruptRAG (arXiv 2025), RSB Benchmark (May 2025, 13 attack methods × 7 defenses), Semantic Chameleon (arXiv Mar 2026, gradient-guided corpus-dependent attacks).\n\n**Distribution-shift-robust CP:** LP-shift framework (arXiv:2502.14105) reduces high-dimensional shifts to one-dimensional score shifts. PRCA's partition-induced TV bound is a specific instantiation for adversarial retrieval corruption.\n\nNo existing work combines conformal abstention with retrieval-poisoning robustness.\n\n## Proposed Approach\n\n**Step 1: Partition-and-Generate.** Partition top-n retrieved passages into K disjoint groups (random assignment). Generate a per-group answer via isolated LLM calls.\n\n**Step 2: Agreement Nonconformity Score.** For each group pair (i, j), compute NLI entailment probability e(i,j) = P(answer_i entails answer_j) using DeBERTa-v3-large (following ReliabilityRAG's NLI approach). Define:\n\ns = 1 − mean({e(i,j)} over all pairs)\n\nCritical properties: (1) **Monotonicity**: s increases with disagreement; higher s → more likely to abstain, satisfying CRC's monotone-loss requirement. (2) **Corruption-boundedness**: under k-poisoning, at most m = ceil(k/floor(n/K)) groups are corrupted, affecting at most m(K−1) of C(K,2) pairwise comparisons, yielding bounded perturbation to s.\n\n**Toward tighter bounds:** The worst-case TV ≤ m/K is a combinatorial upper bound. Because s is a mean of bounded pairwise scores, the actual perturbation from m corrupted groups may be dampened. We will empirically estimate the actual TV distance between clean and poisoned score CDFs (via bootstrap) and compare against the theoretical bound, reporting the tightness ratio. Exploring concentration-based bounds (leveraging the mean structure) is a concrete research direction.\n\n**Clean-condition variance mitigation:** If different passage groups cover different answer facets, clean-condition agreement variance inflates s and may cause excessive abstention. NLI-based semantic entailment (rather than exact match) is robust to surface variation. Calibration on clean data naturally accounts for residual clean-condition variance in the score distribution.\n\n**Step 3: TV-Bounded Calibration.** Under k-poisoning with K groups, corruption bound m determines maximal TV distance: TV ≤ m/K. Using CRC (ICLR 2024) with TV-inflated quantile: set abstention threshold at the (1 − α + TV)-quantile of calibration scores, yielding formal certificate P(correct or abstain) ≥ 1 − α under k-poisoning.\n\n**Calibration protocol:** Calibration set constructed on clean corpus (standard assumption per RPS, ICLR 2025), n_cal ≥ 500 per dataset. Sensitivity experiment evaluates coverage degradation when actual poisoning budget exceeds assumed k.\n\n**Step 4: Abstention Decision.** At test time, if s > λ (calibrated threshold), abstain; otherwise, output the majority answer across groups.\n\n## Experimental Design\n\n**Datasets:** Primary: NQ, HotpotQA, MS-MARCO (standard RAG benchmarks, used by PoisonedRAG/RobustRAG). Secondary: PubMedQA (domain-specific, core metrics only, validating high-stakes scenario motivation).\n\n**Attack methods:**\n- PoisonedRAG (targeted, k ∈ {1, 3, 5, 10})\n- CorruptRAG (single-document high-ASR)\n- One DoS-type attack from RSB Benchmark (May 2025) taxonomy\n- **Agreement-aware adaptive attack**: attacker knows K-partition structure and optimizes poisoned passage content to maximize cross-group NLI entailment (minimize s) while ensuring target wrong answer\n\n**Models:** Three scales for model-agnosticism: (1) primary: Qwen3.5-7B (or Llama-3-8B); (2) medium: Qwen3.5-32B; (3) large: Qwen3.5-72B. NLI model: DeBERTa-v3-large.\n\n**Baselines (8 methods):**\n- Conformal: TRAQ (NAACL 2024), C-RAG (ICML 2024), Conformal-RAG (SIGIR 2025)\n- Certified defense: RobustRAG (SaTML 2026), ReliabilityRAG (NeurIPS 2025)\n- Partition-based: RAGPart (arXiv:2512.24268)—same partition, no conformal (ablation baseline)\n- Compute-normalized: TRAQ + K× self-consistency voting\n- Naive pipeline: RobustRAG + TRAQ (empirically validates the \"Why not combine?\" theoretical argument)\n\n**Metrics:**\n- Primary: Certified coverage rate, empirical coverage under attack, abstention rate\n- Secondary: Clean accuracy (no attack), prediction set size, vacuousness rate (per Chen et al. 2026)\n- Tradeoff: Coverage vs. abstention at varying α; coverage vs. poisoning budget k; certified vs. empirical gap\n- Efficiency: Wall-clock time per query, token consumption\n\n**Ablation matrix** (full ablation on 7B only; 32B/72B do core config only):\n- K ∈ {1, 3, 5, 7, 10}: K=1 is the degenerate no-partition baseline proving partition necessity\n- n ∈ {10, 20, 30}: retrieval depth vs. certificate tightness\n- Score function: NLI entailment (primary) vs. ROUGE-L vs. exact match\n- Calibration: CRC + TV inflation (full method) vs. CRC without inflation (isolates TV contribution) vs. vanilla split conformal (isolates CRC contribution)\n- Partition strategy: random vs. round-robin by retrieval score\n\n**Diagnostic experiments:**\n- **NLI reliability**: Collect clean-group and corrupted-group LLM outputs under attack; evaluate DeBERTa NLI entailment accuracy and calibration (reliability diagram) on these output pairs. If unreliable, evaluate ensemble NLI or temperature-scaled NLI as robustness enhancement. Motivated by The Semantic Illusion (arXiv:2512.15068) findings on NLI limitations.\n- **TV bound tightness**: Empirically estimate actual TV distance between clean and poisoned score CDFs (bootstrap/KDE) vs. theoretical m/K bound. Report tightness ratio across attack settings.\n- **k sensitivity**: Evaluate coverage degradation when actual poisoning exceeds assumed k upper bound.\n\n**Scale:** 200-300 queries per dataset per setting (primary datasets); 200 queries for PubMedQA. 95% confidence intervals reported. Full ablation on 7B; 32B/72B validate core configuration only.\n\n**Discussion items:** (1) Partition-induced reduction as a potential general principle for lifting point-estimate certified defenses to distributional guarantees (future work). (2) k-poisoning assumption validity across different attack types. (3) Gradient-based adaptive attacks (Semantic Chameleon) as future robustness evaluation.\n\n## Key References\n\n- TRAQ: Trustworthy Retrieval Augmented QA via Conformal Prediction (NAACL 2024)\n- C-RAG: Certified Generation Risks for RAG (ICML 2024)\n- Conformal Risk Control (ICLR 2024)\n- Provably Reliable Conformal Prediction Sets under Poisoning (ICLR 2025 Spotlight)\n- Certifiably Robust RAG against Retrieval Corruption (SaTML 2026)\n- ReliabilityRAG (NeurIPS 2025)\n- Is Conformal Factuality for RAG-based LLMs Robust? (arXiv:2603.16817, Mar 2026)\n- Conformal-RAG: Conditional Conformal Factuality (SIGIR 2025)\n- CorruptRAG: Practical Poisoning Attacks against RAG (arXiv 2025)\n- PoisonedRAG (USENIX Security 2025)\n- RSB Benchmark: Benchmarking Poisoning Attacks against RAG (May 2025)\n- RAGPart & RAGMask (arXiv:2512.24268, Dec 2025)\n- Conformal Prediction under Lévy-Prokhorov Distribution Shifts (arXiv:2502.14105)\n- Semantic Chameleon (arXiv Mar 2026)\n- Mitigating LLM Hallucinations via Conformal Abstention (arXiv:2405.01563)\n- The Consensus Trap (arXiv:2604.17139, Apr 2026)\n- The Semantic Illusion (arXiv:2512.15068)"
}
```

---

### Runtime record

_source line 2 · 2026-05-30T07:51:40.734Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T07:51:40.734Z",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30"
}
```

---

## Round 1

43 recorded events

### User

_source line 3 · 2026-05-30T07:51:40.787Z_

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
  "promptId": "42f0fa8d-2ab5-4522-bbdc-de8010b9f267",
  "type": "user",
  "uuid": "7b217159-e78c-4297-a7e9-7ecef6d5d8dd",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T07:51:40.786Z_

```json
{
  "parentUuid": "7b217159-e78c-4297-a7e9-7ecef6d5d8dd",
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
  "uuid": "c08cb6b0-84a4-4440-8f2b-2b63b008fc51",
  "timestamp": "2026-05-30T07:51:40.786Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T07:51:40.786Z_

```json
{
  "parentUuid": "c08cb6b0-84a4-4440-8f2b-2b63b008fc51",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "37d1bd31-933f-4fe6-aadc-0e67664468ca",
  "timestamp": "2026-05-30T07:51:40.786Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
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
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30"
}
```

---

### Assistant

_source line 7 · 2026-05-30T07:51:46.739Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for AAAI 2026. Before I can give any scores, I need to do thorough literature research using WebSearch. Let me first load the WebSearch tool, then conduct several searches to understand the current landscape.

The proposal is about "Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores" (PRCA). It combines conformal prediction with retrieval-poisoning robustness for RAG systems.

Let me start by loading the WebSearch tool and then conducting searches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37d1bd31-933f-4fe6-aadc-0e67664468ca",
  "isSidechain": false,
  "requestId": "req_011CbYPYmLXnVWeFdtoMbhMr",
  "type": "assistant",
  "uuid": "01739fc5-6885-4ddb-9ce6-c2e86b9c7332",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015BPqDxAYzQGBv3RhGpaptn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 18580,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 216,
          "cache_read_input_tokens": 18580,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 8 · 2026-05-30T07:51:47.354Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EUs9seVnRMDkgaADTMG8Yg`</summary>

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
  "parentUuid": "01739fc5-6885-4ddb-9ce6-c2e86b9c7332",
  "isSidechain": false,
  "requestId": "req_011CbYPYmLXnVWeFdtoMbhMr",
  "type": "assistant",
  "uuid": "0dca3215-a148-4bd6-87bc-412bb37b5c4a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015BPqDxAYzQGBv3RhGpaptn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 18580,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 216,
          "cache_read_input_tokens": 18580,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 9 · 2026-05-30T07:51:47.363Z_

<details><summary>↩ Tool result · `toolu_01EUs9seVnRMDkgaADTMG8Yg`</summary>

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
  "parentUuid": "0dca3215-a148-4bd6-87bc-412bb37b5c4a",
  "isSidechain": false,
  "promptId": "42f0fa8d-2ab5-4522-bbdc-de8010b9f267",
  "type": "user",
  "uuid": "e51e1a1d-c965-4046-a52f-a279e2f6b701",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "0dca3215-a148-4bd6-87bc-412bb37b5c4a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 10_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores  ## Core Problem  RAG systems in ad…",
  "leafUuid": "e51e1a1d-c965-4046-a52f-a279e2f6b701",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Poisoning-robust conformal abstention for RAG systems",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30"
}
```

---

### Assistant

_source line 12 · 2026-05-30T07:51:53.191Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me conduct multiple targeted searches to understand the research landscape before evaluating this proposal. I need to search for:

1. Conformal prediction for RAG systems - recent work
2. Corpus poisoning attacks on RAG - recent defenses
3. RobustRAG, ReliabilityRAG - certified RAG defenses
4. Poisoning-robust conformal prediction (RPS, ICLR 2025)
5. Partition-based RAG defenses

Let me run these searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e51e1a1d-c965-4046-a52f-a279e2f6b701",
  "isSidechain": false,
  "requestId": "req_011CbYPZGVip7CCcqYxabvVV",
  "type": "assistant",
  "uuid": "a701ff69-ec33-4474-985a-e33d0fd94667",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015dLESzqTWGwZojA7gwRgYR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 744,
      "cache_read_input_tokens": 18580,
      "output_tokens": 397,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 744,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 397,
          "cache_read_input_tokens": 18580,
          "cache_creation_input_tokens": 744,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 744
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

_source line 13 · 2026-05-30T07:51:53.356Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Az7argzmWX54e3MoMimqjo`</summary>

```json
{
  "query": "conformal prediction RAG retrieval augmented generation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a701ff69-ec33-4474-985a-e33d0fd94667",
  "isSidechain": false,
  "requestId": "req_011CbYPZGVip7CCcqYxabvVV",
  "type": "assistant",
  "uuid": "d636cad6-d08c-47da-a926-271962da2897",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015dLESzqTWGwZojA7gwRgYR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 744,
      "cache_read_input_tokens": 18580,
      "output_tokens": 397,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 744,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 397,
          "cache_read_input_tokens": 18580,
          "cache_creation_input_tokens": 744,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 744
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

_source line 14 · 2026-05-30T07:51:54.320Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017t3PtQ13KkcDwbXvRcB1DZ`</summary>

```json
{
  "query": "corpus poisoning attack RAG defense certified robust 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d636cad6-d08c-47da-a926-271962da2897",
  "isSidechain": false,
  "requestId": "req_011CbYPZGVip7CCcqYxabvVV",
  "type": "assistant",
  "uuid": "a46db8e3-ced1-454f-b949-a8698043b9d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015dLESzqTWGwZojA7gwRgYR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 744,
      "cache_read_input_tokens": 18580,
      "output_tokens": 397,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 744,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 397,
          "cache_read_input_tokens": 18580,
          "cache_creation_input_tokens": 744,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 744
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

_source line 15 · 2026-05-30T07:51:55.383Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018bVmoH1xYpCobbqa9PsjDR`</summary>

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
  "parentUuid": "a46db8e3-ced1-454f-b949-a8698043b9d4",
  "isSidechain": false,
  "requestId": "req_011CbYPZGVip7CCcqYxabvVV",
  "type": "assistant",
  "uuid": "33e51efc-efc8-48c7-b359-2005b96b5315",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015dLESzqTWGwZojA7gwRgYR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 744,
      "cache_read_input_tokens": 18580,
      "output_tokens": 397,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 744,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 397,
          "cache_read_input_tokens": 18580,
          "cache_creation_input_tokens": 744,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 744
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

_source line 16 · 2026-05-30T07:51:55.826Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Roa3HLEpPrVo77RSkmjYPU`</summary>

```json
{
  "query": "poisoning robust conformal prediction RPS ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33e51efc-efc8-48c7-b359-2005b96b5315",
  "isSidechain": false,
  "requestId": "req_011CbYPZGVip7CCcqYxabvVV",
  "type": "assistant",
  "uuid": "cb57cdc7-60fb-41e8-bff6-b6bc3fb40752",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015dLESzqTWGwZojA7gwRgYR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 744,
      "cache_read_input_tokens": 18580,
      "output_tokens": 397,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 744,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 397,
          "cache_read_input_tokens": 18580,
          "cache_creation_input_tokens": 744,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 744
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

_source line 17 · 2026-05-30T07:51:55.971Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013k14Ehd1K1Jt4rgddZaxzn`</summary>

```json
{
  "query": "conformal risk control distribution shift robust abstention 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb57cdc7-60fb-41e8-bff6-b6bc3fb40752",
  "isSidechain": false,
  "requestId": "req_011CbYPZGVip7CCcqYxabvVV",
  "type": "assistant",
  "uuid": "7cf59382-d1dd-416c-a93f-29189891b77b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015dLESzqTWGwZojA7gwRgYR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 744,
      "cache_read_input_tokens": 18580,
      "output_tokens": 397,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 744,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 397,
          "cache_read_input_tokens": 18580,
          "cache_creation_input_tokens": 744,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 744
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

_source line 18 · 2026-05-30T07:52:01.548Z_

<details><summary>↩ Tool result · `toolu_01Az7argzmWX54e3MoMimqjo`</summary>

```text
Web search results for query: "conformal prediction RAG retrieval augmented generation 2025 2026"

Links: [{"title":"Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-21300-6_45"},{"title":"Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/html/2506.20978v1"},{"title":"[2506.20978] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/abs/2506.20978"},{"title":"[2506.20978v1] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/abs/2506.20978v1"},{"title":"TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal   Prediction","url":"https://arxiv.org/pdf/2307.04642"},{"title":"Towards Dependable Retrieval-Augmented Generation Using Factual Confidence Prediction","url":"https://arxiv.org/html/2605.05244v1"},{"title":"RAG is DEAD!. Retrieval-Augmented Generation ruled… | by Reliable Data Engineering | Medium","url":"https://medium.com/@reliabledataengineering/rag-is-dead-and-why-thats-the-best-news-you-ll-hear-all-year-0f3de8c44604"},{"title":"Conformal Prediction: A Data Perspective | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3736575"}]

Based on the search results, here are some key findings about conformal prediction and RAG (Retrieval Augmented Generation) in 2025-2026:

## Recent Research

A novel framework called Conformal-RAG has been proposed to address limitations in RAG trustworthiness by leveraging conformal prediction (CP) and internal information from the RAG mechanism to offer statistical guarantees on response quality. This approach retains up to 60% more high-quality sub-claims from responses compared to direct applications of CP to LLMs, while maintaining the same reliability guarantee.

## Problem Being Addressed

RAG-based question-answering systems sometimes misinterpret user queries, struggle with reasoning in unseen scenarios, and may generate claims that are irrelevant or even contradictory to the provided documents. Recent methods that attempt to improve RAG trustworthiness, such as through auto-evaluation metrics, lack probabilistic guarantees or require ground truth answers.

## Technical Approach

Conformal-RAG ensures group-conditional coverage spanning multiple sub-domains without requiring manual labelling of conformal sets, making it suitable for complex RAG applications. The approach provides separate metrics for the stages of context retrieval and LLM-based answer generation, and demonstrates that conformal prediction is an effective way to provide confidence guarantees for the correctness of chunks.

These developments represent significant progress in making RAG systems more trustworthy and reliable through formal statistical guarantees.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d636cad6-d08c-47da-a926-271962da2897",
  "isSidechain": false,
  "promptId": "42f0fa8d-2ab5-4522-bbdc-de8010b9f267",
  "type": "user",
  "uuid": "efcbf84e-4a2b-4055-be63-147e4c310661",
  "toolUseResult": {
    "query": "conformal prediction RAG retrieval augmented generation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FP3YRjHoKMmgChaDv8oMUG",
        "content": [
          {
            "title": "Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-3-032-21300-6_45"
          },
          {
            "title": "Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality",
            "url": "https://arxiv.org/html/2506.20978v1"
          },
          {
            "title": "[2506.20978] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality",
            "url": "https://arxiv.org/abs/2506.20978"
          },
          {
            "title": "[2506.20978v1] Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality",
            "url": "https://arxiv.org/abs/2506.20978v1"
          },
          {
            "title": "TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal   Prediction",
            "url": "https://arxiv.org/pdf/2307.04642"
          },
          {
            "title": "Towards Dependable Retrieval-Augmented Generation Using Factual Confidence Prediction",
            "url": "https://arxiv.org/html/2605.05244v1"
          },
          {
            "title": "RAG is DEAD!. Retrieval-Augmented Generation ruled… | by Reliable Data Engineering | Medium",
            "url": "https://medium.com/@reliabledataengineering/rag-is-dead-and-why-thats-the-best-news-you-ll-hear-all-year-0f3de8c44604"
          },
          {
            "title": "Conformal Prediction: A Data Perspective | ACM Computing Surveys",
            "url": "https://dl.acm.org/doi/10.1145/3736575"
          }
        ]
      },
      "Based on the search results, here are some key findings about conformal prediction and RAG (Retrieval Augmented Generation) in 2025-2026:\n\n## Recent Research\n\nA novel framework called Conformal-RAG has been proposed to address limitations in RAG trustworthiness by leveraging conformal prediction (CP) and internal information from the RAG mechanism to offer statistical guarantees on response quality. This approach retains up to 60% more high-quality sub-claims from responses compared to direct applications of CP to LLMs, while maintaining the same reliability guarantee.\n\n## Problem Being Addressed\n\nRAG-based question-answering systems sometimes misinterpret user queries, struggle with reasoning in unseen scenarios, and may generate claims that are irrelevant or even contradictory to the provided documents. Recent methods that attempt to improve RAG trustworthiness, such as through auto-evaluation metrics, lack probabilistic guarantees or require ground truth answers.\n\n## Technical Approach\n\nConformal-RAG ensures group-conditional coverage spanning multiple sub-domains without requiring manual labelling of conformal sets, making it suitable for complex RAG applications. The approach provides separate metrics for the stages of context retrieval and LLM-based answer generation, and demonstrates that conformal prediction is an effective way to provide confidence guarantees for the correctness of chunks.\n\nThese developments represent significant progress in making RAG systems more trustworthy and reliable through formal statistical guarantees."
    ],
    "durationSeconds": 8.186009512999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d636cad6-d08c-47da-a926-271962da2897",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-30T07:52:01.901Z_

<details><summary>↩ Tool result · `toolu_01Roa3HLEpPrVo77RSkmjYPU`</summary>

```text
Web search results for query: "poisoning robust conformal prediction RPS ICLR 2025"

Links: [{"title":"Published as a conference paper at ICLR 2025","url":"https://yascho.github.io/assets/pdf/scholten2025provably.pdf"},{"title":"PROVABLY RELIABLE CONFORMAL PREDICTION SETS IN THE PRESENCE OF DATA POISONING - Technical University of Munich","url":"https://portal.fis.tum.de/en/publications/provably-reliable-conformal-prediction-sets-in-the-presence-of-da/"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4d21a4b33361c40c2142db9511c126-Paper-Conference.pdf"},{"title":"Nine papers accepted at ICLR 2025, one at KAIS 2025 - Data Analytics and Machine Learning","url":"https://www.cs.cit.tum.de/en/daml/all-news/article/nine-papers-accepted-at-iclr-2025/"},{"title":"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning | OpenReview","url":"https://openreview.net/forum?id=ofuLWn8DFZ"},{"title":"GitHub - yascho/reliable_conformal_prediction: Implementation of the reliable conformal prediction sets introduced in the paper: \"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning\" accepted at ICLR 2025 (Spotlight).","url":"https://github.com/yascho/reliable_conformal_prediction"},{"title":"Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning","url":"https://arxiv.org/pdf/2410.09878"},{"title":"Robust Yet Efficient Conformal Prediction Sets","url":"https://arxiv.org/pdf/2407.09165"}]

Based on the search results, I found information about the paper on poisoning-robust conformal prediction at ICLR 2025:

The paper proposes Reliable Prediction Sets (RPS): the first efficient method for constructing prediction sets more reliable under data poisoning where adversaries can modify, add and delete datapoints from training and calibration sets.

The approach consists of two key components: First, smoothed score functions that reliably aggregate predictions from classifiers trained on distinct partitions of the training data, improving reliability under training poisoning. Second, calibration of multiple prediction sets on disjoint subsets of the calibration data and construction of a majority prediction set.

The authors derive novel certificates that guarantee the reliability of RPS under worst-case data poisoning attacks, including guarantees against label flipping attacks.

The paper was authored by Yan Scholten and Stephan Günnemann and received a Spotlight presentation at ICLR 2025. The authors have also made their reference implementation publicly available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb57cdc7-60fb-41e8-bff6-b6bc3fb40752",
  "isSidechain": false,
  "promptId": "42f0fa8d-2ab5-4522-bbdc-de8010b9f267",
  "type": "user",
  "uuid": "ed863332-9486-4bd2-b499-622612ec8d25",
  "toolUseResult": {
    "query": "poisoning robust conformal prediction RPS ICLR 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_017E7BA4ppixjohPN5bLuAoS",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://yascho.github.io/assets/pdf/scholten2025provably.pdf"
          },
          {
            "title": "PROVABLY RELIABLE CONFORMAL PREDICTION SETS IN THE PRESENCE OF DATA POISONING - Technical University of Munich",
            "url": "https://portal.fis.tum.de/en/publications/provably-reliable-conformal-prediction-sets-in-the-presence-of-da/"
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
            "title": "Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning | OpenReview",
            "url": "https://openreview.net/forum?id=ofuLWn8DFZ"
          },
          {
            "title": "GitHub - yascho/reliable_conformal_prediction: Implementation of the reliable conformal prediction sets introduced in the paper: \"Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning\" accepted at ICLR 2025 (Spotlight).",
            "url": "https://github.com/yascho/reliable_conformal_prediction"
          },
          {
            "title": "Provably Reliable Conformal Prediction Sets in the Presence of Data   Poisoning",
            "url": "https://arxiv.org/pdf/2410.09878"
          },
          {
            "title": "Robust Yet Efficient Conformal Prediction Sets",
            "url": "https://arxiv.org/pdf/2407.09165"
          }
        ]
      },
      "Based on the search results, I found information about the paper on poisoning-robust conformal prediction at ICLR 2025:\n\nThe paper proposes Reliable Prediction Sets (RPS): the first efficient method for constructing prediction sets more reliable under data poisoning where adversaries can modify, add and delete datapoints from training and calibration sets.\n\nThe approach consists of two key components: First, smoothed score functions that reliably aggregate predictions from classifiers trained on distinct partitions of the training data, improving reliability under training poisoning. Second, calibration of multiple prediction sets on disjoint subsets of the calibration data and construction of a majority prediction set.\n\nThe authors derive novel certificates that guarantee the reliability of RPS under worst-case data poisoning attacks, including guarantees against label flipping attacks.\n\nThe paper was authored by Yan Scholten and Stephan Günnemann and received a Spotlight presentation at ICLR 2025. The authors have also made their reference implementation publicly available on GitHub."
    ],
    "durationSeconds": 6.071599139000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "cb57cdc7-60fb-41e8-bff6-b6bc3fb40752",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-30T07:52:02.273Z_

<details><summary>↩ Tool result · `toolu_017t3PtQ13KkcDwbXvRcB1DZ`</summary>

```text
Web search results for query: "corpus poisoning attack RAG defense certified robust 2025 2026"

Links: [{"title":"Certified Defenses for RAG Systems","url":"https://www.emergentmind.com/topics/certified-defenses-for-rag-systems"},{"title":"RAG Poisoning: Threats and Defenses","url":"https://www.emergentmind.com/topics/retrieval-augmented-generation-rag-poisoning"},{"title":"Addressing Corpus Knowledge Poisoning Attacks on RAG Using Sparse Attention","url":"https://www.arxiv.org/pdf/2602.04711"},{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"RAG Poisoning: Contaminating the AI’s “Source of Truth” | by InstaTunnel | Medium","url":"https://medium.com/@instatunnel/rag-poisoning-contaminating-the-ais-source-of-truth-082dcbdeea7c"},{"title":"RAGShield: Provenance-Verified Defense-in-Depth Against Knowledge Base Poisoning in Government Retrieval-Augmented Generation Systems","url":"https://arxiv.org/html/2604.00387v1"},{"title":"Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems","url":"https://arxiv.org/pdf/2603.18034"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/html/2405.15556v2"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/pdf/2509.23519"}]

Based on the search results, here's what I found about corpus poisoning attacks on RAG systems and certified robust defenses in 2025-2026:

## Corpus Poisoning Attacks on RAG

Corpus poisoning involves the introduction of poisoned documents into the corpus, mimicking benign content and structure to maximize ranking or aggregation influence. Research demonstrates that injecting just five malicious texts into a knowledge database containing millions of documents can achieve a 90% attack success rate, and poisoning merely 0.04% of a corpus can lead to a 98.2% attack success rate and 74.6% system failure.

## Certified Robust Defenses

Several certified defense approaches have emerged:

**RobustRAG**: RobustRAG is proposed as the first certifiably robust defense framework against retrieval corruption attacks, built around the core insight of an isolate-then-aggregate strategy. RobustRAG achieves substantial certifiable robustness while maintaining high clean performance, e.g., 71% clean accuracy and 38% certifiable robust accuracy on the RealtimeQA dataset, compared to 69% clean accuracy and no certifiable accuracy for vanilla RAG.

**RAGPart & RAGMask**: RAGPart leverages the inherent training dynamics of dense retrievers, exploiting document partitioning to mitigate the effect of poisoned points, while RAGMask identifies suspicious tokens based on significant similarity shifts under targeted token masking, and across benchmarks, both defenses consistently reduce attack success rates while preserving utility under benign conditions.

**General Defense Directions**: The vulnerability of RAG architectures to adversarial manipulations has driven the rapid development of certified defenses that deliver formal guarantees against classes of adversarial threats, typically via ranking, aggregation, or detection strategies that admit worst-case bounds, probabilistic guarantees, or explicit certificates of robust operation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a46db8e3-ced1-454f-b949-a8698043b9d4",
  "isSidechain": false,
  "promptId": "42f0fa8d-2ab5-4522-bbdc-de8010b9f267",
  "type": "user",
  "uuid": "a3fc1a21-f455-403d-9074-744f05e32cb5",
  "toolUseResult": {
    "query": "corpus poisoning attack RAG defense certified robust 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DuUE5y6BmxxTu5cYmpJcUb",
        "content": [
          {
            "title": "Certified Defenses for RAG Systems",
            "url": "https://www.emergentmind.com/topics/certified-defenses-for-rag-systems"
          },
          {
            "title": "RAG Poisoning: Threats and Defenses",
            "url": "https://www.emergentmind.com/topics/retrieval-augmented-generation-rag-poisoning"
          },
          {
            "title": "Addressing Corpus Knowledge Poisoning Attacks on RAG Using Sparse Attention",
            "url": "https://www.arxiv.org/pdf/2602.04711"
          },
          {
            "title": "RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2512.24268"
          },
          {
            "title": "RAG Poisoning: Contaminating the AI’s “Source of Truth” | by InstaTunnel | Medium",
            "url": "https://medium.com/@instatunnel/rag-poisoning-contaminating-the-ais-source-of-truth-082dcbdeea7c"
          },
          {
            "title": "RAGShield: Provenance-Verified Defense-in-Depth Against Knowledge Base Poisoning in Government Retrieval-Augmented Generation Systems",
            "url": "https://arxiv.org/html/2604.00387v1"
          },
          {
            "title": "Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems",
            "url": "https://arxiv.org/pdf/2603.18034"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://arxiv.org/html/2405.15556v2"
          },
          {
            "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://arxiv.org/pdf/2509.23519"
          }
        ]
      },
      "Based on the search results, here's what I found about corpus poisoning attacks on RAG systems and certified robust defenses in 2025-2026:\n\n## Corpus Poisoning Attacks on RAG\n\nCorpus poisoning involves the introduction of poisoned documents into the corpus, mimicking benign content and structure to maximize ranking or aggregation influence. Research demonstrates that injecting just five malicious texts into a knowledge database containing millions of documents can achieve a 90% attack success rate, and poisoning merely 0.04% of a corpus can lead to a 98.2% attack success rate and 74.6% system failure.\n\n## Certified Robust Defenses\n\nSeveral certified defense approaches have emerged:\n\n**RobustRAG**: RobustRAG is proposed as the first certifiably robust defense framework against retrieval corruption attacks, built around the core insight of an isolate-then-aggregate strategy. RobustRAG achieves substantial certifiable robustness while maintaining high clean performance, e.g., 71% clean accuracy and 38% certifiable robust accuracy on the RealtimeQA dataset, compared to 69% clean accuracy and no certifiable accuracy for vanilla RAG.\n\n**RAGPart & RAGMask**: RAGPart leverages the inherent training dynamics of dense retrievers, exploiting document partitioning to mitigate the effect of poisoned points, while RAGMask identifies suspicious tokens based on significant similarity shifts under targeted token masking, and across benchmarks, both defenses consistently reduce attack success rates while preserving utility under benign conditions.\n\n**General Defense Directions**: The vulnerability of RAG architectures to adversarial manipulations has driven the rapid development of certified defenses that deliver formal guarantees against classes of adversarial threats, typically via ranking, aggregation, or detection strategies that admit worst-case bounds, probabilistic guarantees, or explicit certificates of robust operation."
    ],
    "durationSeconds": 7.950849758999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a46db8e3-ced1-454f-b949-a8698043b9d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-30T07:52:03.283Z_

<details><summary>↩ Tool result · `toolu_018bVmoH1xYpCobbqa9PsjDR`</summary>

```text
Web search results for query: "RobustRAG certified defense retrieval corruption SaTML 2026"

Links: [{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://goatstack.ai/topics/certifiably-robust-rag-against-retrieval-corruption-yclugx"},{"title":"IEEE SaTML 2026 · Program","url":"https://satml.org/program/"},{"title":"IEEE SaTML 2026 · Accepted Papers","url":"https://satml.org/accepted-papers/"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/pdf/2405.15556"},{"title":"Certifiably Robust RAG against Retrieval Corruption | Request PDF","url":"https://www.researchgate.net/publication/380895542_Certifiably_Robust_RAG_against_Retrieval_Corruption"},{"title":"[Literature Review] Certifiably Robust RAG against Retrieval Corruption","url":"https://www.themoonlight.io/en/review/certifiably-robust-rag-against-retrieval-corruption"},{"title":"Certifiably Robust RAG against Retrieval Corruption Attacks | OpenReview","url":"https://openreview.net/forum?id=cU6ZdN87p3"},{"title":"[2405.15556] Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/abs/2405.15556"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://openreview.net/pdf?id=qsEeACAJjD"}]

Based on the search results, here's what I found about RobustRAG and its presentation at SaTML 2026:

## Overview

RobustRAG is the first defense framework with certifiable robustness against retrieval corruption attacks. Retrieval-augmented generation (RAG) is susceptible to retrieval corruption attacks, where malicious passages injected into retrieval results can lead to inaccurate model responses.

## How It Works

The key insight of RobustRAG is an isolate-then-aggregate strategy: passages are isolated into disjoint groups, LLM responses are generated based on the concatenated passages from each isolated group, and then these responses are securely aggregated for a robust output. To instantiate RobustRAG, keyword-based and decoding-based algorithms are designed for securely aggregating unstructured text responses.

## Performance and Evaluation

RobustRAG was evaluated on the tasks of open-domain question-answering and free-form long text generation and demonstrated its effectiveness across three datasets and three LLMs. RobustRAG achieves 69.0–71.0% certifiable robust accuracy for RQA-MC, 24.0–49.0% for RQA, 27.0–47.0% for NQ, and 24.0–51.2% certifiable LLM-judge score for the bio generation task.

## Authors

The paper was authored by Chong Xiang (NVIDIA), Tong Wu, Zexuan Zhong (Princeton University), David Wagner (University of California, Berkeley), Danqi Chen and Prateek Mittal (Princeton University).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33e51efc-efc8-48c7-b359-2005b96b5315",
  "isSidechain": false,
  "promptId": "42f0fa8d-2ab5-4522-bbdc-de8010b9f267",
  "type": "user",
  "uuid": "7f24dd3d-1417-425a-ad91-864bc4baeef8",
  "toolUseResult": {
    "query": "RobustRAG certified defense retrieval corruption SaTML 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UrxD8Jo74i4WXd9vu5DCHp",
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
      "Based on the search results, here's what I found about RobustRAG and its presentation at SaTML 2026:\n\n## Overview\n\nRobustRAG is the first defense framework with certifiable robustness against retrieval corruption attacks. Retrieval-augmented generation (RAG) is susceptible to retrieval corruption attacks, where malicious passages injected into retrieval results can lead to inaccurate model responses.\n\n## How It Works\n\nThe key insight of RobustRAG is an isolate-then-aggregate strategy: passages are isolated into disjoint groups, LLM responses are generated based on the concatenated passages from each isolated group, and then these responses are securely aggregated for a robust output. To instantiate RobustRAG, keyword-based and decoding-based algorithms are designed for securely aggregating unstructured text responses.\n\n## Performance and Evaluation\n\nRobustRAG was evaluated on the tasks of open-domain question-answering and free-form long text generation and demonstrated its effectiveness across three datasets and three LLMs. RobustRAG achieves 69.0–71.0% certifiable robust accuracy for RQA-MC, 24.0–49.0% for RQA, 27.0–47.0% for NQ, and 24.0–51.2% certifiable LLM-judge score for the bio generation task.\n\n## Authors\n\nThe paper was authored by Chong Xiang (NVIDIA), Tong Wu, Zexuan Zhong (Princeton University), David Wagner (University of California, Berkeley), Danqi Chen and Prateek Mittal (Princeton University)."
    ],
    "durationSeconds": 7.896482174000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "33e51efc-efc8-48c7-b359-2005b96b5315",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
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
  "leafUuid": "7f24dd3d-1417-425a-ad91-864bc4baeef8",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Poisoning-robust conformal abstention for RAG systems",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30"
}
```

---

### Tool result

_source line 24 · 2026-05-30T07:52:04.869Z_

<details><summary>↩ Tool result · `toolu_013k14Ehd1K1Jt4rgddZaxzn`</summary>

```text
Web search results for query: "conformal risk control distribution shift robust abstention 2025 2026"

Links: [{"title":"Explicit Abstention Knobs for Predictable Reliability in Video Question Answering","url":"https://arxiv.org/html/2601.00138v1"},{"title":"[2208.02814] Conformal Risk Control","url":"https://arxiv.org/abs/2208.02814"},{"title":"Conformal Risk Control | OpenReview","url":"https://openreview.net/forum?id=33XGfHLtZg"},{"title":"Anytime-Valid Conformal Risk Control","url":"https://arxiv.org/html/2602.04364v1"},{"title":"Conformal Selective Prediction with General Risk Control","url":"https://arxiv.org/html/2603.24704v1"},{"title":"arXiv:2208.02814v4 [stat.ME] 13 Jun 2025 Conformal Risk Control","url":"https://arxiv.org/pdf/2208.02814"},{"title":"Anytime-Valid Conformal Risk Control","url":"https://arxiv.org/pdf/2602.04364"},{"title":"Conformal Selective Prediction with General Risk Control","url":"https://arxiv.org/pdf/2603.24704"},{"title":"[2510.07750] Calibrating Decision Robustness via Inverse Conformal Risk Control","url":"https://arxiv.org/abs/2510.07750"},{"title":"(PDF) Selective Conformal Risk Control","url":"https://www.researchgate.net/publication/398721023_Selective_Conformal_Risk_Control"}]

Based on the search results, here's what I found regarding conformal risk control, distribution shift, robust abstention, and recent work from 2025-2026:

## Key Recent Work

**Conformal Risk Control Foundations:**
Conformal risk control extends conformal prediction to control the expected value of any monotone loss function. Extensions of the idea include distribution shift, quantile risk control, multiple and adversarial risk control, and expectations of U-statistics.

**Selective Classification with Abstention:**
Xu et al. (2025) combine selective classification with conformal prediction in Selective Conformal Risk Control (SCRC), a two-stage approach that first filters uncertain inputs, then constructs conformal sets for accepted inputs.

**Distribution Shift and Robustness:**
Heng and Soh (2025) revisit selective prediction through the Neyman-Pearson lens, showing that the optimal acceptance rule is a likelihood-ratio test, and propose new selection scores combining distance-from-training-data with model logits, finding improved robustness under covariate shift.

Recent research has shown that conformal prediction and selection under covariate shift enjoy "double robustness" properties in the sense that they achieve desired guarantees (coverage or FDR control) when either estimated weights are consistent or certain score functions converge to ideal scores.

**2026 Developments:**
Calibration-conditional miscoverage control under distribution shifts was recently achieved in (Pournaderi & Xiang, 2026). Additionally, a new framework provides distribution-free, finite-sample guarantees on both miscoverage and regret for any family of robust predict-then-optimize policies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cf59382-d1dd-416c-a93f-29189891b77b",
  "isSidechain": false,
  "promptId": "42f0fa8d-2ab5-4522-bbdc-de8010b9f267",
  "type": "user",
  "uuid": "754725c7-9cf1-42e2-94bd-29e99216bbdd",
  "toolUseResult": {
    "query": "conformal risk control distribution shift robust abstention 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01543gESNUhJtYuDDMs7bSzj",
        "content": [
          {
            "title": "Explicit Abstention Knobs for Predictable Reliability in Video Question Answering",
            "url": "https://arxiv.org/html/2601.00138v1"
          },
          {
            "title": "[2208.02814] Conformal Risk Control",
            "url": "https://arxiv.org/abs/2208.02814"
          },
          {
            "title": "Conformal Risk Control | OpenReview",
            "url": "https://openreview.net/forum?id=33XGfHLtZg"
          },
          {
            "title": "Anytime-Valid Conformal Risk Control",
            "url": "https://arxiv.org/html/2602.04364v1"
          },
          {
            "title": "Conformal Selective Prediction with General Risk Control",
            "url": "https://arxiv.org/html/2603.24704v1"
          },
          {
            "title": "arXiv:2208.02814v4 [stat.ME] 13 Jun 2025 Conformal Risk Control",
            "url": "https://arxiv.org/pdf/2208.02814"
          },
          {
            "title": "Anytime-Valid Conformal Risk Control",
            "url": "https://arxiv.org/pdf/2602.04364"
          },
          {
            "title": "Conformal Selective Prediction with General Risk Control",
            "url": "https://arxiv.org/pdf/2603.24704"
          },
          {
            "title": "[2510.07750] Calibrating Decision Robustness via Inverse Conformal Risk Control",
            "url": "https://arxiv.org/abs/2510.07750"
          },
          {
            "title": "(PDF) Selective Conformal Risk Control",
            "url": "https://www.researchgate.net/publication/398721023_Selective_Conformal_Risk_Control"
          }
        ]
      },
      "Based on the search results, here's what I found regarding conformal risk control, distribution shift, robust abstention, and recent work from 2025-2026:\n\n## Key Recent Work\n\n**Conformal Risk Control Foundations:**\nConformal risk control extends conformal prediction to control the expected value of any monotone loss function. Extensions of the idea include distribution shift, quantile risk control, multiple and adversarial risk control, and expectations of U-statistics.\n\n**Selective Classification with Abstention:**\nXu et al. (2025) combine selective classification with conformal prediction in Selective Conformal Risk Control (SCRC), a two-stage approach that first filters uncertain inputs, then constructs conformal sets for accepted inputs.\n\n**Distribution Shift and Robustness:**\nHeng and Soh (2025) revisit selective prediction through the Neyman-Pearson lens, showing that the optimal acceptance rule is a likelihood-ratio test, and propose new selection scores combining distance-from-training-data with model logits, finding improved robustness under covariate shift.\n\nRecent research has shown that conformal prediction and selection under covariate shift enjoy \"double robustness\" properties in the sense that they achieve desired guarantees (coverage or FDR control) when either estimated weights are consistent or certain score functions converge to ideal scores.\n\n**2026 Developments:**\nCalibration-conditional miscoverage control under distribution shifts was recently achieved in (Pournaderi & Xiang, 2026). Additionally, a new framework provides distribution-free, finite-sample guarantees on both miscoverage and regret for any family of robust predict-then-optimize policies."
    ],
    "durationSeconds": 8.895071907,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7cf59382-d1dd-416c-a93f-29189891b77b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-30T07:52:10.056Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I've gotten substantial results. Let me do a few more targeted searches to fill in gaps - specifically about:
1. Chen et al. 2026 paper about conformal factuality robustness for RAG
2. The Consensus Trap paper
3. Whether anyone has already combined conformal prediction with poisoning robustness for RAG
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "754725c7-9cf1-42e2-94bd-29e99216bbdd",
  "isSidechain": false,
  "requestId": "req_011CbYPaYPifC1qo2SGksWqN",
  "type": "assistant",
  "uuid": "d605ffc9-0b11-4685-8a34-7e684e00156e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DhaQ5r72CXV9Hu72Z7MQPE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4567,
      "cache_read_input_tokens": 19324,
      "output_tokens": 268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4567,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 268,
          "cache_read_input_tokens": 19324,
          "cache_creation_input_tokens": 4567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4567
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

_source line 26 · 2026-05-30T07:52:11.060Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HjunHLgwqA4cDHwS1goM2y`</summary>

```json
{
  "query": "Chen 2026 \"conformal factuality\" RAG robust distribution shift arXiv 2603"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d605ffc9-0b11-4685-8a34-7e684e00156e",
  "isSidechain": false,
  "requestId": "req_011CbYPaYPifC1qo2SGksWqN",
  "type": "assistant",
  "uuid": "0e388f0e-9f09-4a44-ab63-7e6fa009a670",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DhaQ5r72CXV9Hu72Z7MQPE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4567,
      "cache_read_input_tokens": 19324,
      "output_tokens": 268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4567,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 268,
          "cache_read_input_tokens": 19324,
          "cache_creation_input_tokens": 4567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4567
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

_source line 27 · 2026-05-30T07:52:11.675Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0181C21H9ocubnBxU3kmfD8i`</summary>

```json
{
  "query": "\"consensus trap\" multi-agent majority voting adversarial 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e388f0e-9f09-4a44-ab63-7e6fa009a670",
  "isSidechain": false,
  "requestId": "req_011CbYPaYPifC1qo2SGksWqN",
  "type": "assistant",
  "uuid": "21f2a789-1d31-4a14-8ec8-8615345a82c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DhaQ5r72CXV9Hu72Z7MQPE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4567,
      "cache_read_input_tokens": 19324,
      "output_tokens": 268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4567,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 268,
          "cache_read_input_tokens": 19324,
          "cache_creation_input_tokens": 4567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4567
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

_source line 28 · 2026-05-30T07:52:12.573Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MGum1C45kxdUwqzgGaK9qm`</summary>

```json
{
  "query": "ReliabilityRAG NLI contradiction detection provably robust NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21f2a789-1d31-4a14-8ec8-8615345a82c9",
  "isSidechain": false,
  "requestId": "req_011CbYPaYPifC1qo2SGksWqN",
  "type": "assistant",
  "uuid": "64f2b25a-4f27-4e21-b326-2f4a0da3670d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DhaQ5r72CXV9Hu72Z7MQPE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4567,
      "cache_read_input_tokens": 19324,
      "output_tokens": 268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4567,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 268,
          "cache_read_input_tokens": 19324,
          "cache_creation_input_tokens": 4567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4567
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

_source line 29 · 2026-05-30T07:52:17.302Z_

<details><summary>↩ Tool result · `toolu_01HjunHLgwqA4cDHwS1goM2y`</summary>

```text
Web search results for query: "Chen 2026 "conformal factuality" RAG robust distribution shift arXiv 2603"

Links: [{"title":"[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/abs/2603.16817"},{"title":"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/pdf/2603.16817"},{"title":"Not all distributional shifts are equal: Fine-grained robust conformal inference","url":"https://arxiv.org/pdf/2402.13042"},{"title":"[2403.15025] Robust Conformal Prediction under Distribution Shift via Physics-Informed Structural Causal Model","url":"https://arxiv.org/abs/2403.15025"},{"title":"URAG: A Benchmark for Uncertainty Quantification in Retrieval-Augmented Large Language Models","url":"https://arxiv.org/html/2603.19281"},{"title":"Proceedings of Machine Learning Research vol vvv:1–25, 2026","url":"https://arxiv.org/pdf/2602.12616"},{"title":"[2603.27403] Conditional Factuality Controlled LLMs with Generalization Certificates via Conformal Sampling","url":"https://arxiv.org/abs/2603.27403"},{"title":"Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/html/2502.14105v2"}]

I found the paper you're looking for! The paper "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights" is by Yi Chen from the University of Wisconsin-Madison, with arXiv ID 2603.16817, submitted on March 17, 2026.

**Key Findings:**

The study finds that conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, conformal factuality guarantees are not robust to distribution shifts and distractors, and lightweight entailment-based verifiers match or outperform LLM-based confidence scorers while requiring over 100× fewer FLOPs.

The results expose factuality-informativeness trade-offs and fragility of the conformal filtering framework under distribution shifts and distractors, highlighting the need for new approaches that prioritize robustness and usefulness as key metrics for building reliable and computationally efficient RAG pipelines.

You can access the paper directly at: https://arxiv.org/abs/2603.16817


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e388f0e-9f09-4a44-ab63-7e6fa009a670",
  "isSidechain": false,
  "promptId": "42f0fa8d-2ab5-4522-bbdc-de8010b9f267",
  "type": "user",
  "uuid": "1351e0d0-3834-42d5-80e5-9d9488ed5b6d",
  "toolUseResult": {
    "query": "Chen 2026 \"conformal factuality\" RAG robust distribution shift arXiv 2603",
    "results": [
      {
        "tool_use_id": "srvtoolu_01J8NWqi6HDiGFRhyEuzaKcC",
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
            "title": "[2403.15025] Robust Conformal Prediction under Distribution Shift via Physics-Informed Structural Causal Model",
            "url": "https://arxiv.org/abs/2403.15025"
          },
          {
            "title": "URAG: A Benchmark for Uncertainty Quantification in Retrieval-Augmented Large Language Models",
            "url": "https://arxiv.org/html/2603.19281"
          },
          {
            "title": "Proceedings of Machine Learning Research vol vvv:1–25, 2026",
            "url": "https://arxiv.org/pdf/2602.12616"
          },
          {
            "title": "[2603.27403] Conditional Factuality Controlled LLMs with Generalization Certificates via Conformal Sampling",
            "url": "https://arxiv.org/abs/2603.27403"
          },
          {
            "title": "Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/html/2502.14105v2"
          }
        ]
      },
      "I found the paper you're looking for! The paper \"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights\" is by Yi Chen from the University of Wisconsin-Madison, with arXiv ID 2603.16817, submitted on March 17, 2026.\n\n**Key Findings:**\n\nThe study finds that conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs, conformal factuality guarantees are not robust to distribution shifts and distractors, and lightweight entailment-based verifiers match or outperform LLM-based confidence scorers while requiring over 100× fewer FLOPs.\n\nThe results expose factuality-informativeness trade-offs and fragility of the conformal filtering framework under distribution shifts and distractors, highlighting the need for new approaches that prioritize robustness and usefulness as key metrics for building reliable and computationally efficient RAG pipelines.\n\nYou can access the paper directly at: https://arxiv.org/abs/2603.16817"
    ],
    "durationSeconds": 6.237272301000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0e388f0e-9f09-4a44-ab63-7e6fa009a670",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-30T07:52:19.979Z_

<details><summary>↩ Tool result · `toolu_0181C21H9ocubnBxU3kmfD8i`</summary>

```text
Web search results for query: ""consensus trap" multi-agent majority voting adversarial 2026"

Links: [{"title":"[2604.17139] The Consensus Trap: Rescuing Multi-Agent LLMs from Adversarial Majorities via Token-Level Collaboration","url":"https://arxiv.org/abs/2604.17139"},{"title":"The Consensus Trap: Rescuing Multi-Agent LLMs from Adversarial Majorities via Token-Level Collaboration","url":"https://arxiv.org/html/2604.17139"},{"title":"The Pass@k Trap: Why Running Your AI Agent 3 Times Makes Answers Worse – TALVINDER","url":"https://talvinder.com/field-notes/consensus-is-not-verification/"},{"title":"Why Consensus Voting Fails for Agent Truthfulness - DEV Community","url":"https://dev.to/talvinder/why-consensus-voting-fails-for-agent-truthfulness-105f"},{"title":"Consensus Protocols for Multi-Agent Systems - 2026 Guide | Fastio","url":"https://fast.io/resources/consensus-protocols-multi-agent-systems/"},{"title":"When collaboration fails: persuasion driven adversarial influence in multi agent large language model debate | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-42705-7"},{"title":"Many-to-One Adversarial Consensus: Exposing Multi-Agent Collusion Risks in AI-Based Healthcare","url":"https://arxiv.org/html/2512.03097v1"}]

Based on the search results, I found several recent papers and articles discussing the consensus trap in multi-agent systems:

## Primary Research Finding

The "Consensus Trap" refers to a critical vulnerability where multi-agent LLM systems relying on response-level aggregation like Majority Voting collapse when corrupted agents form a local majority.

Agents are susceptible to stealthy contextual corruption such as targeted prompt injections, and voting aggregates fully-formed conclusions, making it blind to flawed intermediate logic.

## Proposed Solution

To overcome this limitation, researchers propose Token-Level Round-Robin (RR) Collaboration, where agents sequentially interleave generation within a shared auto-regressive context. Theoretical analysis shows the honest model's restorative pull can overpower adversarial corruptions even when corrupted agents form a majority, and RR maintains robust accuracy well beyond the threshold where majority voting collapses.

## Related Vulnerabilities

Additional research from 2026 identifies related vulnerabilities: In multi-agent debate, cooperative agents tend to agree increasingly with adversarial agents over rounds, with a positive majority converging to the adversary's bad answer. Coordinated collusion among agents could drastically distort decision-making, and instead of converging toward truth, colluding agents can bias the collective outcome.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21f2a789-1d31-4a14-8ec8-8615345a82c9",
  "isSidechain": false,
  "promptId": "42f0fa8d-2ab5-4522-bbdc-de8010b9f267",
  "type": "user",
  "uuid": "cb0f0d7d-3976-4e6d-8a8c-ddd53c1195f8",
  "toolUseResult": {
    "query": "\"consensus trap\" multi-agent majority voting adversarial 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RnnF5Jg7f1GYn6TQrWMRKx",
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
            "title": "The Pass@k Trap: Why Running Your AI Agent 3 Times Makes Answers Worse – TALVINDER",
            "url": "https://talvinder.com/field-notes/consensus-is-not-verification/"
          },
          {
            "title": "Why Consensus Voting Fails for Agent Truthfulness - DEV Community",
            "url": "https://dev.to/talvinder/why-consensus-voting-fails-for-agent-truthfulness-105f"
          },
          {
            "title": "Consensus Protocols for Multi-Agent Systems - 2026 Guide | Fastio",
            "url": "https://fast.io/resources/consensus-protocols-multi-agent-systems/"
          },
          {
            "title": "When collaboration fails: persuasion driven adversarial influence in multi agent large language model debate | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-026-42705-7"
          },
          {
            "title": "Many-to-One Adversarial Consensus: Exposing Multi-Agent Collusion Risks in AI-Based Healthcare",
            "url": "https://arxiv.org/html/2512.03097v1"
          }
        ]
      },
      "Based on the search results, I found several recent papers and articles discussing the consensus trap in multi-agent systems:\n\n## Primary Research Finding\n\nThe \"Consensus Trap\" refers to a critical vulnerability where multi-agent LLM systems relying on response-level aggregation like Majority Voting collapse when corrupted agents form a local majority.\n\nAgents are susceptible to stealthy contextual corruption such as targeted prompt injections, and voting aggregates fully-formed conclusions, making it blind to flawed intermediate logic.\n\n## Proposed Solution\n\nTo overcome this limitation, researchers propose Token-Level Round-Robin (RR) Collaboration, where agents sequentially interleave generation within a shared auto-regressive context. Theoretical analysis shows the honest model's restorative pull can overpower adversarial corruptions even when corrupted agents form a majority, and RR maintains robust accuracy well beyond the threshold where majority voting collapses.\n\n## Related Vulnerabilities\n\nAdditional research from 2026 identifies related vulnerabilities: In multi-agent debate, cooperative agents tend to agree increasingly with adversarial agents over rounds, with a positive majority converging to the adversary's bad answer. Coordinated collusion among agents could drastically distort decision-making, and instead of converging toward truth, colluding agents can bias the collective outcome."
    ],
    "durationSeconds": 8.299695116000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "21f2a789-1d31-4a14-8ec8-8615345a82c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-30T07:52:20.127Z_

<details><summary>↩ Tool result · `toolu_01MGum1C45kxdUwqzgGaK9qm`</summary>

```text
Web search results for query: "ReliabilityRAG NLI contradiction detection provably robust NeurIPS 2025"

Links: [{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/pdf/2509.23519"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://neurips.cc/media/neurips-2025/Slides/119236.pdf"},{"title":"NeurIPS Poster ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://neurips.cc/virtual/2025/poster/119236"},{"title":"NeurIPS 2025 Thursday 12/4","url":"https://neurips.cc/virtual/2025/day/12/4"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search | OpenReview","url":"https://openreview.net/forum?id=D9JeNTs5Bu"},{"title":"LegalWiz: A Multi-Agent Generation Framework for Contradiction Detection in Legal Documents","url":"https://arxiv.org/html/2510.03418v2"},{"title":"[2509.23519] ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/abs/2509.23519"},{"title":"Contradiction Detection in RAG Systems: Evaluating LLMs as Context   Validators for Improved Information Consistency","url":"https://arxiv.org/pdf/2504.00180"},{"title":"With a Little Push, NLI Models can Robustly and Efficiently Predict   Faithfulness","url":"https://arxiv.org/pdf/2305.16819"},{"title":"Using contradictions improves question answering systems","url":"https://arxiv.org/pdf/2211.05598"}]

Based on the search results, I found information about ReliabilityRAG:

## Overview

ReliabilityRAG is a framework for adversarial robustness that explicitly leverages reliability information of retrieved documents. The work was presented at NeurIPS 2025.

## Key Approach

The paper introduces a novel algorithm based on finding a Maximum Independent Set (MIS) on a document graph where edges encode contradiction. The MIS variant explicitly prioritizes higher-reliability documents and provides provable robustness guarantees against bounded adversarial corruption under natural assumptions.

More specifically, the method involves graph construction where each document is a vertex with edges between contradictory documents, uses an NLI model to check contradictions, and finds a maximum independent set in the graph to identify a consistent majority.

## NLI for Contradiction Detection

The document-selection algorithm identifies a "consistent majority" among retrieved documents by finding the Maximum Independent Set on a "contradiction graph," where vertices represent the retrieved documents and edges connect pairs determined to be contradictory by a Natural Language Inference (NLI) model.

## Robustness Guarantees

Theorem 1 provides theoretical validation that ReliabilityRAG via MIS is provably robust since the probability of selecting a malicious document vanishes as the number of retrieved documents k grows large, provided the NLI error rates and the number of malicious documents satisfy specified conditions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64f2b25a-4f27-4e21-b326-2f4a0da3670d",
  "isSidechain": false,
  "promptId": "42f0fa8d-2ab5-4522-bbdc-de8010b9f267",
  "type": "user",
  "uuid": "6b1e1f51-c1ef-40fb-a78d-616c61511e11",
  "toolUseResult": {
    "query": "ReliabilityRAG NLI contradiction detection provably robust NeurIPS 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XdEoMeKpFjRRDRyH5xbeGW",
        "content": [
          {
            "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://arxiv.org/pdf/2509.23519"
          },
          {
            "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://neurips.cc/media/neurips-2025/Slides/119236.pdf"
          },
          {
            "title": "NeurIPS Poster ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://neurips.cc/virtual/2025/poster/119236"
          },
          {
            "title": "NeurIPS 2025 Thursday 12/4",
            "url": "https://neurips.cc/virtual/2025/day/12/4"
          },
          {
            "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search | OpenReview",
            "url": "https://openreview.net/forum?id=D9JeNTs5Bu"
          },
          {
            "title": "LegalWiz: A Multi-Agent Generation Framework for Contradiction Detection in Legal Documents",
            "url": "https://arxiv.org/html/2510.03418v2"
          },
          {
            "title": "[2509.23519] ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
            "url": "https://arxiv.org/abs/2509.23519"
          },
          {
            "title": "Contradiction Detection in RAG Systems: Evaluating LLMs as Context   Validators for Improved Information Consistency",
            "url": "https://arxiv.org/pdf/2504.00180"
          },
          {
            "title": "With a Little Push, NLI Models can Robustly and Efficiently Predict   Faithfulness",
            "url": "https://arxiv.org/pdf/2305.16819"
          },
          {
            "title": "Using contradictions improves question answering systems",
            "url": "https://arxiv.org/pdf/2211.05598"
          }
        ]
      },
      "Based on the search results, I found information about ReliabilityRAG:\n\n## Overview\n\nReliabilityRAG is a framework for adversarial robustness that explicitly leverages reliability information of retrieved documents. The work was presented at NeurIPS 2025.\n\n## Key Approach\n\nThe paper introduces a novel algorithm based on finding a Maximum Independent Set (MIS) on a document graph where edges encode contradiction. The MIS variant explicitly prioritizes higher-reliability documents and provides provable robustness guarantees against bounded adversarial corruption under natural assumptions.\n\nMore specifically, the method involves graph construction where each document is a vertex with edges between contradictory documents, uses an NLI model to check contradictions, and finds a maximum independent set in the graph to identify a consistent majority.\n\n## NLI for Contradiction Detection\n\nThe document-selection algorithm identifies a \"consistent majority\" among retrieved documents by finding the Maximum Independent Set on a \"contradiction graph,\" where vertices represent the retrieved documents and edges connect pairs determined to be contradictory by a Natural Language Inference (NLI) model.\n\n## Robustness Guarantees\n\nTheorem 1 provides theoretical validation that ReliabilityRAG via MIS is provably robust since the probability of selecting a malicious document vanishes as the number of retrieved documents k grows large, provided the NLI error rates and the number of malicious documents satisfy specified conditions."
    ],
    "durationSeconds": 7.551322000999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "64f2b25a-4f27-4e21-b326-2f4a0da3670d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-30T07:52:24.967Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me do a couple more targeted searches to check:
1. Whether there's any existing work that already combines conformal prediction with adversarial robustness for RAG
2. The Lévy-Prokhorov distribution shift conformal prediction paper
3. RAGPart paper details
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b1e1f51-c1ef-40fb-a78d-616c61511e11",
  "isSidechain": false,
  "requestId": "req_011CbYPbfQfvDnzEhcZHArBN",
  "type": "assistant",
  "uuid": "f5674452-d4fe-4d10-8d4e-3a8488429ca8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HPqCA8nPRFJKWBSEQx4LC5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2531,
      "cache_read_input_tokens": 23891,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2531,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 209,
          "cache_read_input_tokens": 23891,
          "cache_creation_input_tokens": 2531,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2531
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

_source line 33 · 2026-05-30T07:52:25.704Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ABFu5D3UnyykF6fXtqgj78`</summary>

```json
{
  "query": "\"conformal prediction\" \"adversarial\" \"abstention\" RAG poisoning robust 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5674452-d4fe-4d10-8d4e-3a8488429ca8",
  "isSidechain": false,
  "requestId": "req_011CbYPbfQfvDnzEhcZHArBN",
  "type": "assistant",
  "uuid": "c3d5f42b-2585-4a94-a11c-906f8847630d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HPqCA8nPRFJKWBSEQx4LC5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2531,
      "cache_read_input_tokens": 23891,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2531,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 209,
          "cache_read_input_tokens": 23891,
          "cache_creation_input_tokens": 2531,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2531
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

_source line 34 · 2026-05-30T07:52:25.917Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Tk3Gem2TQDBMzT2h4Cc8w5`</summary>

```json
{
  "query": "Levy Prokhorov conformal prediction distribution shift arXiv 2502.14105"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3d5f42b-2585-4a94-a11c-906f8847630d",
  "isSidechain": false,
  "requestId": "req_011CbYPbfQfvDnzEhcZHArBN",
  "type": "assistant",
  "uuid": "bb5f41d4-eaf3-46b0-922e-29542ba6b9fe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HPqCA8nPRFJKWBSEQx4LC5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2531,
      "cache_read_input_tokens": 23891,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2531,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 209,
          "cache_read_input_tokens": 23891,
          "cache_creation_input_tokens": 2531,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2531
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

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores  ## Core Problem  RAG systems in ad…",
  "leafUuid": "bb5f41d4-eaf3-46b0-922e-29542ba6b9fe",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Poisoning-robust conformal abstention for RAG systems",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30"
}
```

---

### Tool result

_source line 37 · 2026-05-30T07:52:31.697Z_

<details><summary>↩ Tool result · `toolu_01Tk3Gem2TQDBMzT2h4Cc8w5`</summary>

```text
Web search results for query: "Levy Prokhorov conformal prediction distribution shift arXiv 2502.14105"

Links: [{"title":"[2502.14105] Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/abs/2502.14105"},{"title":"Conformal Prediction under Lévy-Prokhorov Distribution ...","url":"https://arxiv.org/pdf/2502.14105"},{"title":"Conformal Prediction under Lévy-Prokhorov Distribution ...","url":"https://openreview.net/pdf/860efa6f37cc6b64df19821bba75d83edb3b9603.pdf"},{"title":"Conformal Prediction under Lévy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations | OpenReview","url":"https://openreview.net/forum?id=1ULQvdbZ3X"},{"title":"Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/html/2502.14105v2"},{"title":"NeurIPS Poster Conformal Prediction under Lévy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://neurips.cc/virtual/2025/poster/120230"},{"title":"(PDF) Conformal Prediction under L\\'evy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://www.researchgate.net/publication/389176501_Conformal_Prediction_under_L'evy-Prokhorov_Distribution_Shifts_Robustness_to_Local_and_Global_Perturbations"},{"title":"Coverage Guarantees for Pseudo-Calibrated Conformal Prediction under Distribution Shift","url":"https://arxiv.org/html/2602.14913"},{"title":"Computer Science Feb 2025","url":"https://www.arxiv.org/list/cs/2025-02?skip=11400&show=1000"}]

Based on the search results, here's what I found about arXiv paper 2502.14105:

**Title:** Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations

**Authors:** Liviu Aolaritei, Zheyu Oliver Wang, Julie Zhu, Michael I. Jordan, Youssef Marzouk

**Main Contribution:** The paper addresses distribution shift limitations by modeling distribution shifts using Levy-Prokhorov (LP) ambiguity sets, which capture both local and global perturbations.

**Key Technical Approach:** By propagating the LP ambiguity set through the scoring function, the authors reduce complex high-dimensional distribution shifts to manageable one-dimensional distribution shifts, enabling exact quantification of worst-case quantiles and coverage.

**Related Metrics:** The paper provides an overview of LP ambiguity sets and their connections to popular metrics such as Wasserstein and Total Variation.

**Publication Status:** The paper was submitted on February 19, 2025, with a revised version on May 19, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb5f41d4-eaf3-46b0-922e-29542ba6b9fe",
  "isSidechain": false,
  "promptId": "42f0fa8d-2ab5-4522-bbdc-de8010b9f267",
  "type": "user",
  "uuid": "69d54c86-839a-472f-bf4a-a34d94183dfc",
  "toolUseResult": {
    "query": "Levy Prokhorov conformal prediction distribution shift arXiv 2502.14105",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WLHecT5UDeyQuNircXUKBu",
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
            "title": "Conformal Prediction under Lévy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations | OpenReview",
            "url": "https://openreview.net/forum?id=1ULQvdbZ3X"
          },
          {
            "title": "Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/html/2502.14105v2"
          },
          {
            "title": "NeurIPS Poster Conformal Prediction under Lévy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://neurips.cc/virtual/2025/poster/120230"
          },
          {
            "title": "(PDF) Conformal Prediction under L\\'evy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://www.researchgate.net/publication/389176501_Conformal_Prediction_under_L'evy-Prokhorov_Distribution_Shifts_Robustness_to_Local_and_Global_Perturbations"
          },
          {
            "title": "Coverage Guarantees for Pseudo-Calibrated Conformal Prediction under Distribution Shift",
            "url": "https://arxiv.org/html/2602.14913"
          },
          {
            "title": "Computer Science Feb 2025",
            "url": "https://www.arxiv.org/list/cs/2025-02?skip=11400&show=1000"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2502.14105:\n\n**Title:** Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations\n\n**Authors:** Liviu Aolaritei, Zheyu Oliver Wang, Julie Zhu, Michael I. Jordan, Youssef Marzouk\n\n**Main Contribution:** The paper addresses distribution shift limitations by modeling distribution shifts using Levy-Prokhorov (LP) ambiguity sets, which capture both local and global perturbations.\n\n**Key Technical Approach:** By propagating the LP ambiguity set through the scoring function, the authors reduce complex high-dimensional distribution shifts to manageable one-dimensional distribution shifts, enabling exact quantification of worst-case quantiles and coverage.\n\n**Related Metrics:** The paper provides an overview of LP ambiguity sets and their connections to popular metrics such as Wasserstein and Total Variation.\n\n**Publication Status:** The paper was submitted on February 19, 2025, with a revised version on May 19, 2025."
    ],
    "durationSeconds": 5.7768872679999985,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bb5f41d4-eaf3-46b0-922e-29542ba6b9fe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-30T07:52:34.334Z_

<details><summary>↩ Tool result · `toolu_01ABFu5D3UnyykF6fXtqgj78`</summary>

```text
Web search results for query: ""conformal prediction" "adversarial" "abstention" RAG poisoning robust 2025 2026"

Links: [{"title":"Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0031320325007113"},{"title":"Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks | Request PDF","url":"https://www.researchgate.net/publication/393421882_Verifiably_robust_conformal_prediction_for_probabilistic_guarantees_under_adversarial_attacks"},{"title":"Verifiably robust conformal prediction for probabilistic guarantees under adversarial attacks - King's College London","url":"https://kclpure.kcl.ac.uk/portal/en/publications/verifiably-robust-conformal-prediction-for-probabilistic-guarante"},{"title":"Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks","url":"https://arxiv.org/html/2412.16708v2"},{"title":"Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks","url":"https://arxiv.org/pdf/2412.16708"},{"title":"Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://arxiv.org/html/2506.07804v1"},{"title":"provably reliable conformal prediction sets","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4d21a4b33361c40c2142db9511c126-Paper-Conference.pdf"},{"title":"GitHub - Arstanley/Awesome-Trustworthy-RAG · GitHub","url":"https://github.com/Arstanley/Awesome-Trustworthy-RAG"},{"title":"Robust Yet Efficient Conformal Prediction Sets","url":"https://arxiv.org/pdf/2407.09165"}]

Based on the web search results, I found several relevant recent papers and research on these interconnected topics:

## Conformal Prediction and Adversarial Robustness

Recent research presents Verifiably Robust Conformal Prediction (VRCP), which recovers conformal prediction's probabilistic guarantees under adversarial attacks by combining CP with neural network verification. VRCP is also automatically robust to feature poisoning attacks. This work was published in Pattern Recognition, Vol. 170 in February 2026.

Conformal Prediction has emerged as a promising paradigm for adversarial robustness, distinguished by its distribution-free properties and robust uncertainty quantification capabilities, excelling in both regression and classification tasks by providing statistically rigorous confidence intervals and well-calibrated probability estimates.

## Conformal Prediction Under Data Poisoning

Recent work addresses robustness certification where adversaries can modify, add or remove datapoints from both training and calibration data, focusing on data poisoning robustness. Most existing work only certifies coverage guarantee under calibration poisoning.

## RAG and Adversarial Poisoning

RAG systems combine LLMs with external knowledge to reduce hallucinations, but are vulnerable to adversarial poisoning attacks where attackers inject adversarial data into the RAG database to manipulate retrieval and reduce model accuracy. Abstention is the proportion that LLMs didn't answer.

The search results show active research in 2025-2026 on combining conformal prediction with adversarial robustness, poisoning attacks on RAG systems, and mechanisms like abstention for improving system reliability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3d5f42b-2585-4a94-a11c-906f8847630d",
  "isSidechain": false,
  "promptId": "42f0fa8d-2ab5-4522-bbdc-de8010b9f267",
  "type": "user",
  "uuid": "cf1d2360-f21d-49be-8412-e4aab211c30e",
  "toolUseResult": {
    "query": "\"conformal prediction\" \"adversarial\" \"abstention\" RAG poisoning robust 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AJs9bGJhE65TSgM5nF3A1v",
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
            "title": "Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks",
            "url": "https://arxiv.org/html/2412.16708v2"
          },
          {
            "title": "Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks",
            "url": "https://arxiv.org/pdf/2412.16708"
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
            "title": "GitHub - Arstanley/Awesome-Trustworthy-RAG · GitHub",
            "url": "https://github.com/Arstanley/Awesome-Trustworthy-RAG"
          },
          {
            "title": "Robust Yet Efficient Conformal Prediction Sets",
            "url": "https://arxiv.org/pdf/2407.09165"
          }
        ]
      },
      "Based on the web search results, I found several relevant recent papers and research on these interconnected topics:\n\n## Conformal Prediction and Adversarial Robustness\n\nRecent research presents Verifiably Robust Conformal Prediction (VRCP), which recovers conformal prediction's probabilistic guarantees under adversarial attacks by combining CP with neural network verification. VRCP is also automatically robust to feature poisoning attacks. This work was published in Pattern Recognition, Vol. 170 in February 2026.\n\nConformal Prediction has emerged as a promising paradigm for adversarial robustness, distinguished by its distribution-free properties and robust uncertainty quantification capabilities, excelling in both regression and classification tasks by providing statistically rigorous confidence intervals and well-calibrated probability estimates.\n\n## Conformal Prediction Under Data Poisoning\n\nRecent work addresses robustness certification where adversaries can modify, add or remove datapoints from both training and calibration data, focusing on data poisoning robustness. Most existing work only certifies coverage guarantee under calibration poisoning.\n\n## RAG and Adversarial Poisoning\n\nRAG systems combine LLMs with external knowledge to reduce hallucinations, but are vulnerable to adversarial poisoning attacks where attackers inject adversarial data into the RAG database to manipulate retrieval and reduce model accuracy. Abstention is the proportion that LLMs didn't answer.\n\nThe search results show active research in 2025-2026 on combining conformal prediction with adversarial robustness, poisoning attacks on RAG systems, and mechanisms like abstention for improving system reliability."
    ],
    "durationSeconds": 8.626251108000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c3d5f42b-2585-4a94-a11c-906f8847630d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 39 · 2026-05-30T07:52:34.340Z_

```json
{
  "parentUuid": "cf1d2360-f21d-49be-8412-e4aab211c30e",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "a12f5e15-f23b-4784-a86e-9a16fc111058",
  "timestamp": "2026-05-30T07:52:34.340Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 40 · 2026-05-30T07:53:17.749Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have sufficient information to do a thorough evaluation. Let me compile my findings and provide the assessment.

Key findings from my research:

1. **Conformal Prediction for RAG**: TRAQ (NAACL 2024), C-RAG (ICML 2024), Conformal-RAG (SIGIR 2025) are all real and established. Chen et al. (arXiv:2603.16817, March 2026) showed that conformal factuality for RAG is not robust to distribution shifts - this is confirmed.

2. **Certified RAG Defenses**: RobustRAG (SaTML 2026) uses isolate-then-aggregate strategy. ReliabilityRAG (NeurIPS 2025) uses MIS on contradiction graphs with NLI. 

Both deliver reliable point estimates but lack any way to abstain on uncertain predictions.

3. **Poisoning-Robust CP**: RPS (ICLR 2025 Spotlight) handles calibration-set poisoning but doesn't address test-time retrieval corruption, which represents a genuine gap.

4. **LP-shift CP**: arXiv:2502.14105 reduces high-dimensional distribution shifts to 1D via LP ambiguity sets. The parallel cited by PRCA is legitimate.

5. **No existing work combines conformal abstention with retrieval-poisoning robustness** - the gap identified by the proposal appears genuine.

6. **The Consensus Trap** (arXiv:2604.17139) is confirmed as showing how majority voting breaks down under adversarial majorities.

Now evaluating the proposal itself: it correctly identifies a genuine gap where no existing method provides distribution-free abstention guarantees for RAG under adversarial retrieval corruption. The partition-induced reduction from high-dimensional adversarial corruption to 1D bounded TV shift is elegant and well-motivated, with valid connections to the LP-shift framework. The proposal demonstrates deep knowledge of the field, positioning itself against TRAQ, C-RAG, RobustRAG, ReliabilityRAG, RPS, and RAGPart, and the three alternatives that fail are well-argued and non-trivial. The experimental design appears extremely thorough.

The main concerns are whether the worst-case TV bound is tight enough to avoid excessive abstention in practice, and whether DeBERTa-v3-large NLI remains reliable when adversarial passages produce semantically similar but incorrect answers—though the proposal acknowledges both issues and plans diagnostic experiments to address them.

Beyond these, partitioning reduces passages per group which will hurt clean accuracy, the adaptive attack strategy needs more specifics on how attackers would optimize poisoned passages across groups, the clean calibration assumption may not hold in truly adversarial settings, random partitioning might be suboptimal compared to other strategies, and K independent LLM calls with NLI comparisons could become computationally expensive at scale.

Overall this is a strong proposal with a genuine gap and theoretically grounded approach, though the main practical risks center on bound tightness, NLI reliability under adversarial conditions, and the clean accuracy-robustness tradeoff.

For AAAI 2026, I'm estimating around 35-45% acceptance probability—the work is novel at the intersection of conformal prediction and RAG security with solid experimental design, but success hinges on whether the theoretical guarantees actually deliver practical utility and whether the execution addresses these open questions. clean ✓
- The experimental design is very thorough ✓
- There are legitimate technical risks (TV bound tightness, NLI reliability) that could lead to weak empirical results
- The proposal is quite incremental in the sense that it's combining existing techniques (partition + CRC + NLI) in a new way, rather than introducing fundamentally new techniques
- But the combination is non-trivial and well-motivated

Actually, let me reconsider. This proposal:
1. Has a clear and genuine research gap ✓
2. Has a theoretically clean contribution ✓
3. Has comprehensive experimental design ✓
4. Has strong positioning against alternatives ✓
5. Is highly relevant and timely ✓

The weaknesses are manageable and acknowledged. I think 33-45% with median around 38% is fair. It's a solid submission that could go either way depending on reviewer assignment and execution.

Since this is a proposal rather than a finished paper, I need to weigh both the idea quality and the execution risk—but given how well-thought-out the plan is, I'm comfortable with my estimate.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a12f5e15-f23b-4784-a86e-9a16fc111058",
  "isSidechain": false,
  "requestId": "req_011CbYPciCss8g8xfFYGKZ19",
  "type": "assistant",
  "uuid": "0fb16157-20e6-4091-b4a7-b067aa36b15f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KmU7QML2NBqzAVPsbUAvq7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 846,
      "cache_creation_input_tokens": 1243,
      "cache_read_input_tokens": 26422,
      "output_tokens": 6376,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1243,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 846,
          "output_tokens": 6376,
          "cache_read_input_tokens": 26422,
          "cache_creation_input_tokens": 1243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1243
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

_source line 41 · 2026-05-30T07:55:01.610Z_

Now I have enough information from my research to provide a thorough evaluation. Let me compile the assessment.

---

```
【阶段】: Triage

【领域调研】:
- [TRAQ: Trustworthy Retrieval Augmented QA via Conformal Prediction](https://arxiv.org/pdf/2307.04642) (NAACL 2024): 开创性地将 conformal prediction 引入 RAG，但假设良性检索环境。PRCA 的直接前驱。
- [C-RAG: Certified Generation Risks for RAG](https://arxiv.org/abs/2402.12888) (ICML 2024): 为 RAG 提供 certified 生成风险控制，同样假设 benign retrieval。
- [Conformal-RAG / Response Quality Assessment via Conditional Conformal Factuality](https://arxiv.org/abs/2506.20978) (SIGIR 2025): 扩展至 group-conditional coverage，仍无对抗鲁棒性。
- [Is Conformal Factuality for RAG-based LLMs Robust?](https://arxiv.org/abs/2603.16817) (arXiv Mar 2026): **关键论文**——直接证明了 TRAQ/C-RAG 等方法在 distribution shift 和 retrieval corruption 下产生 vacuous 输出，但未提出解决方案。**验证了 PRCA 所识别的 gap 的真实性。**
- [RobustRAG: Certifiably Robust RAG against Retrieval Corruption](https://arxiv.org/abs/2405.15556) (SaTML 2026): 使用 isolate-then-aggregate 策略，71% clean accuracy / 38% certified robust accuracy (RealtimeQA)。提供鲁棒点估计但**无 abstention 机制或 coverage certificate**。PRCA 的主要对比目标。
- [ReliabilityRAG](https://arxiv.org/abs/2509.23519) (NeurIPS 2025): 基于 NLI 矛盾检测构建文档图，通过 MIS 实现可证明鲁棒的文档过滤。同样仅提供鲁棒点估计。
- [RPS: Provably Reliable Conformal Prediction Sets under Data Poisoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4d21a4b33361c40c2142db9511c126-Paper-Conference.pdf) (ICLR 2025 Spotlight): 首个 poisoning-robust CP 方法，但针对**校准集污染**，无法直接处理 test-time retrieval corruption。
- [RAGPart & RAGMask](https://arxiv.org/pdf/2512.24268) (arXiv Dec 2025): 在 retrieval 阶段使用文档分区稀释 poisoning，但无 conformal 保证。与 PRCA 互补。
- [Conformal Prediction under LP Distribution Shifts](https://arxiv.org/abs/2502.14105) (arXiv Feb 2025 / NeurIPS 2025 poster): 将高维分布偏移归约到一维 score 偏移，PRCA 的 partition-induced TV bound 是其在对抗检索场景下的特定实例化。
- [The Consensus Trap](https://arxiv.org/abs/2604.17139) (arXiv Apr 2026): 证明 response-level majority voting 在对抗多数下失效。PRCA 需要面对此风险，但其主要保证是 abstention 决策而非 majority answer 本身。
- [Verifiably Robust Conformal Prediction](https://www.sciencedirect.com/science/article/pii/S0031320325007113) (Pattern Recognition 2026): 结合 CP 与神经网络验证实现对抗鲁棒 CP，但不针对 RAG 场景。

- **调研总结**: Conformal prediction for RAG 和 certified RAG defense 是两条活跃但**完全独立**的研究线。经充分检索，**无任何已发表工作**将 conformal abstention 与 retrieval-poisoning robustness 结合。Chen et al. (Mar 2026) 明确指出了 conformal RAG 在对抗环境下的脆弱性但未提供解决方案，这恰好是 PRCA 所填补的 gap。该 gap 是**真实且尚未被占领的**。

【整体印象】:
这是一篇**立意精准、理论清晰、实验设计完备**的 proposal。作为审稿人，我的第一反应是 **weak accept 倾向**。原因：(1) 研究 gap 经验证是真实的——两条成熟研究线（conformal CP for RAG + certified RAG defense）之间确实无人桥接；(2) 核心理论贡献——partition-induced reduction 将不可刻画的高维对抗扰动归约为有界一维 TV shift——是干净且非平凡的；(3) 实验设计在 proposal 阶段已经非常完整，8 个 baselines、4 种攻击（含 adaptive attack）、完整 ablation、diagnostic experiments，这在 proposal 中属于罕见的详尽程度。主要顾虑在于 TV bound 可能过松导致 excessive abstention，以及 NLI 在对抗条件下的可靠性尚需验证。

【核心贡献】:
PRCA 的核心贡献是一个**理论归约机制**：通过将检索到的 passages 分区为不相交组并计算组间一致性，将任意 test-time retrieval corruption 确定性地归约为 nonconformity score 分布上的有界 TV 偏移，进而被 CRC 通过膨胀分位数吸收，产生形式化的 coverage certificates。这一 "from high-dimensional adversarial corruption to 1D bounded distributional shift" 的归约填补了 conformal RAG 与 certified RAG defense 之间的空白。对领域的价值是**中高**——它为高风险 RAG 应用（医疗、法律、金融）提供了首个分布无关的、在对抗检索下仍有效的 abstention 保证。

【方法合理性】:
方法在理论上是合理的。核心逻辑链——partition → bounded corruption per group → bounded TV in score → CRC absorption——每一步都有坚实的理论基础。Proposal 出色地论证了三种更简单的替代方案（RobustRAG+CP、full-context self-consistency+CP、logprob+CP）为何失败，这表明 partition 不是可有可无的设计选择而是理论必要性。

潜在简单替代：最接近的简单替代方案是 "RobustRAG + TRAQ"（naive pipeline），proposal 已明确将其列为 baseline 并从理论上论证了其失效原因（exchangeability 被破坏且偏移量无法刻画）。这显示作者对方法空间有全面理解。

合理性风险：(1) TV ≤ m/K 是组合上界，实际 TV 可能远小于此，导致过度保守；(2) NLI-based agreement score 对语义相似但事实错误的答案可能不够敏感（Semantic Illusion 风险）；(3) partition 减少了每组的 passage 数量，可能显著降低 clean accuracy。Proposal 均已识别这些风险并设计了对应的 diagnostic experiments。

【5 维度打分】:
  1. 研究问题: 【强】— 问题定义精准，gap 经调研验证为真实且尚未被占领。Chen et al. (Mar 2026) 的发现为这一问题提供了直接的实证动机。高风险 RAG 场景（医疗 QA、法律检索）的实际需求使问题具有显著的现实意义。
  
  2. 方法与创新: 【中-强】— Partition-induced TV reduction 是一个干净的理论贡献，与 LP-shift framework (arXiv:2502.14105) 形成自然的理论关联。创新不在于发明全新的技术组件（partition 来自 RobustRAG，NLI 来自 ReliabilityRAG，CRC 是已有框架），而在于**非平凡地组合它们并提供新的理论保证**。与 RobustRAG 的关键差异（RobustRAG 的聚合改变输出分布使 CP 失效，PRCA 显式界定 TV shift）论证充分。扣分点：组合式创新在顶会中可能被部分审稿人视为增量性工作。
  
  3. 实验设计: 【强】— 这是 proposal 的一大亮点。8 个精心选择的 baselines 涵盖了三类竞争方法（conformal、certified defense、partition-based），且包含了关键的 ablation baseline（RAGPart 无 conformal、RobustRAG+TRAQ naive pipeline）。4 种攻击方法含 adaptive attack（agreement-aware），完整 ablation matrix（K, n, score function, calibration, partition strategy），以及针对 NLI reliability 和 TV bound tightness 的 diagnostic experiments。这在 proposal 阶段已经达到甚至超过了领域标准。与 RobustRAG (SaTML 2026) 和 PoisonedRAG (USENIX Security 2025) 所使用的 NQ/HotpotQA/MS-MARCO 实验标准对齐。
  
  4. 可行性: 【中-强】— 方法的每个组件（passage partition、isolated LLM generation、NLI entailment、CRC calibration）都是成熟技术，工程实现风险低。主要可行性风险：(a) K 次独立 LLM 调用带来的计算开销（已在 metrics 中包含效率评估）；(b) 对 72B 模型的实验规模可能需要较大计算资源；(c) adaptive attack 的实现需要对 NLI score 的可微性做假设。总体可行，但完整实验需要相当的计算预算。
  
  5. 写作与呈现: 【强】— Proposal 的逻辑结构非常清晰：problem → gap → why naive alternatives fail → proposed method → theoretical insight → experimental design。对每个相关工作的定位准确且有区分度。"Why not simply combine existing methods?" 一节是出色的学术写作——预判了审稿人最可能提出的质疑并系统性地回答。术语使用精确，无模糊或过度声称。

【概率估计】: [30% - 45%] 中位 38%

【估计理由】:
- **上行因素**: (1) 研究 gap 真实且尚无竞争者；(2) 理论贡献清晰（partition-induced TV reduction）；(3) 实验设计在 proposal 阶段已近乎完备；(4) 主题高度时效——RAG 安全与可靠性是 2025-2026 的热点方向；(5) 写作质量高，论证体系完整。
- **下行因素**: (1) 核心创新是组合式创新（partition from RobustRAG + NLI from ReliabilityRAG + CRC），部分审稿人可能认为增量性；(2) TV ≤ m/K bound 可能过松，导致实际 coverage-abstention tradeoff 不理想——如果实验中 abstention rate 过高（>50%），方法的实用性将大打折扣；(3) NLI 在对抗条件下的可靠性是已知问题（Semantic Illusion, arXiv:2512.15068），若 diagnostic experiments 显示 NLI 不可靠则方法根基动摇；(4) AAAI 竞争激烈（接收率~20%），组合式工作需要特别强的实验结果来脱颖而出。
- **中位 38% 的推理**: 这是一篇 solid 的投稿——问题好、方法合理、实验完备——但还不是那种让审稿人兴奋到给 strong accept 的工作。在 AAAI ~20% 接收率下，它大概率落在 borderline 区域，最终结果取决于：(a) 实验是否能展示实用的 coverage-abstention tradeoff；(b) 审稿人对组合式创新的接受度；(c) reviewer 分配的运气因素。

【主要风险】:
1. **TV bound 过松导致方法不实用**: 如果 TV ≤ m/K 过于保守，膨胀后的分位数阈值会导致 excessive abstention（>50% queries 被拒绝回答），审稿人会质疑方法的实际价值——"一个拒绝回答一半问题的系统真的有用吗？"
2. **组合式创新被认为增量**: 核心组件（partition、NLI agreement、CRC）均非原创，主要贡献在于组合方式和理论分析。若实验结果不够亮眼（如 certified coverage 仅比 naive pipeline 高几个百分点），审稿人可能判定贡献不足以达到 AAAI 标准。

【实施评估】:
  - 计算资源: 中高。需要对 7B/32B/72B 三个规模模型做 K 次独立推理（K∈{1,3,5,7,10}），加上 C(K,2) 次 NLI 推理。完整实验（3 个 primary datasets × 4 种攻击 × 多种 K/n 配置 × 3 个模型规模）估计需要 4-8 张 A100 运行 2-4 周。72B 模型的实验尤其资源密集。
  - 数据需求: 低-中。NQ、HotpotQA、MS-MARCO、PubMedQA 均为公开数据集。需要使用 PoisonedRAG/CorruptRAG 的攻击工具生成 poisoned corpus，工具应公开可用。校准集需 ≥500 样本/数据集，从 clean data 中划分。
  - 人工介入: 低。主要工程工作在于搭建 pipeline（partition → generation → NLI → CRC calibration → abstention）和实现 baseline 方法。Adaptive attack 的实现可能需要一些手工设计。
  - 训练需求: 无需训练新模型。所有组件（LLM、DeBERTa NLI）使用现有预训练模型。
  - 新 Benchmark: 否。使用现有标准 benchmark + 现有攻击工具。
  - 预估周期: 10-14 周。分解为：环境搭建与 baseline 复现（2-3 周）→ 核心方法实现与调试（2-3 周）→ 7B 全量实验含 ablation（3-4 周）→ 32B/72B core 实验（2-3 周）→ 论文撰写（2-3 周，可部分并行）。
```

Sources:
- [TRAQ: Trustworthy Retrieval Augmented QA via Conformal Prediction](https://arxiv.org/pdf/2307.04642)
- [Conformal-RAG (SIGIR 2025)](https://arxiv.org/abs/2506.20978)
- [Is Conformal Factuality for RAG-based LLMs Robust? (Chen et al., Mar 2026)](https://arxiv.org/abs/2603.16817)
- [RobustRAG: Certifiably Robust RAG against Retrieval Corruption](https://arxiv.org/abs/2405.15556)
- [ReliabilityRAG (NeurIPS 2025)](https://arxiv.org/abs/2509.23519)
- [RPS: Provably Reliable Conformal Prediction Sets (ICLR 2025 Spotlight)](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c4d21a4b33361c40c2142db9511c126-Paper-Conference.pdf)
- [RAGPart & RAGMask](https://arxiv.org/pdf/2512.24268)
- [Conformal Prediction under LP Distribution Shifts](https://arxiv.org/abs/2502.14105)
- [The Consensus Trap](https://arxiv.org/abs/2604.17139)
- [Verifiably Robust Conformal Prediction (Pattern Recognition 2026)](https://www.sciencedirect.com/science/article/pii/S0031320325007113)
- [Certified Defenses for RAG Systems (Emergent Mind)](https://www.emergentmind.com/topics/certified-defenses-for-rag-systems)
- [RAG Poisoning: Threats and Defenses (Emergent Mind)](https://www.emergentmind.com/topics/retrieval-augmented-generation-rag-poisoning)
- [Semantic Chameleon (arXiv Mar 2026)](https://arxiv.org/pdf/2603.18034)
- [Conformal Risk Control (ICLR 2024)](https://arxiv.org/abs/2208.02814)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fb16157-20e6-4091-b4a7-b067aa36b15f",
  "isSidechain": false,
  "requestId": "req_011CbYPciCss8g8xfFYGKZ19",
  "type": "assistant",
  "uuid": "a32a7719-5a75-4608-bcd7-7006885ef8fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KmU7QML2NBqzAVPsbUAvq7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 846,
      "cache_creation_input_tokens": 1243,
      "cache_read_input_tokens": 26422,
      "output_tokens": 6376,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1243,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 846,
          "output_tokens": 6376,
          "cache_read_input_tokens": 26422,
          "cache_creation_input_tokens": 1243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1243
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
  "leafUuid": "a32a7719-5a75-4608-bcd7-7006885ef8fd",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Poisoning-robust conformal abstention for RAG systems",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores  ## Core Problem  RAG systems in ad…",
  "leafUuid": "a32a7719-5a75-4608-bcd7-7006885ef8fd",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Poisoning-robust conformal abstention for RAG systems",
  "sessionId": "bb91195a-8912-4b30-ae4d-3bedeba4fa30"
}
```

---
