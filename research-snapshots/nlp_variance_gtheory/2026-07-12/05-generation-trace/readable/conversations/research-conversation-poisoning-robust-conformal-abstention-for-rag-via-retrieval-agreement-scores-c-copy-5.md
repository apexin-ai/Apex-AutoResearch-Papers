# Research conversation: Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores ## Core Problem RAG systems in adversarial 

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-3/d030526f-3fa5-4808-bdfe-56665260e1cf.jsonl`
- **Structured JSON:** [`9c06bcd334a733494241.json`](../../sessions/9c/9c06bcd334a733494241.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T07:34:52.296Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T07:34:52.296Z",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
  "content": "# Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores\n\n## Core Problem\n\nRAG systems in adversarial environments (medical QA, legal retrieval, financial compliance) need distribution-free abstention guarantees when the retrieval corpus is poisoned. Corpus poisoning is a practical threat: CorruptRAG (arXiv 2025) achieves high attack success with a single injected document; PoisonedRAG (USENIX Security 2025) reaches 90%+ ASR with 5 documents. Existing conformal prediction methods for RAG (TRAQ, NAACL 2024; C-RAG, ICML 2024; Conformal-RAG, SIGIR 2025) assume benign retrieval—Chen et al. (arXiv:2603.16817, Mar 2026) demonstrated these guarantees break under distribution shift, producing vacuous outputs. Poisoning-robust CP (RPS, ICLR 2025 Spotlight) addresses calibration-set poisoning, not test-time retrieval corruption. Certified RAG defenses (RobustRAG, SaTML 2026; ReliabilityRAG, NeurIPS 2025) provide robust point estimates but no abstention mechanism or coverage certificates. The gap: no method provides distribution-free abstention guarantees for RAG under adversarial retrieval corruption.\n\n## Core Contribution and Theoretical Insight\n\nPRCA's central contribution is a **partition-induced reduction**: partitioning retrieved passages into disjoint groups and computing inter-group agreement deterministically reduces arbitrary test-time retrieval corruption to a bounded TV shift in the one-dimensional nonconformity score distribution. This bounded shift is absorbed by CRC (ICLR 2024) via inflated quantiles, yielding formal coverage certificates. This reduction—from high-dimensional adversarial corruption to one-dimensional bounded distributional shift—parallels the approach of Conformal Prediction under Lévy-Prokhorov Distribution Shifts (arXiv:2502.14105), which reduces high-dimensional shifts to one-dimensional score shifts via ambiguity sets.\n\n**Why not simply combine existing methods?** Three natural alternatives fail:\n\n(1) **RobustRAG + standard CP**: Running RobustRAG's isolate-then-aggregate to obtain a robust answer, then applying TRAQ/C-RAG for conformal abstention, fails because RobustRAG's aggregation transforms the output distribution in a poisoning-dependent manner. Nonconformity scores from clean calibration are no longer exchangeable with test-time scores under attack, and the magnitude of distributional shift is uncharacterized. PRCA explicitly bounds this shift via partition structure.\n\n(2) **Full-context self-consistency + CP**: Generating K answers from the same full retrieval set and using agreement as a conformal score (the approach of Conformal Abstention, arXiv:2405.01563) fails under poisoning because all K samples share the same poisoned context. The model may produce consistently wrong answers with high agreement, making the score blind to corruption. Partition isolates poisoned passages into a bounded number of groups, enabling detection.\n\n(3) **Logprob-based confidence + CP**: Using LLM token-level logprobabilities as nonconformity scores fails because adversarially crafted passages (e.g., via Semantic Chameleon's gradient-guided attacks, arXiv Mar 2026) are designed to appear authoritative, inflating model confidence on wrong answers. Logprob monotonicity with respect to correctness breaks under adversarial retrieval.\n\n**Partition is a theoretical necessity, not a design choice**: it is the structural mechanism that transforms uncharacterizable adversarial corruption into a bounded, quantifiable distributional shift that CRC can absorb.\n\n## Research Landscape\n\n**Conformal prediction for RAG:** TRAQ (NAACL 2024) and C-RAG (ICML 2024) established conformal prediction for RAG under benign retrieval. Conformal-RAG (SIGIR 2025) extends to group-conditional coverage. Chen et al. (arXiv:2603.16817, Mar 2026) showed all such methods produce vacuous prediction sets under distribution shift and retrieval corruption, but proposed no solution.\n\n**Certified RAG defenses:** RobustRAG (SaTML 2026) provides certified defense via isolate-then-aggregate, achieving certified robust accuracy on RealtimeQA/NQ. ReliabilityRAG (NeurIPS 2025) uses graph-theoretic MIS with NLI-based contradiction detection for provably robust document filtering. Both provide robust point estimates but no coverage certificates or abstention mechanism.\n\n**Poisoning-robust CP:** RPS (ICLR 2025 Spotlight) achieves poisoning-robust CP via smoothed scores and majority voting but assumes calibration-set poisoning—certificates do not transfer to test-time retrieval corruption.\n\n**Partition-based defenses:** RAGPart (arXiv:2512.24268, Dec 2025) uses document partitioning at the retrieval stage (fragment embeddings) to dilute poisoning. Three key differences from PRCA: (1) RAGPart operates at retrieval/embedding stage, PRCA at generation/calibration stage; (2) RAGPart outputs filtered retrieval sets, PRCA outputs {answer, abstain} decisions with coverage certificates; (3) they are complementary—RAGPart can preprocess retrieval before PRCA's certified abstention.\n\n**Adversarial aggregation:** The Consensus Trap (arXiv:2604.17139, Apr 2026) proves response-level majority voting fails when corrupted agents form a local majority. PRCA's majority answer output could face this risk, but: (a) PRCA's primary guarantee is the coverage certificate on the abstention decision, not the majority answer's correctness; (b) under the standard threat model k < n/2, the number of corrupted groups m = ceil(k/floor(n/K)) < K/2, so the honest majority is preserved.\n\n**Attack landscape:** PoisonedRAG (USENIX Security 2025), CorruptRAG (arXiv 2025), RSB Benchmark (May 2025, 13 attack methods × 7 defenses), Semantic Chameleon (arXiv Mar 2026, gradient-guided corpus-dependent attacks).\n\n**Distribution-shift-robust CP:** LP-shift framework (arXiv:2502.14105) reduces high-dimensional shifts to one-dimensional score shifts. PRCA's partition-induced TV bound is a specific instantiation for adversarial retrieval corruption.\n\nNo existing work combines conformal abstention with retrieval-poisoning robustness.\n\n## Proposed Approach\n\n**Step 1: Partition-and-Generate.** Partition top-n retrieved passages into K disjoint groups (random assignment). Generate a per-group answer via isolated LLM calls.\n\n**Step 2: Agreement Nonconformity Score.** For each group pair (i, j), compute NLI entailment probability e(i,j) = P(answer_i entails answer_j) using DeBERTa-v3-large (following ReliabilityRAG's NLI approach). Define:\n\ns = 1 − mean({e(i,j)} over all pairs)\n\nCritical properties: (1) **Monotonicity**: s increases with disagreement; higher s → more likely to abstain, satisfying CRC's monotone-loss requirement. (2) **Corruption-boundedness**: under k-poisoning, at most m = ceil(k/floor(n/K)) groups are corrupted, affecting at most m(K−1) of C(K,2) pairwise comparisons, yielding bounded perturbation to s.\n\n**Toward tighter bounds:** The worst-case TV ≤ m/K is a combinatorial upper bound. Because s is a mean of bounded pairwise scores, the actual perturbation from m corrupted groups may be dampened. We will empirically estimate the actual TV distance between clean and poisoned score CDFs (via bootstrap) and compare against the theoretical bound, reporting the tightness ratio. Exploring concentration-based bounds (leveraging the mean structure) is a concrete research direction.\n\n**Clean-condition variance mitigation:** If different passage groups cover different answer facets, clean-condition agreement variance inflates s and may cause excessive abstention. NLI-based semantic entailment (rather than exact match) is robust to surface variation. Calibration on clean data naturally accounts for residual clean-condition variance in the score distribution.\n\n**Step 3: TV-Bounded Calibration.** Under k-poisoning with K groups, corruption bound m determines maximal TV distance: TV ≤ m/K. Using CRC (ICLR 2024) with TV-inflated quantile: set abstention threshold at the (1 − α + TV)-quantile of calibration scores, yielding formal certificate P(correct or abstain) ≥ 1 − α under k-poisoning.\n\n**Calibration protocol:** Calibration set constructed on clean corpus (standard assumption per RPS, ICLR 2025), n_cal ≥ 500 per dataset. Sensitivity experiment evaluates coverage degradation when actual poisoning budget exceeds assumed k.\n\n**Step 4: Abstention Decision.** At test time, if s > λ (calibrated threshold), abstain; otherwise, output the majority answer across groups.\n\n## Experimental Design\n\n**Datasets:** Primary: NQ, HotpotQA, MS-MARCO (standard RAG benchmarks, used by PoisonedRAG/RobustRAG). Secondary: PubMedQA (domain-specific, core metrics only, validating high-stakes scenario motivation).\n\n**Attack methods:**\n- PoisonedRAG (targeted, k ∈ {1, 3, 5, 10})\n- CorruptRAG (single-document high-ASR)\n- One DoS-type attack from RSB Benchmark (May 2025) taxonomy\n- **Agreement-aware adaptive attack**: attacker knows K-partition structure and optimizes poisoned passage content to maximize cross-group NLI entailment (minimize s) while ensuring target wrong answer\n\n**Models:** Three scales for model-agnosticism: (1) primary: Qwen3.5-7B (or Llama-3-8B); (2) medium: Qwen3.5-32B; (3) large: Qwen3.5-72B. NLI model: DeBERTa-v3-large.\n\n**Baselines (8 methods):**\n- Conformal: TRAQ (NAACL 2024), C-RAG (ICML 2024), Conformal-RAG (SIGIR 2025)\n- Certified defense: RobustRAG (SaTML 2026), ReliabilityRAG (NeurIPS 2025)\n- Partition-based: RAGPart (arXiv:2512.24268)—same partition, no conformal (ablation baseline)\n- Compute-normalized: TRAQ + K× self-consistency voting\n- Naive pipeline: RobustRAG + TRAQ (empirically validates the \"Why not combine?\" theoretical argument)\n\n**Metrics:**\n- Primary: Certified coverage rate, empirical coverage under attack, abstention rate\n- Secondary: Clean accuracy (no attack), prediction set size, vacuousness rate (per Chen et al. 2026)\n- Tradeoff: Coverage vs. abstention at varying α; coverage vs. poisoning budget k; certified vs. empirical gap\n- Efficiency: Wall-clock time per query, token consumption\n\n**Ablation matrix** (full ablation on 7B only; 32B/72B do core config only):\n- K ∈ {1, 3, 5, 7, 10}: K=1 is the degenerate no-partition baseline proving partition necessity\n- n ∈ {10, 20, 30}: retrieval depth vs. certificate tightness\n- Score function: NLI entailment (primary) vs. ROUGE-L vs. exact match\n- Calibration: CRC + TV inflation (full method) vs. CRC without inflation (isolates TV contribution) vs. vanilla split conformal (isolates CRC contribution)\n- Partition strategy: random vs. round-robin by retrieval score\n\n**Diagnostic experiments:**\n- **NLI reliability**: Collect clean-group and corrupted-group LLM outputs under attack; evaluate DeBERTa NLI entailment accuracy and calibration (reliability diagram) on these output pairs. If unreliable, evaluate ensemble NLI or temperature-scaled NLI as robustness enhancement. Motivated by The Semantic Illusion (arXiv:2512.15068) findings on NLI limitations.\n- **TV bound tightness**: Empirically estimate actual TV distance between clean and poisoned score CDFs (bootstrap/KDE) vs. theoretical m/K bound. Report tightness ratio across attack settings.\n- **k sensitivity**: Evaluate coverage degradation when actual poisoning exceeds assumed k upper bound.\n\n**Scale:** 200-300 queries per dataset per setting (primary datasets); 200 queries for PubMedQA. 95% confidence intervals reported. Full ablation on 7B; 32B/72B validate core configuration only.\n\n**Discussion items:** (1) Partition-induced reduction as a potential general principle for lifting point-estimate certified defenses to distributional guarantees (future work). (2) k-poisoning assumption validity across different attack types. (3) Gradient-based adaptive attacks (Semantic Chameleon) as future robustness evaluation.\n\n## Key References\n\n- TRAQ: Trustworthy Retrieval Augmented QA via Conformal Prediction (NAACL 2024)\n- C-RAG: Certified Generation Risks for RAG (ICML 2024)\n- Conformal Risk Control (ICLR 2024)\n- Provably Reliable Conformal Prediction Sets under Poisoning (ICLR 2025 Spotlight)\n- Certifiably Robust RAG against Retrieval Corruption (SaTML 2026)\n- ReliabilityRAG (NeurIPS 2025)\n- Is Conformal Factuality for RAG-based LLMs Robust? (arXiv:2603.16817, Mar 2026)\n- Conformal-RAG: Conditional Conformal Factuality (SIGIR 2025)\n- CorruptRAG: Practical Poisoning Attacks against RAG (arXiv 2025)\n- PoisonedRAG (USENIX Security 2025)\n- RSB Benchmark: Benchmarking Poisoning Attacks against RAG (May 2025)\n- RAGPart & RAGMask (arXiv:2512.24268, Dec 2025)\n- Conformal Prediction under Lévy-Prokhorov Distribution Shifts (arXiv:2502.14105)\n- Semantic Chameleon (arXiv Mar 2026)\n- Mitigating LLM Hallucinations via Conformal Abstention (arXiv:2405.01563)\n- The Consensus Trap (arXiv:2604.17139, Apr 2026)\n- The Semantic Illusion (arXiv:2512.15068)"
}
```

---

### Runtime record

_source line 2 · 2026-05-30T07:34:52.303Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T07:34:52.303Z",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf"
}
```

---

## Round 1

36 recorded events

### User

_source line 3 · 2026-05-30T07:34:52.323Z_

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
  "promptId": "f0229240-58ff-4aa0-b450-18fffd9fc131",
  "type": "user",
  "uuid": "8eb0f7c8-c48c-418c-8f68-afe3f70307de",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T07:34:52.321Z_

```json
{
  "parentUuid": "8eb0f7c8-c48c-418c-8f68-afe3f70307de",
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
  "uuid": "d5b612b5-1f7a-4ab9-86e5-bdaba7a53fc5",
  "timestamp": "2026-05-30T07:34:52.321Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T07:34:52.321Z_

```json
{
  "parentUuid": "d5b612b5-1f7a-4ab9-86e5-bdaba7a53fc5",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "47e861a9-1ac3-45f1-9f8e-67568c6af96f",
  "timestamp": "2026-05-30T07:34:52.321Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
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
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf"
}
```

---

### Assistant

_source line 7 · 2026-05-30T07:34:58.604Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to act as the "发掘 agent" (Discovery Agent) to analyze this research proposal about "Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores" (PRCA). I need to:

1. First do WebSearch-based literature research (3-5 searches)
2. Then evaluate the proposal on Novelty, Significance, and Related Work differentiation
3. Provide specific suggestions to raise the ceiling of the idea

Let me start by loading the WebSearch tool, then conduct my research.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47e861a9-1ac3-45f1-9f8e-67568c6af96f",
  "isSidechain": false,
  "requestId": "req_011CbYNGRnjSuXM6aQwsFyid",
  "type": "assistant",
  "uuid": "a164f906-dbe6-4d66-ab8b-f60a5347c1b7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TMwbMd454bBGtSEQx1g1qg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5004,
      "cache_read_input_tokens": 14184,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5004,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 5004,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5004
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

_source line 8 · 2026-05-30T07:34:59.261Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NUY1GJZukD4RWV7pAKT199`</summary>

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
  "parentUuid": "a164f906-dbe6-4d66-ab8b-f60a5347c1b7",
  "isSidechain": false,
  "requestId": "req_011CbYNGRnjSuXM6aQwsFyid",
  "type": "assistant",
  "uuid": "7a5e5223-d496-4d6f-a5aa-7691eae52779",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TMwbMd454bBGtSEQx1g1qg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5004,
      "cache_read_input_tokens": 14184,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5004,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 218,
          "cache_read_input_tokens": 14184,
          "cache_creation_input_tokens": 5004,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5004
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

_source line 9 · 2026-05-30T07:34:59.270Z_

<details><summary>↩ Tool result · `toolu_01NUY1GJZukD4RWV7pAKT199`</summary>

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
  "parentUuid": "7a5e5223-d496-4d6f-a5aa-7691eae52779",
  "isSidechain": false,
  "promptId": "f0229240-58ff-4aa0-b450-18fffd9fc131",
  "type": "user",
  "uuid": "77053797-8bde-4076-a353-9f1389b79e63",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "7a5e5223-d496-4d6f-a5aa-7691eae52779",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
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
  "lastPrompt": "# Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores  ## Core Problem  RAG systems in adversarial environments (medical QA, legal retrieval, financial compliance) need distri…",
  "leafUuid": "77053797-8bde-4076-a353-9f1389b79e63",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Poisoning-robust conformal abstention for RAG systems",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf"
}
```

---

### Assistant

_source line 12 · 2026-05-30T07:35:02.887Z_

Now let me conduct the prerequisite literature research. I'll run multiple searches in parallel to cover the key dimensions of this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77053797-8bde-4076-a353-9f1389b79e63",
  "isSidechain": false,
  "requestId": "req_011CbYNGwmHP5tgsH74ckRTL",
  "type": "assistant",
  "uuid": "5a0d0a73-e6f7-4038-a28f-ee586f1643c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cs8k35qjfYhyXJGeAbEQSG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 746,
      "cache_read_input_tokens": 19188,
      "output_tokens": 256,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 256,
          "cache_read_input_tokens": 19188,
          "cache_creation_input_tokens": 746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 746
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

_source line 13 · 2026-05-30T07:35:03.427Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012qBYdiwCqYxXz6SNqJteJG`</summary>

```json
{
  "query": "conformal prediction RAG retrieval augmented generation robustness poisoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a0d0a73-e6f7-4038-a28f-ee586f1643c7",
  "isSidechain": false,
  "requestId": "req_011CbYNGwmHP5tgsH74ckRTL",
  "type": "assistant",
  "uuid": "e828dcc8-b7f0-423a-ba5f-9b3f16eb1a1b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cs8k35qjfYhyXJGeAbEQSG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 746,
      "cache_read_input_tokens": 19188,
      "output_tokens": 256,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 256,
          "cache_read_input_tokens": 19188,
          "cache_creation_input_tokens": 746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 746
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

_source line 14 · 2026-05-30T07:35:04.369Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XR7b3fSgH4Ug5gMVF2oyex`</summary>

```json
{
  "query": "RobustRAG certified defense retrieval corruption conformal abstention 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e828dcc8-b7f0-423a-ba5f-9b3f16eb1a1b",
  "isSidechain": false,
  "requestId": "req_011CbYNGwmHP5tgsH74ckRTL",
  "type": "assistant",
  "uuid": "f554fdc1-6a3b-47b8-a102-b940f36904f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cs8k35qjfYhyXJGeAbEQSG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 746,
      "cache_read_input_tokens": 19188,
      "output_tokens": 256,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 256,
          "cache_read_input_tokens": 19188,
          "cache_creation_input_tokens": 746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 746
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

_source line 15 · 2026-05-30T07:35:04.843Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R6xPVtcRxuWNf91Xr2uynE`</summary>

```json
{
  "query": "conformal risk control distribution shift adversarial robustness 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f554fdc1-6a3b-47b8-a102-b940f36904f0",
  "isSidechain": false,
  "requestId": "req_011CbYNGwmHP5tgsH74ckRTL",
  "type": "assistant",
  "uuid": "5e223b81-65c4-48f9-9771-f6c922fce2e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cs8k35qjfYhyXJGeAbEQSG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 746,
      "cache_read_input_tokens": 19188,
      "output_tokens": 256,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 256,
          "cache_read_input_tokens": 19188,
          "cache_creation_input_tokens": 746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 746
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

_source line 16 · 2026-05-30T07:35:05.299Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ddjb7pNo29QEktQcg5E146`</summary>

```json
{
  "query": "partition-based defense RAG poisoning agreement score 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e223b81-65c4-48f9-9771-f6c922fce2e3",
  "isSidechain": false,
  "requestId": "req_011CbYNGwmHP5tgsH74ckRTL",
  "type": "assistant",
  "uuid": "29e56209-bd83-484e-8f67-ae9ccb347016",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cs8k35qjfYhyXJGeAbEQSG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 746,
      "cache_read_input_tokens": 19188,
      "output_tokens": 256,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 256,
          "cache_read_input_tokens": 19188,
          "cache_creation_input_tokens": 746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 746
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

_source line 17 · 2026-05-30T07:35:10.349Z_

<details><summary>↩ Tool result · `toolu_012qBYdiwCqYxXz6SNqJteJG`</summary>

```text
Web search results for query: "conformal prediction RAG retrieval augmented generation robustness poisoning 2025 2026"

Links: [{"title":"GitHub - Arstanley/Awesome-Trustworthy-RAG · GitHub","url":"https://github.com/Arstanley/Awesome-Trustworthy-RAG"},{"title":"Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks","url":"https://arxiv.org/pdf/2412.16708"},{"title":"Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks","url":"https://arxiv.org/html/2412.16708v2"},{"title":"Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality","url":"https://arxiv.org/html/2506.20978v1"},{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"Practical Poisoning Attacks against Retrieval-Augmented Generation","url":"https://arxiv.org/html/2504.03957v2"},{"title":"[2412.16708] Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks","url":"https://arxiv.org/abs/2412.16708"}]

I found several relevant research papers and resources on this topic. Here's what the search revealed:

## Key Findings

**Conformal Prediction with RAG:**
Conformal-RAG leverages conformal prediction (CP) and internal information from the RAG mechanism to offer statistical guarantees on response quality, ensuring group-conditional coverage spanning multiple sub-domains without requiring manual labelling.

**RAG Robustness and Poisoning Attacks:**
RAG systems are vulnerable to various adversarial poisoning attacks where by injecting adversarial data into the underlying RAG database, attackers can manipulate the retriever to return factually incorrect information, thereby reducing model accuracy and propagating disinformation.

**Recent Defense Mechanisms (2025-2026):**
The search results show several recent papers addressing RAG robustness:
- RAGPart and RAGMask are retrieval-stage defenses that leverage document partitioning and token masking to mitigate poisoning attacks, with findings showing these defenses consistently reduce attack success rates while preserving utility
- Knowledge expansion defense enhances retrieval robustness by enlarging the set of retrieved top-ranked documents, thus increasing the likelihood of including benign information

A curated GitHub repository titled "Awesome-Trustworthy-RAG" contains numerous recent papers (2025-2026) on these topics, including works on conformal prediction with knowledge graphs, RAG safety analysis, and data poisoning attacks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e828dcc8-b7f0-423a-ba5f-9b3f16eb1a1b",
  "isSidechain": false,
  "promptId": "f0229240-58ff-4aa0-b450-18fffd9fc131",
  "type": "user",
  "uuid": "6d0a83c9-2ffc-4d1b-be68-b8334a1d74cb",
  "toolUseResult": {
    "query": "conformal prediction RAG retrieval augmented generation robustness poisoning 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KoQgPUiJtSjsqahnt4JiNF",
        "content": [
          {
            "title": "GitHub - Arstanley/Awesome-Trustworthy-RAG · GitHub",
            "url": "https://github.com/Arstanley/Awesome-Trustworthy-RAG"
          },
          {
            "title": "Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks",
            "url": "https://arxiv.org/pdf/2412.16708"
          },
          {
            "title": "Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks",
            "url": "https://arxiv.org/html/2412.16708v2"
          },
          {
            "title": "Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality",
            "url": "https://arxiv.org/html/2506.20978v1"
          },
          {
            "title": "RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2512.24268"
          },
          {
            "title": "Practical Poisoning Attacks against Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2504.03957v2"
          },
          {
            "title": "[2412.16708] Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks",
            "url": "https://arxiv.org/abs/2412.16708"
          }
        ]
      },
      "I found several relevant research papers and resources on this topic. Here's what the search revealed:\n\n## Key Findings\n\n**Conformal Prediction with RAG:**\nConformal-RAG leverages conformal prediction (CP) and internal information from the RAG mechanism to offer statistical guarantees on response quality, ensuring group-conditional coverage spanning multiple sub-domains without requiring manual labelling.\n\n**RAG Robustness and Poisoning Attacks:**\nRAG systems are vulnerable to various adversarial poisoning attacks where by injecting adversarial data into the underlying RAG database, attackers can manipulate the retriever to return factually incorrect information, thereby reducing model accuracy and propagating disinformation.\n\n**Recent Defense Mechanisms (2025-2026):**\nThe search results show several recent papers addressing RAG robustness:\n- RAGPart and RAGMask are retrieval-stage defenses that leverage document partitioning and token masking to mitigate poisoning attacks, with findings showing these defenses consistently reduce attack success rates while preserving utility\n- Knowledge expansion defense enhances retrieval robustness by enlarging the set of retrieved top-ranked documents, thus increasing the likelihood of including benign information\n\nA curated GitHub repository titled \"Awesome-Trustworthy-RAG\" contains numerous recent papers (2025-2026) on these topics, including works on conformal prediction with knowledge graphs, RAG safety analysis, and data poisoning attacks."
    ],
    "durationSeconds": 6.916650258999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e828dcc8-b7f0-423a-ba5f-9b3f16eb1a1b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-30T07:35:11.602Z_

<details><summary>↩ Tool result · `toolu_01XR7b3fSgH4Ug5gMVF2oyex`</summary>

```text
Web search results for query: "RobustRAG certified defense retrieval corruption conformal abstention 2025 2026"

Links: [{"title":"[2405.15556] Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/abs/2405.15556"},{"title":"Certifiably Robust RAG against Retrieval Corruption - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240515556X/abstract"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/pdf/2405.15556"},{"title":"Certifiably Robust RAG against Retrieval Corruption Attacks | OpenReview","url":"https://openreview.net/forum?id=cU6ZdN87p3"},{"title":"Certifiably Robust RAG against Retrieval Corruption | Request PDF","url":"https://www.researchgate.net/publication/380895542_Certifiably_Robust_RAG_against_Retrieval_Corruption"},{"title":"RobustRAG: A Unique Defense Framework Developed for Opposing Retrieval Corruption Attacks in Retrieval-Augmented Generation (RAG) Systems - MarkTechPost","url":"https://www.marktechpost.com/2024/06/01/robustrag-a-unique-defense-framework-developed-for-opposing-retrieval-corruption-attacks-in-retrieval-augmented-generation-rag-systems/"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://arxiv.org/html/2405.15556"},{"title":"Certifiably Robust RAG against Retrieval Corruption","url":"https://openreview.net/pdf?id=qsEeACAJjD"}]

Based on the search results, here's what I found about RobustRAG:

## Overview

RobustRAG is the first defense framework with certifiable robustness against retrieval corruption attacks. Retrieval-augmented generation (RAG) is susceptible to retrieval corruption attacks, where malicious passages injected into retrieval results can lead to inaccurate model responses.

## Key Mechanism

The key insight of RobustRAG is an isolate-then-aggregate strategy: it isolates passages into disjoint groups, generates LLM responses based on the concatenated passages from each isolated group, and then securely aggregates these responses for a robust output.

RobustRAG designs keyword-based and decoding-based algorithms for securely aggregating unstructured text responses.

## Certifiable Robustness

RobustRAG achieves certifiable robustness: for certain queries in evaluation datasets, it can formally certify non-trivial lower bounds on response quality—even against an adaptive attacker with full knowledge of the defense and the ability to arbitrarily inject a bounded number of malicious passages.

## Performance

RobustRAG achieves 69.0–71.0% certifiable robust accuracy for RQA-MC, 24.0–49.0% for RQA, 27.0–47.0% for NQ, and 24.0–51.2% certifiable LLM-judge score for the bio generation task.

Note: The paper was uploaded in May 2024 and indexed in April 2026, but the search results don't contain specific information about conformal abstention or other details from your complete query phrase.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f554fdc1-6a3b-47b8-a102-b940f36904f0",
  "isSidechain": false,
  "promptId": "f0229240-58ff-4aa0-b450-18fffd9fc131",
  "type": "user",
  "uuid": "d5bd4606-7e45-4876-af59-cef5c1968aa5",
  "toolUseResult": {
    "query": "RobustRAG certified defense retrieval corruption conformal abstention 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SwjD6WtvtPWUd3PCP6aV5u",
        "content": [
          {
            "title": "[2405.15556] Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://arxiv.org/abs/2405.15556"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv240515556X/abstract"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://arxiv.org/pdf/2405.15556"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption Attacks | OpenReview",
            "url": "https://openreview.net/forum?id=cU6ZdN87p3"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption | Request PDF",
            "url": "https://www.researchgate.net/publication/380895542_Certifiably_Robust_RAG_against_Retrieval_Corruption"
          },
          {
            "title": "RobustRAG: A Unique Defense Framework Developed for Opposing Retrieval Corruption Attacks in Retrieval-Augmented Generation (RAG) Systems - MarkTechPost",
            "url": "https://www.marktechpost.com/2024/06/01/robustrag-a-unique-defense-framework-developed-for-opposing-retrieval-corruption-attacks-in-retrieval-augmented-generation-rag-systems/"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://arxiv.org/html/2405.15556"
          },
          {
            "title": "Certifiably Robust RAG against Retrieval Corruption",
            "url": "https://openreview.net/pdf?id=qsEeACAJjD"
          }
        ]
      },
      "Based on the search results, here's what I found about RobustRAG:\n\n## Overview\n\nRobustRAG is the first defense framework with certifiable robustness against retrieval corruption attacks. Retrieval-augmented generation (RAG) is susceptible to retrieval corruption attacks, where malicious passages injected into retrieval results can lead to inaccurate model responses.\n\n## Key Mechanism\n\nThe key insight of RobustRAG is an isolate-then-aggregate strategy: it isolates passages into disjoint groups, generates LLM responses based on the concatenated passages from each isolated group, and then securely aggregates these responses for a robust output.\n\nRobustRAG designs keyword-based and decoding-based algorithms for securely aggregating unstructured text responses.\n\n## Certifiable Robustness\n\nRobustRAG achieves certifiable robustness: for certain queries in evaluation datasets, it can formally certify non-trivial lower bounds on response quality—even against an adaptive attacker with full knowledge of the defense and the ability to arbitrarily inject a bounded number of malicious passages.\n\n## Performance\n\nRobustRAG achieves 69.0–71.0% certifiable robust accuracy for RQA-MC, 24.0–49.0% for RQA, 27.0–47.0% for NQ, and 24.0–51.2% certifiable LLM-judge score for the bio generation task.\n\nNote: The paper was uploaded in May 2024 and indexed in April 2026, but the search results don't contain specific information about conformal abstention or other details from your complete query phrase."
    ],
    "durationSeconds": 7.231036586999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f554fdc1-6a3b-47b8-a102-b940f36904f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-30T07:35:12.669Z_

<details><summary>↩ Tool result · `toolu_01Ddjb7pNo29QEktQcg5E146`</summary>

```text
Web search results for query: "partition-based defense RAG poisoning agreement score 2025 2026"

Links: [{"title":"RAG Poisoning: Threats and Defenses","url":"https://www.emergentmind.com/topics/retrieval-augmented-generation-rag-poisoning"},{"title":"RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2512.24268"},{"title":"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search","url":"https://arxiv.org/pdf/2509.23519"},{"title":"Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions","url":"https://arxiv.org/html/2604.08304v1"},{"title":"May 2026: RAG Poisoning Challenge | redteams.ai","url":"https://redteams.ai/topics/community-challenges/challenge-may-2026"},{"title":"ProvenanceGuard: RAG Retrieval Poisoning Defense Evaluation Dataset | IEEE DataPort","url":"https://ieee-dataport.org/documents/provenanceguard-rag-retrieval-poisoning-defense-evaluation-dataset"}]

Based on the search results, here's what I found about partition-based defense, RAG poisoning, and agreement scores in 2025-2026:

## Partition-Based Defense (RAGPart)

RAGPart leverages the inherent training dynamics of dense retrievers, exploiting document partitioning to mitigate the effect of poisoned points. This approach aggregates over fragment-based index partitions to defeat highly-localized attacks, and was developed by Pathmanathan et al. in December 2025.

## Performance Results

Across two benchmarks, four poisoning strategies, and four state-of-the-art retrievers, the RAGPart and RAGMask defenses consistently reduce attack success rates while preserving utility under benign conditions.

## Related Defense Research (2025-2026)

The search results show this is part of a broader landscape of RAG poisoning defenses:

- Embedding Anomaly Detection detects spiked retrieval similarity or unusual embedding norms/clustering among new documents
- InstructRAG and AstuteRAG prompt the LLM to cross-check context utility and corroborate external claims against internal memory, reducing DoS rates but only partially mitigating targeted poisoning

The research demonstrates active development in RAG security during 2025-2026, with focus on practical defenses against corpus poisoning attacks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29e56209-bd83-484e-8f67-ae9ccb347016",
  "isSidechain": false,
  "promptId": "f0229240-58ff-4aa0-b450-18fffd9fc131",
  "type": "user",
  "uuid": "b23913ec-f3f6-40df-b8be-6fa62be40a3e",
  "toolUseResult": {
    "query": "partition-based defense RAG poisoning agreement score 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012fvccFiEzMSugbst5kECwd",
        "content": [
          {
            "title": "RAG Poisoning: Threats and Defenses",
            "url": "https://www.emergentmind.com/topics/retrieval-augmented-generation-rag-poisoning"
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
            "title": "Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions",
            "url": "https://arxiv.org/html/2604.08304v1"
          },
          {
            "title": "May 2026: RAG Poisoning Challenge | redteams.ai",
            "url": "https://redteams.ai/topics/community-challenges/challenge-may-2026"
          },
          {
            "title": "ProvenanceGuard: RAG Retrieval Poisoning Defense Evaluation Dataset | IEEE DataPort",
            "url": "https://ieee-dataport.org/documents/provenanceguard-rag-retrieval-poisoning-defense-evaluation-dataset"
          }
        ]
      },
      "Based on the search results, here's what I found about partition-based defense, RAG poisoning, and agreement scores in 2025-2026:\n\n## Partition-Based Defense (RAGPart)\n\nRAGPart leverages the inherent training dynamics of dense retrievers, exploiting document partitioning to mitigate the effect of poisoned points. This approach aggregates over fragment-based index partitions to defeat highly-localized attacks, and was developed by Pathmanathan et al. in December 2025.\n\n## Performance Results\n\nAcross two benchmarks, four poisoning strategies, and four state-of-the-art retrievers, the RAGPart and RAGMask defenses consistently reduce attack success rates while preserving utility under benign conditions.\n\n## Related Defense Research (2025-2026)\n\nThe search results show this is part of a broader landscape of RAG poisoning defenses:\n\n- Embedding Anomaly Detection detects spiked retrieval similarity or unusual embedding norms/clustering among new documents\n- InstructRAG and AstuteRAG prompt the LLM to cross-check context utility and corroborate external claims against internal memory, reducing DoS rates but only partially mitigating targeted poisoning\n\nThe research demonstrates active development in RAG security during 2025-2026, with focus on practical defenses against corpus poisoning attacks."
    ],
    "durationSeconds": 7.366529096999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "29e56209-bd83-484e-8f67-ae9ccb347016",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-30T07:35:13.147Z_

<details><summary>↩ Tool result · `toolu_01R6xPVtcRxuWNf91Xr2uynE`</summary>

```text
Web search results for query: "conformal risk control distribution shift adversarial robustness 2025 2026"

Links: [{"title":"Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/html/2502.14105v2"},{"title":"Conformal Prediction under Lévy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations | OpenReview","url":"https://openreview.net/forum?id=1ULQvdbZ3X"},{"title":"Adversarially Robust Conformal Prediction","url":"https://www.emergentmind.com/topics/adversarially-robust-conformal-prediction"},{"title":"Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks","url":"https://arxiv.org/pdf/2511.18562"},{"title":"Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability","url":"https://arxiv.org/html/2506.07804v1"},{"title":"[2510.07750] Calibrating Decision Robustness via Inverse Conformal Risk Control","url":"https://arxiv.org/abs/2510.07750"}]

Based on the search results, here are relevant recent papers and developments in conformal risk control, distribution shift, and adversarial robustness from 2025-2026:

## Key Recent Works

**Conformal Prediction under Distribution Shifts:**

Conformal prediction is a framework for constructing prediction intervals with finite-sample guarantees, though robustness under distribution shifts remains challenging. Recent work addresses this by modeling distribution shifts using Lévy-Prokhorov (LP) ambiguity sets, which capture both local and global perturbations. By propagating the LP ambiguity set through the scoring function, complex high-dimensional distribution shifts reduce to manageable one-dimensional shifts, enabling exact quantification of worst-case quantiles and coverage.

**Adversarially Robust Conformal Prediction:**

Robustness benefits from integrating adversarial training with conformal loss objectives, with frameworks like OPSA attacking the set size directly through a bilevel min-max paradigm. Recent work shows that prediction coverage varies monotonically with calibration-time attack strength, enabling control of coverage under adversarial tests.

**Conformal Risk Control Applications:**

A new framework provides distribution-free, finite-sample guarantees on both miscoverage and regret for robust predict-then-optimize policies. This approach enables decision-makers to evaluate tradeoffs between robustness and cost.

Adversarially robust conformal prediction is rapidly developing with diverse algorithmic paradigms delivering provable guarantees and practical efficiency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e223b81-65c4-48f9-9771-f6c922fce2e3",
  "isSidechain": false,
  "promptId": "f0229240-58ff-4aa0-b450-18fffd9fc131",
  "type": "user",
  "uuid": "e45c2ed8-8921-4702-ab12-465dbf7e4e15",
  "toolUseResult": {
    "query": "conformal risk control distribution shift adversarial robustness 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AdPcfz7fDvhZuVB93FYey9",
        "content": [
          {
            "title": "Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/html/2502.14105v2"
          },
          {
            "title": "Conformal Prediction under Lévy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations | OpenReview",
            "url": "https://openreview.net/forum?id=1ULQvdbZ3X"
          },
          {
            "title": "Adversarially Robust Conformal Prediction",
            "url": "https://www.emergentmind.com/topics/adversarially-robust-conformal-prediction"
          },
          {
            "title": "Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks",
            "url": "https://arxiv.org/pdf/2511.18562"
          },
          {
            "title": "Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability",
            "url": "https://arxiv.org/html/2506.07804v1"
          },
          {
            "title": "[2510.07750] Calibrating Decision Robustness via Inverse Conformal Risk Control",
            "url": "https://arxiv.org/abs/2510.07750"
          }
        ]
      },
      "Based on the search results, here are relevant recent papers and developments in conformal risk control, distribution shift, and adversarial robustness from 2025-2026:\n\n## Key Recent Works\n\n**Conformal Prediction under Distribution Shifts:**\n\nConformal prediction is a framework for constructing prediction intervals with finite-sample guarantees, though robustness under distribution shifts remains challenging. Recent work addresses this by modeling distribution shifts using Lévy-Prokhorov (LP) ambiguity sets, which capture both local and global perturbations. By propagating the LP ambiguity set through the scoring function, complex high-dimensional distribution shifts reduce to manageable one-dimensional shifts, enabling exact quantification of worst-case quantiles and coverage.\n\n**Adversarially Robust Conformal Prediction:**\n\nRobustness benefits from integrating adversarial training with conformal loss objectives, with frameworks like OPSA attacking the set size directly through a bilevel min-max paradigm. Recent work shows that prediction coverage varies monotonically with calibration-time attack strength, enabling control of coverage under adversarial tests.\n\n**Conformal Risk Control Applications:**\n\nA new framework provides distribution-free, finite-sample guarantees on both miscoverage and regret for robust predict-then-optimize policies. This approach enables decision-makers to evaluate tradeoffs between robustness and cost.\n\nAdversarially robust conformal prediction is rapidly developing with diverse algorithmic paradigms delivering provable guarantees and practical efficiency."
    ],
    "durationSeconds": 8.300890337,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5e223b81-65c4-48f9-9771-f6c922fce2e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-30T07:35:18.998Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CjEVLbSR8CsTj8AMiAp1kZ`</summary>

```json
{
  "query": "\"consensus trap\" multi-agent majority voting adversarial corruption 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e45c2ed8-8921-4702-ab12-465dbf7e4e15",
  "isSidechain": false,
  "requestId": "req_011CbYNHxbRFfiqXrJCqwNTG",
  "type": "assistant",
  "uuid": "4bd68065-34ac-4c25-81a3-823bd07a6794",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJiesyci4WWYifkKmfH6Ko",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 683,
      "cache_creation_input_tokens": 2579,
      "cache_read_input_tokens": 19934,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2579,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 683,
          "output_tokens": 125,
          "cache_read_input_tokens": 19934,
          "cache_creation_input_tokens": 2579,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2579
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

_source line 22 · 2026-05-30T07:35:19.978Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01USX6Z8F32AWp4uTcS3LCju`</summary>

```json
{
  "query": "conformal abstention LLM hallucination self-consistency nonconformity score 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bd68065-34ac-4c25-81a3-823bd07a6794",
  "isSidechain": false,
  "requestId": "req_011CbYNHxbRFfiqXrJCqwNTG",
  "type": "assistant",
  "uuid": "e9f3920d-3506-48d8-8b39-3da6f3ddded8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJiesyci4WWYifkKmfH6Ko",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 683,
      "cache_creation_input_tokens": 2579,
      "cache_read_input_tokens": 19934,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2579,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 683,
          "output_tokens": 125,
          "cache_read_input_tokens": 19934,
          "cache_creation_input_tokens": 2579,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2579
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

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores  ## Core Problem  RAG systems in adversarial environments (medical QA, legal retrieval, financial compliance) need distri…",
  "leafUuid": "e9f3920d-3506-48d8-8b39-3da6f3ddded8",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Poisoning-robust conformal abstention for RAG systems",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf"
}
```

---

### Tool result

_source line 25 · 2026-05-30T07:35:28.343Z_

<details><summary>↩ Tool result · `toolu_01USX6Z8F32AWp4uTcS3LCju`</summary>

```text
Web search results for query: "conformal abstention LLM hallucination self-consistency nonconformity score 2025 2026"

Links: [{"title":"A method to mitigate hallucinations in large language models","url":"https://techxplore.com/news/2024-05-method-mitigate-hallucinations-large-language.html"},{"title":"[2405.01563] Mitigating LLM Hallucinations via Conformal Abstention","url":"https://arxiv.org/abs/2405.01563"},{"title":"NeurIPS Mitigating LLM Hallucinations via ConformalAbstention","url":"https://neurips.cc/virtual/2024/105548"},{"title":"[PDF] Mitigating LLM Hallucinations via Conformal Abstention | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mitigating-LLM-Hallucinations-via-Conformal-Abbasi-Yadkori-Kuzborskij/b5cd6bc53343f2ad8a7c7830555d8c744e626245"},{"title":"Conformal Abstention Framework","url":"https://www.emergentmind.com/topics/conformal-abstention"},{"title":"Mitigating LLM Hallucinations via Conformal Abstention | alphaXiv","url":"https://www.alphaxiv.org/abs/2405.1563"},{"title":"Uncertainty-Based Abstention in LLMs Improves Safety and Reduces   Hallucinations","url":"https://arxiv.org/pdf/2404.10960"},{"title":"Learning Conformal Abstention Policies for Adaptive Risk Management in Large Language and Vision-Language Models","url":"https://arxiv.org/html/2502.06884v1"}]

The search results provide comprehensive information about conformal abstention methods for mitigating LLM hallucinations. Here are the key findings:

## Overview of Conformal Abstention for LLM Hallucinations

Conformal abstention is a principled procedure for determining when a large language model should abstain from responding (by saying "I don't know") instead of resorting to potentially hallucinating a non-sensical or incorrect answer.

## Core Methodology

The approach builds on self-consistency as a measure of model confidence by using the LLM itself to self-evaluate the similarity between its sampled responses for a given query, then leverages conformal prediction techniques to develop an abstention procedure with rigorous theoretical guarantees on the hallucination rate.

## Technical Implementation

The framework quantifies prediction uncertainty via nonconformity scores and applies thresholding rules to decide when a model should abstain, balancing risk and informativeness.

## Recent Advances (2025)

Recent evaluations show improvements including accuracy gains up to 3.2%, AUROC boosts for hallucination detection of 22.19%, and 70%–85% reductions in calibration error across diverse benchmarks.

## Future Research Directions

Ongoing research is formalizing robustness under covariate shift and advancing toward adaptive, data-driven, and multimodal selective prediction, including hierarchical abstention at phrase or rationale levels and integration of multiple nonconformity signals for multimodal and retrieval-augmented scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9f3920d-3506-48d8-8b39-3da6f3ddded8",
  "isSidechain": false,
  "promptId": "f0229240-58ff-4aa0-b450-18fffd9fc131",
  "type": "user",
  "uuid": "b6a556a6-e65f-46a8-a93d-a8ef6aeaaf65",
  "toolUseResult": {
    "query": "conformal abstention LLM hallucination self-consistency nonconformity score 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_019RUWPLXmJUB4EN2VnBVs1m",
        "content": [
          {
            "title": "A method to mitigate hallucinations in large language models",
            "url": "https://techxplore.com/news/2024-05-method-mitigate-hallucinations-large-language.html"
          },
          {
            "title": "[2405.01563] Mitigating LLM Hallucinations via Conformal Abstention",
            "url": "https://arxiv.org/abs/2405.01563"
          },
          {
            "title": "NeurIPS Mitigating LLM Hallucinations via ConformalAbstention",
            "url": "https://neurips.cc/virtual/2024/105548"
          },
          {
            "title": "[PDF] Mitigating LLM Hallucinations via Conformal Abstention | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Mitigating-LLM-Hallucinations-via-Conformal-Abbasi-Yadkori-Kuzborskij/b5cd6bc53343f2ad8a7c7830555d8c744e626245"
          },
          {
            "title": "Conformal Abstention Framework",
            "url": "https://www.emergentmind.com/topics/conformal-abstention"
          },
          {
            "title": "Mitigating LLM Hallucinations via Conformal Abstention | alphaXiv",
            "url": "https://www.alphaxiv.org/abs/2405.1563"
          },
          {
            "title": "Uncertainty-Based Abstention in LLMs Improves Safety and Reduces   Hallucinations",
            "url": "https://arxiv.org/pdf/2404.10960"
          },
          {
            "title": "Learning Conformal Abstention Policies for Adaptive Risk Management in Large Language and Vision-Language Models",
            "url": "https://arxiv.org/html/2502.06884v1"
          }
        ]
      },
      "The search results provide comprehensive information about conformal abstention methods for mitigating LLM hallucinations. Here are the key findings:\n\n## Overview of Conformal Abstention for LLM Hallucinations\n\nConformal abstention is a principled procedure for determining when a large language model should abstain from responding (by saying \"I don't know\") instead of resorting to potentially hallucinating a non-sensical or incorrect answer.\n\n## Core Methodology\n\nThe approach builds on self-consistency as a measure of model confidence by using the LLM itself to self-evaluate the similarity between its sampled responses for a given query, then leverages conformal prediction techniques to develop an abstention procedure with rigorous theoretical guarantees on the hallucination rate.\n\n## Technical Implementation\n\nThe framework quantifies prediction uncertainty via nonconformity scores and applies thresholding rules to decide when a model should abstain, balancing risk and informativeness.\n\n## Recent Advances (2025)\n\nRecent evaluations show improvements including accuracy gains up to 3.2%, AUROC boosts for hallucination detection of 22.19%, and 70%–85% reductions in calibration error across diverse benchmarks.\n\n## Future Research Directions\n\nOngoing research is formalizing robustness under covariate shift and advancing toward adaptive, data-driven, and multimodal selective prediction, including hierarchical abstention at phrase or rationale levels and integration of multiple nonconformity signals for multimodal and retrieval-augmented scenarios."
    ],
    "durationSeconds": 8.361812658000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e9f3920d-3506-48d8-8b39-3da6f3ddded8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-30T07:35:30.644Z_

<details><summary>↩ Tool result · `toolu_01CjEVLbSR8CsTj8AMiAp1kZ`</summary>

```text
Web search results for query: ""consensus trap" multi-agent majority voting adversarial corruption 2026"

Links: [{"title":"[2604.17139] The Consensus Trap: Rescuing Multi-Agent LLMs from Adversarial Majorities via Token-Level Collaboration","url":"https://arxiv.org/abs/2604.17139"},{"title":"The Consensus Trap: Rescuing Multi-Agent LLMs from Adversarial Majorities via Token-Level Collaboration","url":"https://arxiv.org/html/2604.17139"},{"title":"The Pass@k Trap: Why Running Your AI Agent 3 Times Makes Answers Worse – TALVINDER","url":"https://talvinder.com/field-notes/consensus-is-not-verification/"},{"title":"Consensus Protocols for Multi-Agent Systems - 2026 Guide | Fastio","url":"https://fast.io/resources/consensus-protocols-multi-agent-systems/"},{"title":"When collaboration fails: persuasion driven adversarial influence in multi agent large language model debate | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-42705-7"},{"title":"Why Consensus Voting Fails for Agent Truthfulness - DEV Community","url":"https://dev.to/talvinder/why-consensus-voting-fails-for-agent-truthfulness-105f"},{"title":"Building an Adversarial Consensus Engine | Multi-Agent LLMs for Automated Malware Analysis | SentinelOne","url":"https://www.sentinelone.com/labs/building-an-adversarial-consensus-engine-multi-agent-llms-for-automated-malware-analysis/"}]

I found several relevant results on this topic. Here's what the search revealed:

## The Consensus Trap

Multi-agent LLM systems increasingly use response-level aggregation like Majority Voting to improve reasoning, but this approach has a critical structural vulnerability: response-level aggregation collapses when corrupted agents form a local majority.

Voting aggregates fully-formed conclusions, making it blind to flawed intermediate logic.

## Adversarial Corruption Vulnerabilities

In open environments, agents are highly susceptible to stealthy contextual corruption, such as targeted prompt injections. Experimental results show that adversarial agents can lower system accuracy by 10–40% while increasing consensus on incorrect answers by more than 30%.

## Token-Level Collaboration Solution

To address this vulnerability, researchers proposed Token-Level Round-Robin (RR) Collaboration, where agents sequentially interleave generation within a shared auto-regressive context. This formalizes aggregation as a discrete-time dynamical system, proving that token-level interleaving transitions from a brittle counting of final votes to a dynamic, interwoven chain of logic. Through this approach, the honest model's restorative pull can overpower adversarial corruptions, even when corrupted agents form a majority.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4bd68065-34ac-4c25-81a3-823bd07a6794",
  "isSidechain": false,
  "promptId": "f0229240-58ff-4aa0-b450-18fffd9fc131",
  "type": "user",
  "uuid": "7dad968a-6118-43f1-a66f-d531a82fa1ad",
  "toolUseResult": {
    "query": "\"consensus trap\" multi-agent majority voting adversarial corruption 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GrSvyBz66LNaGKrGuRe9YN",
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
            "title": "Consensus Protocols for Multi-Agent Systems - 2026 Guide | Fastio",
            "url": "https://fast.io/resources/consensus-protocols-multi-agent-systems/"
          },
          {
            "title": "When collaboration fails: persuasion driven adversarial influence in multi agent large language model debate | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-026-42705-7"
          },
          {
            "title": "Why Consensus Voting Fails for Agent Truthfulness - DEV Community",
            "url": "https://dev.to/talvinder/why-consensus-voting-fails-for-agent-truthfulness-105f"
          },
          {
            "title": "Building an Adversarial Consensus Engine | Multi-Agent LLMs for Automated Malware Analysis | SentinelOne",
            "url": "https://www.sentinelone.com/labs/building-an-adversarial-consensus-engine-multi-agent-llms-for-automated-malware-analysis/"
          }
        ]
      },
      "I found several relevant results on this topic. Here's what the search revealed:\n\n## The Consensus Trap\n\nMulti-agent LLM systems increasingly use response-level aggregation like Majority Voting to improve reasoning, but this approach has a critical structural vulnerability: response-level aggregation collapses when corrupted agents form a local majority.\n\nVoting aggregates fully-formed conclusions, making it blind to flawed intermediate logic.\n\n## Adversarial Corruption Vulnerabilities\n\nIn open environments, agents are highly susceptible to stealthy contextual corruption, such as targeted prompt injections. Experimental results show that adversarial agents can lower system accuracy by 10–40% while increasing consensus on incorrect answers by more than 30%.\n\n## Token-Level Collaboration Solution\n\nTo address this vulnerability, researchers proposed Token-Level Round-Robin (RR) Collaboration, where agents sequentially interleave generation within a shared auto-regressive context. This formalizes aggregation as a discrete-time dynamical system, proving that token-level interleaving transitions from a brittle counting of final votes to a dynamic, interwoven chain of logic. Through this approach, the honest model's restorative pull can overpower adversarial corruptions, even when corrupted agents form a majority."
    ],
    "durationSeconds": 11.641381016000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4bd68065-34ac-4c25-81a3-823bd07a6794",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-30T07:35:34.975Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me do one more targeted search to understand whether the specific "partition-induced reduction to bounded TV shift" idea has been explored before, and to check if there's any work that already combines conformal abstention with adversarial robustness in the RAG setting specifically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7dad968a-6118-43f1-a66f-d531a82fa1ad",
  "isSidechain": false,
  "requestId": "req_011CbYNKFSDRZRw3Ux2RTfNo",
  "type": "assistant",
  "uuid": "f5c557ed-be22-426d-b14c-3ba79cac1ab2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pc9dtkj1g3Yw4HAqgQedjL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 839,
      "cache_creation_input_tokens": 1546,
      "cache_read_input_tokens": 22513,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1546,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 839,
          "output_tokens": 200,
          "cache_read_input_tokens": 22513,
          "cache_creation_input_tokens": 1546,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1546
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

_source line 28 · 2026-05-30T07:35:36.068Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SAiPSkv6aBq5CoJwsohz9M`</summary>

```json
{
  "query": "total variation shift conformal prediction calibration robust partition aggregation certificate 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5c557ed-be22-426d-b14c-3ba79cac1ab2",
  "isSidechain": false,
  "requestId": "req_011CbYNKFSDRZRw3Ux2RTfNo",
  "type": "assistant",
  "uuid": "b2d3c0e3-8223-4f77-9153-70ba54ca62d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pc9dtkj1g3Yw4HAqgQedjL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 839,
      "cache_creation_input_tokens": 1546,
      "cache_read_input_tokens": 22513,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1546,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 839,
          "output_tokens": 200,
          "cache_read_input_tokens": 22513,
          "cache_creation_input_tokens": 1546,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1546
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

_source line 29 · 2026-05-30T07:35:36.878Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011N4nsFTNJAXebzzbJJUCqK`</summary>

```json
{
  "query": "Chen arXiv 2603.16817 conformal factuality RAG robust distribution shift 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2d3c0e3-8223-4f77-9153-70ba54ca62d4",
  "isSidechain": false,
  "requestId": "req_011CbYNKFSDRZRw3Ux2RTfNo",
  "type": "assistant",
  "uuid": "7f41684f-c56b-42ff-8568-328bc62dd9cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pc9dtkj1g3Yw4HAqgQedjL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 839,
      "cache_creation_input_tokens": 1546,
      "cache_read_input_tokens": 22513,
      "output_tokens": 200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1546,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 839,
          "output_tokens": 200,
          "cache_read_input_tokens": 22513,
          "cache_creation_input_tokens": 1546,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1546
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

_source line 30 · 2026-05-30T07:35:42.652Z_

<details><summary>↩ Tool result · `toolu_01SAiPSkv6aBq5CoJwsohz9M`</summary>

```text
Web search results for query: "total variation shift conformal prediction calibration robust partition aggregation certificate 2025 2026"

Links: [{"title":"Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/html/2502.14105v2"},{"title":"Robust Conformal Prediction with a Single Binary Certificate","url":"https://arxiv.org/pdf/2503.05239"},{"title":"Robust Conformal Prediction with a Single Binary Certificate","url":"https://arxiv.org/html/2503.05239v1"},{"title":"Doubly Robust Calibration of Prediction Sets under Covariate Shift","url":"https://arxiv.org/pdf/2203.01761"},{"title":"Robust Conformal Prediction under Distribution Shift via   Physics-Informed Structural Causal Model","url":"https://arxiv.org/pdf/2403.15025"},{"title":"Wasserstein-Regularized Conformal Prediction under General Distribution Shift | OpenReview","url":"https://openreview.net/forum?id=aJ3tiX1Tu4"},{"title":"Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/pdf/2502.14105"}]

Based on the search results, I found several relevant recent papers on conformal prediction with robustness to distribution shifts:

## Key Findings:

**Recent Papers on Robust Conformal Prediction:**

1. **Conformal Prediction under Lévy-Prokhorov Distribution Shifts** - This paper addresses robustness of conformal prediction under distribution shifts by modeling them using Lévy-Prokhorov (LP) ambiguity sets, which capture both local and global perturbations.

2. **Robust Conformal Prediction with a Single Binary Certificate** - Recent robust conformal prediction baselines use a conservative score at test time that is a certified bound on the conformity score of the clean unseen input, where certified bounds can be derived through model-dependent verifiers or smoothing-based black-box certificates.

3. **Wasserstein-Regularized Conformal Prediction under General Distribution Shift** - This work bounds the coverage gap by Wasserstein distance between calibration and test conformal scores, noting that prior studies bound the gap using total variation distance.

4. **Doubly Robust Calibration of Prediction Sets under Covariate Shift** - This paper addresses obtaining distribution-free prediction regions accounting for a shift in the distribution of covariates between training and test data using semiparametric efficiency theory.

These papers represent cutting-edge research in 2025-2026 on robust conformal prediction methods for handling distribution shifts while maintaining coverage guarantees.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2d3c0e3-8223-4f77-9153-70ba54ca62d4",
  "isSidechain": false,
  "promptId": "f0229240-58ff-4aa0-b450-18fffd9fc131",
  "type": "user",
  "uuid": "c8353832-1914-46f1-998c-7ac80dd75f07",
  "toolUseResult": {
    "query": "total variation shift conformal prediction calibration robust partition aggregation certificate 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DQNMBd1gz5zsvu6s9WuK6u",
        "content": [
          {
            "title": "Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/html/2502.14105v2"
          },
          {
            "title": "Robust Conformal Prediction with a Single Binary Certificate",
            "url": "https://arxiv.org/pdf/2503.05239"
          },
          {
            "title": "Robust Conformal Prediction with a Single Binary Certificate",
            "url": "https://arxiv.org/html/2503.05239v1"
          },
          {
            "title": "Doubly Robust Calibration of Prediction Sets under Covariate Shift",
            "url": "https://arxiv.org/pdf/2203.01761"
          },
          {
            "title": "Robust Conformal Prediction under Distribution Shift via   Physics-Informed Structural Causal Model",
            "url": "https://arxiv.org/pdf/2403.15025"
          },
          {
            "title": "Wasserstein-Regularized Conformal Prediction under General Distribution Shift | OpenReview",
            "url": "https://openreview.net/forum?id=aJ3tiX1Tu4"
          },
          {
            "title": "Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/pdf/2502.14105"
          }
        ]
      },
      "Based on the search results, I found several relevant recent papers on conformal prediction with robustness to distribution shifts:\n\n## Key Findings:\n\n**Recent Papers on Robust Conformal Prediction:**\n\n1. **Conformal Prediction under Lévy-Prokhorov Distribution Shifts** - This paper addresses robustness of conformal prediction under distribution shifts by modeling them using Lévy-Prokhorov (LP) ambiguity sets, which capture both local and global perturbations.\n\n2. **Robust Conformal Prediction with a Single Binary Certificate** - Recent robust conformal prediction baselines use a conservative score at test time that is a certified bound on the conformity score of the clean unseen input, where certified bounds can be derived through model-dependent verifiers or smoothing-based black-box certificates.\n\n3. **Wasserstein-Regularized Conformal Prediction under General Distribution Shift** - This work bounds the coverage gap by Wasserstein distance between calibration and test conformal scores, noting that prior studies bound the gap using total variation distance.\n\n4. **Doubly Robust Calibration of Prediction Sets under Covariate Shift** - This paper addresses obtaining distribution-free prediction regions accounting for a shift in the distribution of covariates between training and test data using semiparametric efficiency theory.\n\nThese papers represent cutting-edge research in 2025-2026 on robust conformal prediction methods for handling distribution shifts while maintaining coverage guarantees."
    ],
    "durationSeconds": 6.578924601999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b2d3c0e3-8223-4f77-9153-70ba54ca62d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-30T07:35:43.472Z_

<details><summary>↩ Tool result · `toolu_011N4nsFTNJAXebzzbJJUCqK`</summary>

```text
Web search results for query: "Chen arXiv 2603.16817 conformal factuality RAG robust distribution shift 2026"

Links: [{"title":"[2603.16817] Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/abs/2603.16817"},{"title":"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights","url":"https://arxiv.org/pdf/2603.16817"},{"title":"Not all distributional shifts are equal: Fine-grained robust conformal inference","url":"https://arxiv.org/pdf/2402.13042"},{"title":"When Environments Shift: Safe Planning with Generative Priors and Robust Conformal Prediction","url":"https://arxiv.org/pdf/2602.12616"},{"title":"Robust Conformal Prediction under Distribution Shift via   Physics-Informed Structural Causal Model","url":"https://arxiv.org/pdf/2403.15025"},{"title":"Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/html/2502.14105v2"},{"title":"Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations","url":"https://arxiv.org/pdf/2502.14105"}]

I found the paper you're looking for! Here are the key details:

The paper is titled "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights" by Yi Chen and 4 other authors, and it was published on March 17, 2026.

The paper addresses how large language models frequently hallucinate, limiting their reliability in knowledge-intensive applications, and explores how retrieval-augmented generation (RAG) and conformal factuality can address this limitation.

The main findings are: conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs; conformal factuality guarantee is not robust to distribution shifts and distractors, highlighting the limitation that requires calibration data to closely match deployment conditions; and lightweight entailment-based verifiers match or outperform LLM-based model confidence scorers while requiring over 100× fewer FLOPs.

You can access the paper directly at https://arxiv.org/abs/2603.16817


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f41684f-c56b-42ff-8568-328bc62dd9cf",
  "isSidechain": false,
  "promptId": "f0229240-58ff-4aa0-b450-18fffd9fc131",
  "type": "user",
  "uuid": "f1b06d27-3e97-4cf3-9506-5023251d7226",
  "toolUseResult": {
    "query": "Chen arXiv 2603.16817 conformal factuality RAG robust distribution shift 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GbDGeo5iUAiPFrpqKvxKnS",
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
            "title": "When Environments Shift: Safe Planning with Generative Priors and Robust Conformal Prediction",
            "url": "https://arxiv.org/pdf/2602.12616"
          },
          {
            "title": "Robust Conformal Prediction under Distribution Shift via   Physics-Informed Structural Causal Model",
            "url": "https://arxiv.org/pdf/2403.15025"
          },
          {
            "title": "Conformal Prediction under Lévy–Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/html/2502.14105v2"
          },
          {
            "title": "Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
            "url": "https://arxiv.org/pdf/2502.14105"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details:\n\nThe paper is titled \"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights\" by Yi Chen and 4 other authors, and it was published on March 17, 2026.\n\nThe paper addresses how large language models frequently hallucinate, limiting their reliability in knowledge-intensive applications, and explores how retrieval-augmented generation (RAG) and conformal factuality can address this limitation.\n\nThe main findings are: conformal filtering suffers from low usefulness at high factuality levels due to vacuous outputs; conformal factuality guarantee is not robust to distribution shifts and distractors, highlighting the limitation that requires calibration data to closely match deployment conditions; and lightweight entailment-based verifiers match or outperform LLM-based model confidence scorers while requiring over 100× fewer FLOPs.\n\nYou can access the paper directly at https://arxiv.org/abs/2603.16817"
    ],
    "durationSeconds": 6.589355381999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7f41684f-c56b-42ff-8568-328bc62dd9cf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-30T07:35:43.477Z_

```json
{
  "parentUuid": "f1b06d27-3e97-4cf3-9506-5023251d7226",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "4a602e52-49c4-4fbc-8ec1-5987db061904",
  "timestamp": "2026-05-30T07:35:43.477Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 33 · 2026-05-30T07:36:44.190Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture of the research landscape. Let me analyze this proposal carefully.

Key findings from my research:

1. **Chen et al. (arXiv:2603.16817, Mar 2026)** - Confirmed: shows conformal factuality for RAG is NOT robust to distribution shifts and distractors. This paper identifies the problem but proposes no solution. This validates PRCA's problem statement.

2. **RobustRAG (SaTML 2026)** - Uses isolate-then-aggregate strategy (partition passages into disjoint groups, generate per-group, aggregate). 

PRCA claims its key innovation is adding conformal abstention with coverage certificates, but RobustRAG already employs the same partitioning approach—so the real novelty lies in how PRCA reduces the partition structure to a TV shift problem with conformal risk control.

3. **LP-shift framework (arXiv:2502.14105)** - Reduces high-dimensional distribution shifts to one-dimensional score shifts via ambiguity sets. PRCA's partition-induced TV bound appears to be a specific instantiation of this, which is theoretically sound but suggests the underlying technique isn't entirely novel.

4. **Conformal Abstention (arXiv:2405.01563)** - Uses self-consistency as...

Self-consistency fails as a nonconformity score under poisoning since all samples share the same poisoned context. PRCA correctly identifies this limitation.

5. **The Consensus Trap (arXiv:2604.17139, Apr 2026)** - Response-level majority voting breaks down when adversaries control the majority. PRCA's approach addresses this partially.

6. **Robust Conformal Prediction with a Single Binary Certificate (arXiv:2503.05239)** - Provides certified bounds on conformity scores and could be relevant to PRCA's framework.

7. **RAGPart (arXiv:2512.24268)** - Applies partitioning at the retrieval stage, whereas PRCA operates at generation and calibration.

Looking at the novelty here, the core contribution is the chain from partitioning through inter-group agreement to bounded TV shift and then CRC absorption. RobustRAG already handles the partitioning piece, so I need to assess whether the reduction mechanism itself is sufficiently novel.

The genuine contribution appears to be combining inter-group agreement as a nonconformity score with a TV bound proof and integrating this with CRC for formal coverage guarantees—no existing work has merged certified RAG defenses with conformal abstention guarantees. That said, this feels more like bridging two established frameworks rather than introducing fundamentally new methodology.

On significance, the problem matters in high-stakes settings and Chen et al. clearly demonstrate the gap in distribution-free abstention under poisoning. The real question is whether the coverage certificates remain useful in practice—if TV inflation drives abstention rates too high, the method becomes impractical.

The related work section does strong positioning work, especially the "Why not simply combine?" argument that clearly differentiates from RobustRAG, TRAQ, and other baselines. But I'm seeing two major concerns: first, whether empirical calibration of uncertainty scores after RobustRAG aggregation could sidestep the theoretical argument about uncharacterized distribution shift, and second, how tight the TV bound actually is in realistic settings.

Looking at the numbers, with K=5 partitions and k=5 poisoned documents in a set of 20, the TV bound reaches 0.4, which could inflate the CRC quantile enough to make coverage certificates loose and drive up abstention rates significantly. There's also a conceptual issue—RobustRAG already uses partitioning, so the claim that partitioning is a theoretical necessity for PRCA specifically needs refinement; it's really about how partitioning enables the TV reduction, not that it's unique to this approach. The proposal hints at a "lifting" principle that could generalize beyond this specific application.

The real strength here is that PRCA produces a continuous nonconformity score enabling calibrated abstention at any coverage level, whereas RobustRAG only gives binary certified/not-certified decisions. There's also a formal parallel to Byzantine fault tolerance—the k-poisoning plus K-partition plus majority agreement structure mirrors the n > 2f + 1 requirement from distributed systems, and emphasizing this connection could make the theoretical contribution more compelling.

Now I'm examining what's actually novel in this work. The partition-agreement-TV bound-CRC pipeline is the specific combination that's new—partitioning for RAG defense exists in RobustRAG, agreement-based nonconformity scoring exists in conformal abstention work, and TV-bounded CRC exists in the literature, but nobody's put these pieces together for RAG poisoning defense before. The novelty is incremental but meaningful.

A reviewer familiar with both RobustRAG and CRC might initially think this is obvious—partition the groups, compute agreement, and naturally the TV shift is bounded by the corruption fraction. That feels almost tautological. But the real strength is showing why three natural alternatives fail and articulating the partition-induced reduction as a general principle.

The discovery space is there, though it's more about theoretical framing and connecting existing ideas than introducing fundamentally new methods. I should focus on elevating the lifting principle as the core contribution.

Actually, stepping back—the proposal is already quite solid. The lifting principle is present, the distinction from RobustRAG is clear, and the TV bound tightness is addressed through empirical estimation. I'm probably overthinking this.

That said, there are still some genuine refinements worth considering: elevating the lifting principle as the core framing would make the contribution land harder, sharpening the focus on score function design with bounded sensitivity as the real innovation rather than the partitioning itself, and adding theoretical evidence for TV bound tightness alongside the empirical validation would give the paper more rigor.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a602e52-49c4-4fbc-8ec1-5987db061904",
  "isSidechain": false,
  "requestId": "req_011CbYNLCPgqFi9gdPvgjMLR",
  "type": "assistant",
  "uuid": "1f93de51-835e-4bd6-8e1d-d7cdac8d0160",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqhoNUZ1Qe6A6XXaM9WVqT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2500,
      "cache_read_input_tokens": 24059,
      "output_tokens": 6561,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2500,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6561,
          "cache_read_input_tokens": 24059,
          "cache_creation_input_tokens": 2500,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2500
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

_source line 34 · 2026-05-30T07:38:22.334Z_

Now I have sufficient research context. Let me synthesize my findings and provide the evaluation.

---

【状态】: 有发掘空间

【前置调研发现】
- **Chen et al. (arXiv:2603.16817, Mar 2026)**: 直接验证了 PRCA 的问题设定——现有 RAG conformal factuality 方法在 distribution shift 和 distractor 下产生 vacuous 输出，但未提出解决方案。核心发现：lightweight entailment-based verifiers 匹配甚至优于 LLM-based scorers 且 FLOPs 少 100×。
- **RobustRAG (arXiv:2405.15556, SaTML 2026)**: 已使用 isolate-then-aggregate 的 partition 结构，但输出是 robust point estimate（certified robust accuracy 在 NQ 上约 27-47%），无 coverage certificate 或 calibrated abstention 机制。
- **LP-shift framework (arXiv:2502.14105, 2025)**: 将高维分布偏移通过 ambiguity set 归约为一维 score 偏移，提供 worst-case quantile 精确量化。PRCA 的 TV bound 是这一思路在 adversarial retrieval corruption 上的具体实例化。
- **Robust CP with Binary Certificate (arXiv:2503.05239, 2025)**: 通过 certified bound on conformity score 实现 robust CP，使用 model-dependent verifiers 或 smoothing-based certificates。与 PRCA 的 structural TV bound 路线不同但目标相似。
- **Conformal Abstention (arXiv:2405.01563, NeurIPS 2024)**: 用 self-consistency 作为 nonconformity score 进行 abstention，无 adversarial robustness 考虑。PRCA 正确识别了其在 poisoning 下的失败模式。
- **The Consensus Trap (arXiv:2604.17139, Apr 2026)**: 证明 response-level majority voting 在 adversarial majority 下失败，提出 token-level round-robin 替代。直接威胁 PRCA 的 majority answer output，但 PRCA 主要保证是 abstention certificate 而非 answer correctness。
- **Wasserstein-Regularized CP (OpenReview, 2025)**: 用 Wasserstein 距离 bound coverage gap，指出先前工作用 TV 距离 bound gap。提供了 PRCA 选择 TV metric 的替代视角。
- 调研总结：这个领域当前研究者沿两条平行线推进——(1) certified RAG defense（RobustRAG、ReliabilityRAG）追求 robust point estimate，(2) conformal prediction for RAG（TRAQ、C-RAG、Conformal-RAG）追求 distribution-free coverage guarantee——但两条线尚未交汇。PRCA 的定位正是填补这个交汇点，这一 gap 是真实存在的。

---

【发掘点 1】
- 维度: 核心 claim 强化 / significance 提升
- 内容: 当前 proposal 将 "partition-induced reduction" 定位为 PRCA 的 *内部机制*，但在 Discussion 中提到它可能是 "lifting point-estimate certified defenses to distributional guarantees 的一般原则"。建议将这一 **lifting principle 从 Discussion 提升为与 PRCA 方法并列的核心贡献**。具体论述：任何使用 partition-and-aggregate 结构的 certified defense（RobustRAG 的 isolate-then-aggregate、ReliabilityRAG 的 graph-based filtering、甚至联邦学习中的 Byzantine-resilient aggregation）都可以通过 partition → inter-component agreement score → bounded TV shift → CRC 这一管线获得 distribution-free abstention guarantee。PRCA-for-RAG 是这一原则的第一个实例化。这样做将论文的影响力从 "RAG-specific method" 提升到 "general principle with broad applicability"，显著增加 significance 得分。注意：这不需要额外实验，只需要在理论部分增加一个 general theorem（partition + bounded corruption → bounded TV on agreement score）和若干 instantiation example。
- 价值: 命中 Significance 维度。AAAI 审稿人偏好有通用性的贡献。一个仅适用于 RAG 的方法 vs. 一个以 RAG 为首要实例但原则上通用的 framework，后者的天花板明显更高。
- 调研依据: LP-shift framework (arXiv:2502.14105) 已成功通过 "将特定领域问题归约为一般性框架" 获得高影响力。PRCA 的 partition-induced TV bound 与 LP-shift 的 ambiguity-set reduction 在结构上平行，但 PRCA 目前未充分利用这一平行性。

【发掘点 2】
- 维度: novelty 锐化
- 内容: 当前 proposal 的 novelty 叙事存在一个微妙风险：审稿人可能认为 "partition passages + compute agreement" 只是 RobustRAG 的变体，因为 RobustRAG *已经* 做了 partition-and-aggregate。建议 **锐化 novelty 叙述的核心对象**：PRCA 的真正创新不是 partition 本身（RobustRAG 已有），而是 **将 agreement 设计为一个具有 bounded sensitivity 的一维 nonconformity score function**——这个 score function 在 adversarial corruption 下的偏移量可被 partition structure 精确 bound，因此可被 CRC 吸收。对比：RobustRAG 的 partition 服务于 aggregation（输出 robust answer），PRCA 的 partition 服务于 **score construction**（输出 bounded nonconformity score）。这是两个根本不同的用途。建议在论文中显式使用 "partition-for-aggregation vs. partition-for-scoring" 这一对比术语，一句话说清 novelty 落点。
- 价值: 命中 Novelty 维度。消除审稿人 "这不就是 RobustRAG + conformal prediction 吗" 的第一反应。Proposal 的 "Why not simply combine?" 部分已经论证了 naive combination 会失败，但还需要在正面叙述中锐化 novelty 的落点——不是 "我们做了 partition"，而是 "我们发现 partition 结构使 agreement score 的 adversarial sensitivity 可量化"。
- 调研依据: RobustRAG (SaTML 2026) 的 isolate-then-aggregate 已被社区熟知。Robust CP with Binary Certificate (arXiv:2503.05239) 也使用 score-level certified bound 思路，但依赖 model-dependent verifiers，而 PRCA 的 bound 来自 partition combinatorics，是 model-agnostic 的——这个差异值得强调。

【发掘点 3】
- 维度: 前提假设质疑 / trivial alternative 威胁
- 内容: Proposal 声称 "RobustRAG + standard CP" 失败因为 "aggregation transforms the output distribution in a poisoning-dependent manner, and the magnitude of distributional shift is uncharacterized"。但一个自然的 trivial alternative 需要更认真地排除：**在 RobustRAG 的 isolate-then-aggregate 输出上，直接用 empirical calibration 学一个 post-hoc threshold（而非理论 TV bound）做 abstention**。具体来说：用一个混合了 clean 和 poisoned 样本的 validation set 来校准 RobustRAG 输出的 uncertainty score（如 logprob entropy），然后用 standard split conformal 做 abstention。虽然没有 formal certificate under adversarial corruption，但在 practical deployment 中可能 empirically 足够好。Proposal 需要明确论证：(1) 为什么 formal certificate 在这个 threat model 下是必要的（不是所有场景都需要 worst-case guarantee），(2) 即使只看 empirical performance，PRCA 的 agreement score 是否优于 post-hoc calibrated RobustRAG uncertainty。如果论文只能在 "有 formal certificate" 这一点上胜过 trivial alternative，而 empirical coverage 差不多，审稿人可能会质疑 practical significance。
- 价值: 命中 Novelty 维度（排除 trivial alternative 是 novelty 的前提条件）。这不是致命问题，但如果不正面回应，可能被审稿人作为 weakness 提出。建议在 baselines 中加入 "RobustRAG + empirically calibrated abstention" 作为对比（这属于补救 agent 的范畴），同时在 motivation 部分论证 formal guarantee 的不可替代性——例如在 FDA-regulated medical QA 或 legal compliance 场景中，empirical performance 不够，需要 provable coverage bound。
- 调研依据: Chen et al. (arXiv:2603.16817) 发现 conformal factuality 在 distribution shift 下不 robust，但其研究的是 *理论保证的失效*，empirical coverage 的退化程度取决于具体 shift magnitude。这意味着 "empirical calibration might still work reasonably well in practice" 是一个需要排除的 alternative。

【发掘点 4】
- 维度: significance 提升 / 核心 claim 强化
- 内容: 当前 proposal 的 coverage certificate 依赖于 CRC + TV inflation，quantile 被 inflate 到 (1 − α + TV)。当 TV = m/K 较大时（例如 K=5, m=2 → TV=0.4），inflate 后的 quantile 为 1 − α + 0.4，在 α=0.1 时为 1.3——超过 1，certificate 变为 vacuous（永远 abstain）。这意味着 **在高 poisoning budget 下 certificate 可能 trivially vacuous**，严重削弱 significance。建议 Proposal 做两件事：(1) **明确界定 certificate 有意义的 (k, K, n) 参数区间**，给出 non-vacuousness condition：TV = ceil(k/floor(n/K)) / K < α，即证书非 vacuous 的充要条件。例如在 α=0.1, n=20 时，需要 K ≥ 10m，给出几组典型参数的 non-vacuousness 表格。(2) **讨论 tighter TV bound 的可能性**——当前 TV ≤ m/K 是 worst-case combinatorial bound，但 agreement score 作为 pairwise entailment 的均值，可能存在 concentration-based tighter bound（proposal 已提到但建议更强势地 push：将 tighter bound 作为一个可能的理论贡献，而非仅仅"未来方向"）。如果能在论文中给出 even slightly tighter bound（哪怕是 under additional mild assumptions），将显著增加理论贡献。
- 价值: 命中 Significance 和 Novelty 维度。Vacuous certificate 是这类方法的阿喀琉斯之踵。审稿人一定会计算 quantile inflation 的值并质疑 non-vacuousness。提前给出参数区间和 tighter bound 方向，可以从 "potential weakness" 转化为 "honest and thorough analysis"。
- 调研依据: Wasserstein-Regularized CP (OpenReview 2025) 指出 TV 距离是 bound coverage gap 的常用但非唯一选择，Wasserstein 距离可能给出 tighter bound。LP-shift framework 也探索了不同 ambiguity set 的 tightness tradeoff。PRCA 可以讨论是否 Wasserstein-based bound 能替代 TV bound 获得更 tight 的 certificate，即使不在本文实现，也显示理论视野。

【发掘点 5】
- 维度: related work 差异化
- 内容: Proposal 对 The Consensus Trap (arXiv:2604.17139, Apr 2026) 的回应是 "(a) PRCA 的主要保证是 abstention certificate 而非 majority answer correctness; (b) k < n/2 下 honest majority 被保持"。但这个回应有一个逻辑漏洞需要堵上：**PRCA 在不 abstain 时输出 majority answer，如果 majority answer 是错的，即使 abstention decision 有 certificate，用户仍然收到错误答案**。也就是说，coverage guarantee P(correct or abstain) ≥ 1 − α 的 "correct" 部分依赖于 majority answer 的 correctness，而 Consensus Trap 恰恰攻击的就是 majority correctness。建议 Proposal 更精确地论述：(1) 在 PRCA 的 threat model 下（k < n/2 corrupted passages, not groups），Consensus Trap 的 "adversarial majority" 是否可能在 group level 发生？给出 k 的 threshold。(2) 如果 Consensus Trap 攻击确实可能导致 majority answer 错误，那么 PRCA 的 coverage guarantee 应该 degrade gracefully——此时 agreement score 会偏高（因为 corrupted groups 之间可能达成一致但与 clean groups 不一致），触发 abstention。这实际上是 PRCA 设计的一个 hidden strength：当 majority voting 不可靠时，agreement score 自然会反映出 disagreement，leading to abstention。这个论点如果清晰地论证出来，会显著强化 PRCA 相对于 Consensus Trap 的定位。
- 价值: 命中 Related Work 差异化和核心 claim 强化。Consensus Trap 是 2026 年 4 月的新工作，审稿人很可能引用它来质疑 PRCA 的 majority voting 组件。提前给出严密回应是必要的。
- 调研依据: The Consensus Trap (arXiv:2604.17139) 的核心发现是 adversarial agents 可以降低系统 accuracy 10-40% 同时增加 incorrect consensus 30%+。其 token-level round-robin 解决方案与 PRCA 的 partition structure 在精神上互补——partition isolates corruption at generation, token-level RR isolates corruption at aggregation——但 PRCA 目前未讨论这种互补性。

Sources:
- [Is Conformal Factuality for RAG-based LLMs Robust?](https://arxiv.org/abs/2603.16817)
- [Certifiably Robust RAG against Retrieval Corruption](https://arxiv.org/abs/2405.15556)
- [Conformal Prediction under Lévy-Prokhorov Distribution Shifts](https://arxiv.org/html/2502.14105v2)
- [Robust Conformal Prediction with a Single Binary Certificate](https://arxiv.org/html/2503.05239v1)
- [The Consensus Trap](https://arxiv.org/abs/2604.17139)
- [RAGPart & RAGMask](https://arxiv.org/pdf/2512.24268)
- [Mitigating LLM Hallucinations via Conformal Abstention](https://arxiv.org/abs/2405.01563)
- [Wasserstein-Regularized CP under General Distribution Shift](https://openreview.net/forum?id=aJ3tiX1Tu4)
- [Conformal Abstention Framework](https://www.emergentmind.com/topics/conformal-abstention)
- [RAG Poisoning: Threats and Defenses](https://www.emergentmind.com/topics/retrieval-augmented-generation-rag-poisoning)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f93de51-835e-4bd6-8e1d-d7cdac8d0160",
  "isSidechain": false,
  "requestId": "req_011CbYNLCPgqFi9gdPvgjMLR",
  "type": "assistant",
  "uuid": "dd5c0dc7-d573-4bb3-b790-ea343361f105",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqhoNUZ1Qe6A6XXaM9WVqT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2500,
      "cache_read_input_tokens": 24059,
      "output_tokens": 6561,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2500,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6561,
          "cache_read_input_tokens": 24059,
          "cache_creation_input_tokens": 2500,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2500
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
  "lastPrompt": "# Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores  ## Core Problem  RAG systems in adversarial environments (medical QA, legal retrieval, financial compliance) need distri…",
  "leafUuid": "dd5c0dc7-d573-4bb3-b790-ea343361f105",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Poisoning-robust conformal abstention for RAG systems",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Poisoning-Robust Conformal Abstention for RAG via Retrieval-Agreement Scores  ## Core Problem  RAG systems in adversarial environments (medical QA, legal retrieval, financial compliance) need distri…",
  "leafUuid": "dd5c0dc7-d573-4bb3-b790-ea343361f105",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Poisoning-robust conformal abstention for RAG systems",
  "sessionId": "d030526f-3fa5-4808-bdfe-56665260e1cf"
}
```

---
